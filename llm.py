from langchain.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import GooglePalm
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv


load_dotenv('.env')


class LLM(object):
    def __init__(self) -> None:
        os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
        self.llm=GooglePalm(api_key=os.environ['GOOGLE_API_KEY'])
        
    def loadDocumentsToVectorStore(self, urls:list):
        loader=UnstructuredURLLoader(urls=urls)
        documents=loader.load()
        
        textSplitter=RecursiveCharacterTextSplitter(separators=['\n', '\n \n', ' '], chunk_size=500, chunk_overlap=100)
        splitedDocuments=textSplitter.split_documents(documents)
        
        model_name = "BAAI/bge-large-en"
        model_kwargs = {'device': 'cpu'}

        embeddings = HuggingFaceBgeEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
        )
        
        vectorStore=FAISS.from_documents(documents=splitedDocuments, embedding=embeddings)
        
        self.retriever=vectorStore.as_retriever()
            
    
    def answerQuestions(self, question:str):
        
        prompt_template = """Given the following context and a question, generate an answer based on this context only.
                        In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
                        If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

                        CONTEXT: {context}

                        QUESTION: {question}"""

        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        chain_type_kwargs = {"prompt": PROMPT}

        chain = RetrievalQA.from_chain_type(llm=self.llm,
                                    chain_type="stuff",
                                    retriever=self.retriever,
                                    input_key="query",
                                    return_source_documents=True,
                                    chain_type_kwargs=chain_type_kwargs)
        
        response=chain(question)
        
        return response
