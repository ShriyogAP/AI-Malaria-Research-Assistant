# AI Malaria Research Assistant

A small educational RAG-style web app that retrieves information from a curated starter knowledge base about malaria and malaria research.

## Features
- Streamlit web interface
- TF-IDF retrieval over curated source summaries
- Optional LLM answer generation using an OpenAI API key
- Source links displayed with retrieved results
- Demo mode works without an API key
- Safety note: this app does not diagnose malaria, interpret patient images, or recommend treatment

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the app: `streamlit run app.py`
6. Open the local address printed by Streamlit.

## Enable live AI answers (optional)
Set `OPENAI_API_KEY` as an environment variable before running the app. Keep the key private and do not upload it to GitHub. Without a key, the app still runs in demo mode and shows the retrieved passages.

## How it works
1. The question and knowledge-base chunks are vectorized with TF-IDF.
2. Cosine similarity ranks the most relevant passages.
3. If an API key is configured, the top passages are supplied to the LLM with instructions to answer only from the supplied context.
4. The interface displays source links for verification.

This is a lightweight RAG demonstration, not a clinical decision-support tool. It does not currently load or run a CNN image classifier.

## Suggested manual tests
- Submit an empty question.
- Ask: "What causes malaria and how does it spread?"
- Ask: "How do healthcare professionals test for malaria?"
- Ask an unrelated question, such as "How do I repair a bicycle?" and confirm the app explains that it could not find a relevant passage.
- Run once without an API key to confirm demo mode works.
- If using an API key, test that the answer stays grounded in the supplied context and that medical safety language remains visible.

## Knowledge sources
- WHO, Malaria fact sheet: https://www.who.int/news-room/fact-sheets/detail/malaria
- CDC, About Malaria: https://www.cdc.gov/malaria/about/index.html
- CDC, Testing for Malaria: https://www.cdc.gov/malaria/testing/
- CDC, Symptoms of Malaria: https://www.cdc.gov/malaria/symptoms/
- NLM, Malaria Dataset research resource: https://lhncbc.nlm.nih.gov/LHC-publications/pubs/MalariaDataset.html

Review official sources regularly; this small collection is not comprehensive.
