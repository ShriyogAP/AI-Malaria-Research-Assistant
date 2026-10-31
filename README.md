# 🦟 AI Malaria Research Assistant

### An AI-powered educational prototype for malaria research and information retrieval.

The **AI Malaria Research Assistant** is a web application designed to help users explore malaria-related information, including symptoms, diagnosis, prevention, and research methods. It retrieves relevant information from a curated knowledge base and displays the sources used.

This project demonstrates how AI-assisted development, information retrieval, and Retrieval-Augmented Generation (RAG) concepts can be applied to healthcare education.

## 🎯 Project Objectives

- Make malaria research information easier to explore.
- Retrieve relevant passages from a curated knowledge base.
- Display source references to support transparent, evidence-based learning.
- Demonstrate a practical application of AI and information retrieval in healthcare.

## ✨ Key Features

- **Interactive web interface:** Enter a research question or select an example question.
- **Source-grounded retrieval:** Retrieve relevant passages using TF-IDF-based text matching.
- **Source references:** Display links to the original information sources.
- **Demo mode:** Explore retrieved information without requiring an API key.
- **Optional LLM integration:** Support language-model-generated answers when the required API configuration is provided.
- **Healthcare safety notice:** Clearly communicate that the application is educational and cannot diagnose malaria or prescribe treatment.

## 🛠️ Technologies Used

- Python
- Streamlit
- TF-IDF information retrieval
- Retrieval-Augmented Generation (RAG) concepts
- OpenAI API integration (optional)
- Markdown-based knowledge base
- Git and GitHub
- AI tools for project development and debugging

## ⚙️ How It Works

1. The user enters a question about malaria or malaria research.
2. The application searches a curated collection of educational information.
3. TF-IDF-based matching identifies passages relevant to the question.
4. The application displays the retrieved passages and their sources.
5. When an API key is configured, the application can use an LLM to generate an answer grounded in the retrieved information.

**Note:** Without the API key, the application operates in demo mode and displays retrieved passages rather than generating a live LLM answer.

## 📚 Knowledge Sources

The curated knowledge base includes educational information from:

- [World Health Organization — Malaria Fact Sheet](https://www.who.int/news-room/fact-sheets/detail/malaria)
- [CDC — About Malaria](https://www.cdc.gov/malaria/about/index.html)
- [CDC — Testing for Malaria](https://www.cdc.gov/malaria/testing/)
- [CDC — Symptoms of Malaria](https://www.cdc.gov/malaria/symptoms/)
- [National Library of Medicine — Malaria Cell Image Dataset](https://lhncbc.nlm.nih.gov/LHC-publications/pubs/MalariaDataset.html)

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or later
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ShriyogAP/AI-Malaria-Research-Assistant.git
cd AI-Malaria-Research-Assistant
```

**2. Install the dependencies**

```bash
pip install -r requirements.txt
```

**3. Start the application**

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

### Optional API Configuration

To enable language-model-generated answers, configure an OpenAI API key using Streamlit secrets or an environment variable, as supported by the application.

Never upload API keys, passwords, or other secrets to GitHub.

## 🧪 Example Questions

Try asking:

- What causes malaria and how does it spread?
- What are the symptoms of malaria?
- How is malaria diagnosed?
- How can malaria be prevented?
- How do researchers use CNNs to classify malaria blood-smear images?

## ⚠️ Limitations and Responsible Use

- This is an educational prototype, not a medical diagnostic tool.
- It does not replace professional medical advice or laboratory testing.
- It does not currently run a CNN model or classify uploaded blood-smear images.
- The quality of retrieved information depends on the knowledge base and retrieval method.
- Medical information should be checked against current official guidance.

Anyone who suspects malaria should seek prompt assessment from a qualified healthcare professional. Severe symptoms, including confusion, seizures, or difficulty breathing, require emergency care.

## 📁 Project Structure

```text
AI-Malaria-Research-Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── knowledge_base.md
├── data/
│   └── knowledge_base.md
├── prompt_documentation.md
├── prompt_documentation.docx
└── video_presentation_script.docx
```

*The file structure above reflects the expected project files; check your repository to confirm the exact locations before final submission.*

## 🤖 Use of AI Tools

AI tools were used to support project planning, code development, prompt refinement, troubleshooting, and documentation.

The development process involved refining instructions, testing the application with sample questions, identifying a knowledge-base loading issue, and correcting the file formatting and retrieval workflow.

## 📦 Project Deliverables

- **Source code:** Available in this GitHub repository.
- **Prompt documentation:** Documents the prompts and revisions used during development.
- **Video presentation:** Explains the project objectives, AI tools, development approach, challenges, and final demonstration.
- **Live application:** Access the deployed application through the Streamlit link provided with the submission.

## 👨‍💻 Author

**Shriyog A P**

Electronics and Communication Engineering Graduate

---

*Developed as a practical AI-tools project demonstrating healthcare information retrieval and responsible AI application development.*
