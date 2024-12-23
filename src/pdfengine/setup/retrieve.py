from src.pdfengine.setup.embedding import VectorRetriever
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class RetrievalChain(object):
    def __init__(self, open_api_key_, model_, file_path):
        self.open_api_key = open_api_key_
        self.model = model_
        self.file_path = file_path

    def define_output_parser(self):
        return StrOutputParser()

    def give_llm(self):
        # ChatOpenAI()
        return ChatOpenAI(api_key=self.open_api_key, model= self.model)

    def prepare_chain_llm_output_parser(self):
        llm = self.give_llm()
        sop = self.define_output_parser()
        chain = llm | sop
        return chain

    def prepare_the_prompt(self):
        prompt = ChatPromptTemplate.from_template(
                """Answer the following question IN TURKISH LANGUAGE ONLY based on provided context, and also answer the questions which can not be answered from the given context. \
                    And if the input given to you is not meaning full, please say so. And try to be as human as possible. \
                    If some one says Hi or something else (greetings) greet accordingly. \
                    
                    MOST IMPORTANTLY: PLEASE DON'T ADD BOLD, ITALIC OR UNDERLINE IN YOUR RESPONSE \
                        
                    FOR PROCEDURAL ANSWER, PLEASE ANSWER IN STEPS:
                <context>
                {context}
                </context>
                {chat_history}
                Question: {input}"""
                    )
        return prompt

    def prepare_the_retrieval_chain(self):
        prompt = self.prepare_the_prompt()
        chain = self.prepare_chain_llm_output_parser()
        vector_store = VectorRetriever(open_api_embedding_key_=self.open_api_key, file_path=self.file_path)
        retriever_chain = create_history_aware_retriever(chain, vector_store.retriever, prompt)
        document_chain = create_stuff_documents_chain(chain, prompt)
        retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

        return retrieval_chain