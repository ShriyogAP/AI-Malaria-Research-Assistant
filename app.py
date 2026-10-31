import os
import re
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

APP_DIR = Path(__file__).parent
KB_PATH = APP_DIR / "data" / "knowledge_base.md"

st.set_page_config(page_title="AI Malaria Research Assistant", page_icon="🦟", layout="wide")

st.title("🦟 AI Malaria Research Assistant")
st.caption("A source-grounded educational prototype for learning about malaria and malaria research.")

st.warning(
    "Educational use only — this tool cannot diagnose malaria or recommend treatment for an individual. "
    "If malaria is suspected, seek prompt assessment from a qualified healthcare professional. "
    "Severe symptoms such as confusion, seizures, or difficulty breathing require emergency care."
)

@st.cache_data
def load_knowledge_base():
    raw = KB_PATH.read_text(encoding="utf-8")
    # Split on document headings while retaining the heading in each chunk.
    chunks = re.split(r"(?=^## SOURCE:)", raw, flags=re.MULTILINE)
    return [c.strip() for c in chunks if c.strip() and c.strip().startswith("## SOURCE:")]

def retrieve(query, chunks, top_k=3):
    if not chunks:
        return []
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(chunks + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    order = scores.argsort()[::-1][:top_k]
    return [(chunks[i], float(scores[i])) for i in order if scores[i] > 0]

def get_source_title(chunk):
    first_line = chunk.splitlines()[0]
    return first_line.replace("## SOURCE:", "").strip()

def answer_with_openai(question, context):
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key or OpenAI is None:
        return None
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an educational malaria research assistant. Answer only from the supplied context. "
                    "If the context does not answer the question, say so and suggest consulting the linked official sources. "
                    "Do not diagnose, prescribe, estimate an individual's probability of infection, or replace clinical care. "
                    "For personal symptoms, advise prompt professional assessment. For confusion, seizures, difficulty breathing, "
                    "impaired consciousness, or other severe symptoms, advise emergency care. Clearly distinguish established "
                    "facts from uncertainty. Cite source titles in square brackets."
                ),
            },
            {
                "role": "user",
                "content": f"Question:\n{question}\n\nRetrieved source context:\n{context}",
            },
        ],
    )
    return response.choices[0].message.content

chunks = load_knowledge_base()

with st.sidebar:
    st.header("About this prototype")
    st.write("**Method:** Retrieval-Augmented Generation (RAG) concept")
    st.write("1. Search a small curated knowledge base with TF-IDF.")
    st.write("2. Pass the most relevant passages to an LLM when an API key is configured.")
    st.write("3. Show the sources used.")
    st.divider()
    st.write("**AI mode**")
    if os.getenv("OPENAI_API_KEY", "").strip() and OpenAI is not None:
        st.success("LLM mode available")
    else:
        st.info("Demo mode: source retrieval with a grounded extractive summary. Add OPENAI_API_KEY to enable LLM answers.")
    st.caption("No questions are intentionally saved by this app.")

example_questions = [
    "What causes malaria and how does it spread?",
    "What symptoms can occur with malaria?",
    "How do healthcare professionals test for malaria?",
    "What is the difference between Plasmodium falciparum and Plasmodium vivax?",
    "How can people reduce mosquito bites?",
    "How is a CNN used in malaria blood-cell image research?",
]

st.subheader("Ask a research question")
question = st.text_area(
    "Enter a question about malaria, diagnosis, prevention, or research methods",
    placeholder="For example: How do researchers use CNNs to classify malaria blood-smear images?",
    height=90,
)

selected = st.selectbox("Or try an example question", ["Choose an example…"] + example_questions)
if not question.strip() and selected != "Choose an example…":
    question = selected

if st.button("Find an answer", type="primary", use_container_width=True):
    if not question.strip():
        st.error("Please enter a question or choose an example.")
    else:
        with st.spinner("Searching trusted sources…"):
            results = retrieve(question, chunks)
        if not results:
            st.info(
                "I could not find a relevant passage in the current knowledge base. "
                "Try rephrasing the question or consult the official sources listed below."
            )
        else:
            context = "\n\n".join(
                f"[{get_source_title(chunk)}]\n{chunk}" for chunk, score in results
            )
            answer = None
            try:
                answer = answer_with_openai(question, context)
            except Exception as exc:
                st.error("The AI API could not be reached. Showing retrieved-source demo output instead.")
                st.caption(f"Technical detail: {type(exc).__name__}")
            if answer:
                st.subheader("AI-generated answer")
                st.write(answer)
                st.caption("Generated from retrieved context. Verify important information against the linked sources.")
            else:
                st.subheader("Retrieved information (demo mode)")
                st.write(
                    "No live language-model answer was generated in this run. The passages below are the "
                    "most relevant matches from the curated knowledge base; use them to review the source information."
                )
                for i, (chunk, score) in enumerate(results, start=1):
                    with st.expander(f"{i}. {get_source_title(chunk)} — relevance {score:.2f}"):
                        st.markdown(chunk)

            st.subheader("Sources used")
            for chunk, score in results:
                title_line = get_source_title(chunk)
                url_match = re.search(r"URL:\s*(https?://\S+)", chunk)
                url = url_match.group(1) if url_match else ""
                if url:
                    st.markdown(f"- [{title_line}]({url})")
                else:
                    st.markdown(f"- {title_line}")

st.divider()
st.subheader("Research note: CNN-based malaria image classification")
st.write(
    "Convolutional Neural Networks (CNNs) can be explored in research that classifies microscope images "
    "of blood cells. Model performance depends on dataset quality, labeling, train/test separation, and "
    "external validation. This application does not run an image classifier and does not interpret uploaded "
    "blood-smear images."
)
st.caption("Prototype prepared for an AI-tools project challenge. Review and update the source collection before any real-world use.")
