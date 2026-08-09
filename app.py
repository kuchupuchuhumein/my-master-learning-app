import streamlit as st
from groq import Groq
import random

# Page Setup
st.set_page_config(
    page_title="Universal Mastery & AI Chatbot Hub", 
    page_icon="🎓", 
    layout="centered"
)

st.title("🎓 Universal Mastery & AI Chatbot Hub")
st.write("Study any topic, take 10-question MCQ practice quizzes, or chat directly with your AI tutor to solve any doubt!")

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Global Settings")
    api_key = st.text_input(
        "Enter your Groq API Key:", 
        type="password", 
        help="Get your free key from console.groq.com"
    )
    
    st.markdown("---")
    
    # Language Options
    language = st.selectbox(
        "🌐 Output Language / System:",
        [
            "English",
            "American Sign Language (ASL - Handshape, Motion & Gloss)",
            "British Sign Language (BSL - Handshape, Motion & Gloss)",
            "Indian Sign Language (ISL - Handshape, Motion & Gloss)",
            "Spanish", "French", "German", "Hindi", "Mandarin Chinese",
            "Arabic", "Portuguese", "Russian", "Japanese", "Korean", 
            "Italian", "Turkish", "Urdu", "Bengali", "Vietnamese", "Dutch"
        ]
    )
    
    # Target Rigor / Level
    exam_level = st.selectbox(
        "🎯 Rigor / Exam Level:",
        [
            "Digital SAT - Reading & Writing",
            "Digital SAT - Mathematics",
            "Simple & Clear (Explain Like I'm 5)",
            "Basic / Beginner",
            "Intermediate",
            "Advanced / University Level",
            "Business Professional / Corporate",
            "IOQM / RMO / INMO (Math Olympiads)",
            "JEE Advanced (Physics, Chemistry, Math)",
            "JEE Main",
            "International Science Olympiads (IPhO, IChO, IBO)",
            "NEET (Medical Entrance)",
            "Standard High School (Grades 9-12)"
        ]
    )
    
    # Subject Selector
    subject = st.selectbox(
        "📚 Select Subject Area:",
        [
            "Digital SAT Test Prep (Reading, Writing, Math)",
            "Sign Language, Gestures & Visual Linguistics",
            "Human Psychology & Cognitive Science",
            "Business, Finance & Entrepreneurship",
            "Mathematics (Algebra, Geometry, Calculus, SAT)",
            "Physics (Mechanics, Electromagnetism, Quantum)",
            "Chemistry (Organic, Inorganic, Physical)",
            "Biology & Neuroscience",
            "Computer Science & Programming",
            "History & Social Sciences",
            "Literature & Humanities",
            "General / Any Subject"
        ]
    )

# App Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "💬 Ask AI Tutor & Doubts", 
    "🎯 10-Question MCQ Quiz", 
    "📖 Deep Study Material", 
    "✏️ Open Practice & Case Studies"
])

# ---------------------------------------------------------
# TAB 1: Interactive Chatbot for Doubts & Questions
# ---------------------------------------------------------
with tab1:
    st.subheader("💬 Interactive AI Tutor (Ask Any Doubt)")
    st.write("Type any question, doubt, or problem below to get instant step-by-step guidance.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User chat input
    user_query = st.chat_input("Ask a doubt, request a proof, or type anything...")
    if user_query:
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the left sidebar to start chatting.")
        else:
            # Display user message (FIXED LINE BELOW)
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.markdown(user_query)

            # Generate AI response
            try:
                client = Groq(api_key=api_key)
                
                system_prompt = f"""
                You are a patient, brilliant
