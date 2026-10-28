from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

print("Connecting to local Ollama model...")
model = ChatOllama(model="llama3.2", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a witty chef who gives short, funny answers."),
    ("human", "What can I cook with just {ingredient_1} and {ingredient_2}?")
])

chain = prompt | model

print("Processing your request locally...")
response = chain.invoke({
    "ingredient_1": "eggs",
    "ingredient_2": "ramen noodles"
})

print("\nChef AI says:")
print(response.content)
