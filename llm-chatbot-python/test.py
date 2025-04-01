# from llm import llm
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# chat_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a movie expert providing information about movies."),
#         ("human", "{input}"),
#     ]
# )

# movie_chat = chat_prompt | llm# | StrOutputParser()

# print(movie_chat.invoke({"input": "Who is the CEO of neo4j?"}))

from langchain_ollama import ChatOllama

# template="You are a helpful assistant who can give {category} for given input. Only give {category} no other text, use as little words as possible while responding, better give reply only in one word."
# system_message_prompt=SystemMessagePromptTemplate.from_template(template)
# human_template="{text}"
# human_message_prompt=HumanMessagePromptTemplate.from_template(human_template)
# chat_prompt=ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])

chat = ChatOllama(model="tinyllama",temperature=0,)

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie expert providing information about movies."),
        ("human", "{input}"),
    ]
)

movie_chat = chat_prompt | chat

print(movie_chat.invoke({"input": "Who is the CEO of neo4j?"}))

# resp = chat.invoke(chat_prompt.format_prompt(category="antonyms", text="Happy").to_messages())
# print(resp.content)
