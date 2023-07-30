import os
import sys

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader


def process_llm_response(llm_response):
    print(llm_response['result'])
    print('\n\nSources:')
    for source in llm_response["source_documents"]:
        print(source.metadata['source'])

if __name__ == '__main__':
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if openai_api_key is None or 0 == len(openai_api_key):
        sys.exit(1)
    print(openai_api_key)

    loader = DirectoryLoader('./articles', glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    print(f'number of documents: {len(documents)}')

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    print(f'number of texts: {len(texts)}')

    #   Create Chroma DB
    persist_directory = 'db'

    embedding = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=persist_directory)

    vectordb.persist()
    vectordb = None

    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding)

    retriever = vectordb.as_retriever()

    docs = retriever.get_relevant_documents("What is Generative AI?")

    for doc in docs:
        print(doc.metadata["source"])

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    docs = retriever.get_relevant_documents("What is Generative AI?")

    for doc in docs:
        print(doc.metadata["source"])

    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True)

    queries = ["How much money did Pando raise?",
                "Who led the round in Pando?",
                "What did Databricks acquire?",
                "What is Generative AI?",
                "Who is CMA?",
                ]
    for query in queries:
        llm_response = qa_chain(query)
        process_llm_response(llm_response)
