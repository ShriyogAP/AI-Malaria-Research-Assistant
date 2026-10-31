# AI Malaria Research Assistant — Prompt Documentation

**Important:** These are proposed development prompts. Replace or annotate them with the exact prompts actually used and add genuine iteration results.

## 1. Planning
I want to build an AI Malaria Research Assistant for an AI project challenge. It should answer educational questions about malaria using trusted sources, retrieve relevant passages, and show source links. Help me define a small working prototype using Python and Streamlit. Do not make it a diagnostic tool or claim it can identify malaria in a person.

## 2. Retrieval architecture
Design a simple RAG workflow for a small curated knowledge base. Use TF-IDF and cosine similarity to retrieve relevant passages. Explain limitations and provide modular Python code.

## 3. User interface
Create a Streamlit interface with a question box, example questions, submit button, retrieved passages, source links, workflow description, and a persistent medical safety disclaimer.

## 4. LLM grounding and safety
Add optional LLM answers using an environment variable for the API key. Answer only from retrieved context, cite source titles, say when context is insufficient, avoid diagnosis or prescribing, and direct people with possible malaria symptoms to professional assessment. Do not expose secrets.

## 5. Fallback and error handling
Make the app work without an API key by showing retrieved passages in demo mode. Handle empty input, no relevant results, and API errors. Never claim an LLM answer was generated if it was not.

## 6. Testing
Review correctness, security, usability, and healthcare safety. Suggest tests for empty input, relevant/irrelevant questions, source visibility, missing API key, and API failure. Separate tests actually run from tests recommended.

## 7. Iteration log template
- Date / iteration:
- Problem observed:
- Prompt revision:
- Change made:
- Test performed:
- Result and next improvement:
