# DocRAG

## Overview
DocRAG is an advanced document analysis and retrieval application powered by the LangChain Palm2 model, FAISS for efficient similarity search, and Hugging Face embeddings. It enables users to upload various types of documents or provide URLs, allowing them to obtain summaries or answers to specific questions related to the uploaded content.

## Features

- Document Upload: Users can upload documents of different formats or provide URLs to online documents.
- Question Answering: DocRAG utilizes the RAG (Retrieval-Augmented Generation) capabilities of the LangChain Palm2 model to answer user-specified questions based on the uploaded documents.
- Automatic Summarization: Generates concise summaries of uploaded documents using advanced natural language processing techniques.
- Efficient Document Retrieval: FAISS is employed for fast and accurate similarity search among documents, ensuring relevant results are retrieved swiftly.
- Intuitive Interface: A user-friendly interface makes it easy for users to upload documents, choose actions (summarization or question answering), and view results seamlessly.

## Technologies Used
- LangChain Palm2 Model: State-of-the-art large language model for understanding and generating human-like text.
- FAISS: A library for efficient similarity search and clustering of dense vectors.
- Hugging Face Embeddings: Pre-trained embeddings for document representation and similarity computation, enhancing accuracy and performance.

## Usage
- Upload Documents: Users upload documents or provide URLs to documents.

## Choose Action:
- Summarize: Obtain a summarized version of the uploaded document(s).
- Question Answering: Ask specific questions related to the content of the uploaded document(s).
- View Results: Receive summaries or answers based on the uploaded documents.

## Installation

1. Clone the repository:
```
git clone https://github.com/pinilDissanayaka/DocRAG.git
cd DocRAG
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Start the application:
```
streamlit run app.py
```

4. Access the application at http://localhost:5000 in your web browser.
   
### Example
Imagine a user uploads a research paper on climate change. They can ask questions like "What are the main conclusions of this study?" or request a summary of the document. DocRAG will utilize its powerful capabilities to generate relevant answers or summaries based on the content provided.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
LangChain for providing the Palm2 model.
Hugging Face for their contributions to the NLP community.
FAISS developers for the efficient similarity search library.
