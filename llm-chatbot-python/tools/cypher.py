import streamlit as st
from llm import llm
from graph import graph
from langchain_neo4j import GraphCypherQAChain
from langchain.prompts import PromptTemplate

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about tweets.
Convert the user's question based on the schema.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Do not return entire nodes or embedding properties.

Example Cypher Statements:

1. To get followers of a user
```
MATCH (f:User)-[r:FOLLOWS]->(u:User {{name: "User Name"}})
RETURN f.name
```

2. To find who is the author of a tweet:
```
MATCH (u:User)-[r:POSTS]->(t:Tweet {{id: tweetId}})
RETURN u.name
```

3. To find tweets using a hashtag:
```
MATCH (t:Tweet)-[r:TAGS]->(h:Hashtag {{name: "Hashtag"}})
RETURN t.text
```

Schema:
{schema}

Question:
{question}
"""

cypher_prompt = PromptTemplate.from_template(CYPHER_GENERATION_TEMPLATE)

# Create the Cypher QA chain
cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    verbose=True,
    cypher_prompt=cypher_prompt,
    allow_dangerous_requests=True
)
