import streamlit as st
from groq import Groq
import random

# Page Setup
st.set_page_config(
    page_title="Universal Mastery & SAT Prep Hub", 
    page_icon="🎓", 
    layout="centered"
)

st.title("🎓 Universal Mastery & SAT Learning Hub")
st.write("Master any subject or language, prep for Digital SAT/Olympiads, and generate non-repeating 10-question MCQ quizzes!")

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Global Settings")
    api_key = st.text_input(
        "Enter your Groq API Key:", 
        type="password", 
        help="Get your free key from console.groq.com"
    )
    
    st.markdown("---")
    
    # Extensive Spoken & Sign Languages List
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
    
    # Target Rigor / Level (Includes Digital SAT)
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
    
    # Subjects
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
tab1, tab2, tab3 = st.tabs(["🎯 10-Question MCQ Quiz", "📖 Deep Study Material", "✏️ Open Practice & Case Studies"])

# ---------------------------------------------------------
# TAB 1: 10-Question Non-Repeating MCQ Quiz
# ---------------------------------------------------------
with tab1:
    st.subheader("🎯 Generate 10-Question Practice Quiz")
    mcq_topic = st.text_input(
        "Enter quiz topic:", 
        placeholder="e.g., Digital SAT Sentence Equivalence, ASL Syntax, Cognitive Dissonance, Financial Accounting"
    )
    num_mcqs = st.slider("Number of Questions:", min_value=1, max_value=15, value=10)
    
    if st.button("🚀 Generate 10 MCQ Questions", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the left sidebar.")
        elif not mcq_topic.strip():
            st.warning("⚠️ Please enter a topic first.")
        else:
            try:
                client = Groq(api_key=api_key)
                
                # Generate a random seed to enforce non-repeating questions on every click
                random_seed = random.randint(1000, 999999)
                
                prompt = f"""
                You are an expert exam creator for {subject} at the '{exam_level}' level.
                Topic: '{mcq_topic}'.
                Unique Generation Seed: {random_seed} (Ensure all questions are fresh and unique!).
                
                Requirements:
                - Create EXACTLY {num_mcqs} multiple-choice questions.
                - Output strictly using: {language}.
                - If testing SAT: Match the exact style, difficulty, and question format of College Board Digital SAT questions.
                - If testing Sign Language (ASL/BSL/ISL): Detail handshapes, movement, facial expressions, and visual gloss.
                - Provide 4 options (A, B, C, D) per question.
                - Underneath each question, provide an expandable HTML details block containing the correct answer and a step-by-step solution.

                Format required:
                ### Question [Number]
                [Question text]
                - **A)** [Option A]
                - **B)** [Option B]
                - **C)** [Option C]
                - **D)** [Option D]

                <details>
                <summary><b>Click to show solution</b></summary>

                **Correct Answer:** [Correct Option]  
                **Detailed Solution:** [Clear step-by-step reasoning]
                </details>

                ---
                """
                with st.spinner(f"Generating {num_mcqs} unique practice questions..."):
                    response = client.chat.completions.create(
