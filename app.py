import streamlit as st
from llm import LLM

llm=LLM()

st.title('DocRAG :sunglasses:')

col1, col2 = st.columns(2)

with col1:

    url=str(st.text_input(
        "Enter source URL",
        "URL"
    ))
    
    status=st.button("Load Document", type="primary")
    
    
    if status:
        with st.spinner('Loading documents into vector store. Please wait...'):
            llm.loadDocumentsToVectorStore(urls=[url])
        st.success('Document loading done!')
        
        question=st.text_input(
        "Ask Questions :",
        "Enter question"
        )
        ask=st.button("Ask", type="primary")
        
with col2:
    with st.spinner('Answering ....'):
        st.subheader('Result')
        response=llm.answerQuestions(question=question)
        st.write(response['result'])
        
        st.subheader('Reference : ')   
        st.write(response['source_documents'])
            



