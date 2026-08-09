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
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.markdown(user_query)

            try:
                client = Groq(api_key=api_key)
                
                system_prompt = (
                    f"You are a patient, brilliant educational chatbot expert in {subject} at the {exam_level} level. "
                    f"Language/System to respond in: {language}. "
                    f"Provide clear, encouraging, step-by-step explanations for any doubt, concept, or problem the user presents."
                )
                
                conversation = [{"role": "system", "content": system_prompt}] + [
                    {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
                ]

                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = client.chat.completions.create(
                            messages=conversation,
                            model="llama-3.3-70b-versatile"
                        )
                        bot_reply = response.choices[0].message.content
                        st.markdown(bot_reply)

                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ---------------------------------------------------------
# TAB 2: 10-Question Non-Repeating MCQ Quiz
# ---------------------------------------------------------
with tab2:
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
                random_seed = random.randint(1000, 999999)
                
                prompt = (
                    f"You are an expert exam creator for {subject} at the '{exam_level}' level. "
                    f"Topic: '{mcq_topic}'. "
                    f"Unique Generation Seed: {random_seed}. "
                    f"Requirements: Create EXACTLY {num_mcqs} multiple-choice questions. "
                    f"Output strictly using: {language}. "
                    f"Provide 4 options (A, B, C, D) per question. "
                    f"Format required for each question:\n\n"
                    f"### Question [Number]\n[Question text]\n"
                    f"- **A)** [Option A]\n- **B)** [Option B]\n- **C)** [Option C]\n- **D)** [Option D]\n\n"
                    f"<details>\n<summary><b>Click to show solution</b></summary>\n\n"
                    f"**Correct Answer:** [Correct Option]\n"
                    f"**Detailed Solution:** [Clear step-by-step reasoning]\n"
                    f"</details>\n\n---"
                )
                
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
# TAB 3: Deep Study Material
# ---------------------------------------------------------
with tab3:
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
                prompt = (
                    f"You are a master tutor in {subject}. "
                    f"Provide comprehensive, highly structured study material for: '{study_topic}'. "
                    f"Level: {exam_level}. Language / System: {language}. "
                    f"Structure with clear headings, key definitions, core concepts, bullet points, and real-world examples."
                )
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
# TAB 4: Free-Response & Practice Scenarios
# ---------------------------------------------------------
with tab4:
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
                prompt = (
                    f"Create 3 practice scenarios, passage analysis, or open questions for: '{q_topic}'. "
                    f"Subject: {subject} | Level: {exam_level} | System: {language}. "
                    f"Include a full model answer inside an expandable HTML details block for each question."
                )
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
