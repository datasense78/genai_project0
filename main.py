from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ["OPENAI_API_KEY"])

# 2 Ways of Chatbot
#A) Customized Model

# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input="Tell me about India"
# )

# print(response.output_text)



#B) Use Standard Library-Langchain
#1. Take User Question

user_question=input("Enter Your Question: ")


#2. Convert to Prompt

from langchain.prompts import PromptTemplate

text="""You are a Career Coach in AI Field. Answer Best Advice to candidate. Dont give cliche answers
Below is user question: 

{question}

"""

prompt=PromptTemplate(
    input_variables=["question"],
    template=text
)

#3. Make LLM Call
# from langchain_openai import ChatOpenAI

# llm=ChatOpenAI(model="gpt-4o")

from langchain_groq import ChatGroq

llm=ChatGroq(model="deepseek-r1-distill-llama-70b")



#Create Chain

chain=prompt | llm


#4. Response

result=chain.invoke({"question":user_question})
print(result.content)

