from langchain.indexes import VectorstoreIndexCreator
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import FigmaFileLoader
import os
from dotenv import load_dotenv
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

from revisited_lessons.r_chatgpt_qa.figma_llm.prompts import system_prompt_template, human_prompt_template

figma_loader = FigmaFileLoader(
    os.environ.get('ACCESS_TOKEN'),
    os.environ.get('NODE_IDS'),
    os.environ.get('FILE_KEY'),
)

index = VectorstoreIndexCreator().from_loaders([figma_loader])
figma_doc_retriever = index.vectorstore.as_retriever()


gpt_4 = ChatOpenAI(temperature=.03, model_name='gpt-3.5-turbo', request_timeout=120)

# Define a function to generate code based on the input
def generate_code(input):
    # Get relevant nodes from the Figma document retriever
    relevant_nodes = figma_doc_retriever.get_relevant_documents(input)

    # Create system and human message prompts
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)

    # Create the chat prompt using the system and human message prompts
    conversation = [system_message_prompt, human_message_prompt]
    chat_prompt = ChatPromptTemplate.from_messages(conversation)
    response = gpt_4(chat_prompt.format_prompt(
        context=relevant_nodes,
        text=input).to_messages())

    return response.conten
