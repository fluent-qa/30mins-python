from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_models import ChatOpenAI

from revisited_lessons.r_chatgpt_qa.figma_llm.prompts import prompt

chatgpt_chain = LLMChain(
    llm=ChatOpenAI(temperature=0, request_timeout=120),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)


# Function to generate a response using OpenAI's ChatCompletion API
def generate_response(prompt, html_content):
    completion = chatgpt_chain.predict(
        human_input=(
            "You are a senior developer. I want you to improve the following code with the following {prompt}: {html_content}. Only output new html/css code. Do not write additional text."
            "The code is html/css that was created by AI based on a Figma document."
        ).format(prompt=prompt, html_content=html_content)
    )
    return completion
