from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from youtube_transcript_loader import YouTubeTranscriptLoader

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "text-embedding-3-large"
LLM_MODEL = "gpt-4o-mini"


class YouTubeRAGChatbot:
    def __init__(self, youtube_url: str):
        # Load transcript
        loader = YouTubeTranscriptLoader(youtube_url)
        documents = loader.load()

        # Chunk documents
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = splitter.split_documents(documents)

        # Vector store
        embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        vector_store = FAISS.from_documents(chunks, embeddings)

        # Memory (short-term, exact)
        memory = ConversationBufferWindowMemory(
            k=4,
            memory_key="chat_history",
            return_messages=True
        )

        # Prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are an AI assistant answering questions strictly using the provided context. "
             "If the answer is not found in the context, say "
             "'I could not find this information in the provided video content.'"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human",
             "Context:\n{context}\n\nQuestion:\n{question}")
        ])

        # Conversational RAG chain
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model=LLM_MODEL, temperature=0),
            retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
            memory=memory,
            combine_docs_chain_kwargs={"prompt": prompt},
            return_source_documents=True
        )

    def ask(self, question: str) -> dict:
        response = self.chain({"question": question})
        return {
            "answer": response["answer"],
            "sources": list(
                set(doc.metadata["source"] for doc in response["source_documents"])
            )
        }
