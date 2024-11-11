from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
from difflib import get_close_matches

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Predefined responses
predefined_responses = {
    "What does the eligibility verification agent (EVA) do?": 
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?": 
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?": 
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.": 
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?": 
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

# Prompt Template for LLM fallback
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question:{question}")
])

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit interface
st.title('LangChain AI Agent Demo')
input_text = st.text_input("Ask a question about Thoughtful AI:")

def get_predefined_response(question):
    # Attempt to find an exact match or close match in predefined responses
    response = predefined_responses.get(question)
    if not response:
        close_match = get_close_matches(question, predefined_responses.keys(), n=1, cutoff=0.6)
        if close_match:
            response = predefined_responses[close_match[0]]
    return response

# Check for predefined response or fallback to LLM with error handling
if input_text.strip():
    response = get_predefined_response(input_text)
    if response:
        st.write(response)
    else:
        try:
            st.write("AI Assistant Response:")
            st.write(chain.invoke({'question': input_text}))
        except Exception as e:
            st.error("I'm not trained for this type of question. Please try asking something else.")

else:
    st.write("Please enter a valid question.")
