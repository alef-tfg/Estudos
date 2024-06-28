from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url, language = 'pt')
    transcript = loader.load() 

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model="gpt-3.5-turbo-instruct")
    
    prompt = PromptTemplate(
        input_variables=["question", 'docs'],
        template = """
        Você é um assistente muito útil para assuntos 
        do youtube que pode responder questões baseadas em 
        transcrições de videos.
        
        Responda a seguinte questão: {question}
        Utilizando como fonte a transcrição do video {docs}

        apenas use informações fatuais da transcrição do video para 
        responder a questão.

        Se você sente que não tem informação o sufivciente para
        responder a questão diga "Eu não sei".

        Suas respostas devem ser detalhadas.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question = query, docs = docs_page_content)
    response = response.replace("\n", "")
    return response, docs
