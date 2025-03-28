import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# Initialize Groq LLM
def init_llm():
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-70b-8192",
        temperature=0.7
    )

# Load content from text file
def load_content():
    if not os.path.exists("unisole.txt"):
        st.error("unisole.txt file not found! Please ensure it exists in the same directory.")
        return "No content available."
    
    with open("unisole.txt", "r", encoding="utf-8") as f:
        return f.read()

def main():
    st.set_page_config(
        page_title="YL-360 Initiative Assistant",
        page_icon="🚀",
        layout="centered"
    )
    
    st.title("YL-360 Initiative Assistant")
    st.markdown("Welcome to the YL-360 Initiative by Unisole! How can I help you today?")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "llm" not in st.session_state:
        st.session_state.llm = init_llm()
    
    if "content" not in st.session_state:
        with st.spinner("Loading YL-360 information..."):
            st.session_state.content = load_content()
    
    # Display chat history
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="🚀"):
                st.markdown(message.content)
    
    # Get user input
    user_input = st.chat_input("Ask about YL-360 Initiative, students, or Unisole...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Get AI response
        with st.chat_message("assistant", avatar="🚀"):
            message_placeholder = st.empty()
            
            try:
                # Create prompt with context
                system_prompt = f"""
                You are the official AI assistant for the YL-360 Initiative by Unisole. Your name is YL-360 Assistant.
                
                Here is information about YL-360, Unisole, and the program:
                
                {st.session_state.content}
                
                Use this information to answer questions. Be warm, welcoming, and enthusiastic.
                If you don't know something, suggest they contact Ajay Mokta.
                
                Previous conversation:
                {' '.join([f"Human: {m.content}" if isinstance(m, HumanMessage) else f"Assistant: {m.content}" for m in st.session_state.messages[-6:]])}
                """
                
                prompt = ChatPromptTemplate.from_messages([
                    ("system", system_prompt),
                    ("human", user_input)
                ])
                
                chain = prompt | st.session_state.llm
                response = chain.invoke({})
                
                message_placeholder.markdown(response.content)
                # Add AI response to chat history
                st.session_state.messages.append(AIMessage(content=response.content))
                
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                message_placeholder.markdown(error_msg)
                st.session_state.messages.append(AIMessage(content=error_msg))

if __name__ == "__main__":
    main()