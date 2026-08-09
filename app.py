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
                        messages=[
                            {"role": "system", "content": f"You are an expert test builder fluent in {language}."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile",
                        temperature=0.8
                    )
                    st.success("🎉 Quiz Ready!")
                    st.markdown(response.choices[0].message.content, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ---------------------------------------------------------
# TAB 2: Deep Study Material
# ---------------------------------------------------------
with tab2:
    st.subheader("📚 Detailed Study Material & Guides")
    study_topic = st.text_input(
        "Enter topic to learn:", 
        placeholder="e.g., Digital SAT Grammar Rules, ASL Fingerspelling, Psychology Theories, Business Strategy"
    )
    
    if st.button("✨ Generate Study Notes", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the left sidebar.")
        elif not study_topic.strip():
            st.warning("⚠️ Please enter a topic first.")
        else:
            try:
                client = Groq(api_key=api_key)
                prompt = f"""
                You are a master tutor in {subject}.
                Provide comprehensive, highly structured study material for: '{study_topic}'.
                Level: {exam_level}.
                Language / System: {language}.
                
                Structure requirements:
                - Clear headings, key definitions, core concepts, bullet points, and real-world examples.
                - For SAT: Cover core strategies, rules, formulas, and common traps.
                - For Sign Languages: Describe handshapes, movement, locations, and facial expressions.
                - Include key takeaways and practical practice tips.
                """
                with st.spinner("Writing deep study notes..."):
                    response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": f"You are a helpful tutor fluent in {language}."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile"
                    )
                    st.success("🎉 Study Notes Ready!")
                    st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ---------------------------------------------------------
# TAB 3: Free-Response & Practice Scenarios
# ---------------------------------------------------------
with tab3:
    st.subheader("✏️ Practical Scenarios & Case Studies")
    q_topic = st.text_input("Enter topic:", placeholder="e.g., Business Marketing Strategy, SAT Essay Analysis, Proofs")
    
    if st.button("📝 Generate Exercises", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the left sidebar.")
        elif not q_topic.strip():
            st.warning("⚠️ Please enter a topic first.")
        else:
            try:
                client = Groq(api_key=api_key)
                prompt = f"""
                Create 3 practice scenarios, passage analysis, or open questions for: '{q_topic}'.
                Subject: {subject} | Level: {exam_level} | System: {language}.
                
                Include a full model answer inside an expandable details block for each question.
                """
                with st.spinner("Creating practice exercises..."):
                    response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": f"You are an instructor fluent in {language}."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile"
                    )
                    st.success("🎉 Practice Exercises Ready!")
                    st.markdown(response.choices[0].message.content, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")
