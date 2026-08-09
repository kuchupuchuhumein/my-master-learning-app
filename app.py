import streamlit as st
from groq import Groq

# Page Setup
st.set_page_config(
    page_title="Universal Mastery & Exam Hub", 
    page_icon="🧠", 
    layout="centered"
)

st.title("🧠 Universal Mastery & Learning Hub")
st.write("Master anything: Sign languages (ASL), Psychology, Business, Olympiads, JEE, and more!")

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Global & Exam Settings")
    api_key = st.text_input(
        "Enter your Groq API Key:", 
        type="password", 
        help="Get your free key from console.groq.com"
    )
    
    st.markdown("---")
    
    # Language Selector (Spoken & Sign Languages)
    language = st.selectbox(
        "🌐 Output Language / System:",
        [
            "English",
            "American Sign Language (ASL - Visual/Gloss Description)",
            "British Sign Language (BSL - Gloss Description)",
            "Indian Sign Language (ISL - Gloss Description)",
            "Hindi", "Spanish", "French", "German", 
            "Mandarin Chinese", "Arabic", "Portuguese", "Russian", 
            "Japanese", "Korean", "Italian"
        ]
    )
    
    # Target Rigor / Level
    exam_level = st.selectbox(
        "🎯 Rigor / Level:",
        [
            "Beginner / Introductory",
            "Intermediate",
            "Advanced / University Level",
            "Business Professional / Corporate",
            "IOQM / RMO / INMO (Math Olympiads)",
            "JEE Advanced (Physics, Chemistry, Math)",
            "JEE Main",
            "International Science Olympiads (IPhO, IChO, IBO)",
            "NEET (Medical Entrance)",
            "AP / IB Higher Level (HL)",
            "Standard High School (Grades 9-12)"
        ]
    )
    
    # Expanded Subject Selector
    subject = st.selectbox(
        "📚 Select Subject Area:",
        [
            "Psychology & Cognitive Science (Behavioral, Clinical, Neuropsychology)",
            "Business, Finance & Entrepreneurship (Marketing, Management, Economics)",
            "Sign Language & Linguistics (ASL, Fingerspelling, Grammar)",
            "Mathematics (Algebra, Combinatorics, Geometry, Number Theory, Calculus)",
            "Physics (Mechanics, Electromagnetism, Quantum, Optics, Thermodynamics)",
            "Chemistry (Organic, Inorganic, Physical)",
            "Biology & Neuroscience",
            "Computer Science & Competitive Programming",
            "History & World Events",
            "Literature & Language Arts",
            "General / Any Subject"
        ]
    )

# App Tabs
tab1, tab2, tab3 = st.tabs(["📖 Comprehensive Notes", "🎯 MCQ & Quiz Hub", "✏️ Open/Subjective Practice"])

# ---------------------------------------------------------
# TAB 1: Study Material & Guides
# ---------------------------------------------------------
with tab1:
    st.subheader("📚 In-Depth Concept Masterclass")
    study_topic = st.text_input(
        "Enter topic, sign, or concept:", 
        placeholder="e.g., ASL Alphabet/Syntax, Cognitive Dissonance, Swot Analysis, Rotational Dynamics"
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
                You are a world-class instructor in {subject}.
                Provide an in-depth, clear explanation for: '{study_topic}'.
                Selected Level/Rigor: {exam_level}.
                Language/Format Requirement: Output strictly in {language}.
                
                Note for Sign Languages (e.g., ASL/BSL): Describe handshapes, facial expressions, palm orientations, movement, and visual gloss notation step-by-step!
                
                Format requirements:
                - Clear definitions, core theories, equations, or visual sign instructions where applicable.
                - Real-world case studies, psychological studies, or business applications.
                - Step-by-step worked example or practical breakdown.
                """
                with st.spinner("Generating detailed notes..."):
                    response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": f"You are an expert tutor fluent in {language}."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile"
                    )
                    st.success("🎉 Notes Ready!")
                    st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ---------------------------------------------------------
# TAB 2: Multiple Choice Questions (MCQs)
# ---------------------------------------------------------
with tab2:
    st.subheader("🎯 Practice MCQs & Knowledge Checks")
    mcq_topic = st.text_input("Enter quiz topic:", placeholder="e.g., ASL Grammar Rules, Pavlovian Conditioning, Balance Sheets, JEE Integration")
    num_mcqs = st.slider("Number of Questions:", min_value=1, max_value=10, value=5)
    
    if st.button("🚀 Generate Quiz Questions", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the left sidebar.")
        elif not mcq_topic.strip():
            st.warning("⚠️ Please enter a topic first.")
        else:
            try:
                client = Groq(api_key=api_key)
                prompt = f"""
                You are an exam writer in {subject} at the {exam_level} level.
                Topic: '{mcq_topic}'.
                
                Requirements:
                - Create {num_mcqs} challenging multiple-choice questions matching the style of {subject} / {exam_level}.
                - Language/Format: Write strictly in {language}.
                - Provide 4 distinct options (A, B, C, D) for each question.
                - Include clear explanations in the expandable answer box.

                Format:
                ### Question [Number]
                [Question text]
                - **A)** [Option A]
                - **B)** [Option B]
                - **C)** [Option C]
                - **D)** [Option D]

                <details>
                <summary><b>Reveal Correct Answer & Explanation</b></summary>

                **Correct Answer:** [Correct Option]  
                **Detailed Explanation:** [Complete explanation / reasoning]
                </details>

                ---
                """
                with st.spinner("Generating questions..."):
                    response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": f"You are an expert quiz designer fluent in {language}."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile"
                    )
                    st.success("🎉 Quiz Ready!")
                    st.markdown(response.choices[0].message.content, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# ---------------------------------------------------------
# TAB 3: Subjective, Proofs & Case Studies
# ---------------------------------------------------------
with tab3:
    st.subheader("✏️ Free-Response, Case Studies & Proofs")
    q_topic = st.text_input("Enter topic for open-ended practice:", placeholder="e.g., Business Strategy Case Study, Psychological Diagnosis, ASL Sentence Translation")
    
    if st.button("📝 Generate Practice Scenarios", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the left sidebar.")
        elif not q_topic.strip():
            st.warning("⚠️ Please enter a topic first.")
        else:
            try:
                client = Groq(api_key=api_key)
                prompt = f"""
                You are an expert evaluator in {subject} at the {exam_level} level.
                Generate 3 practice scenarios/questions (e.g., Business Case Study, Psychological Analysis, Proofs, or Translation) for: '{q_topic}'.
                Language/Format: Output strictly in {language}.
                
                Provide a complete model answer/solution inside an expandable details element.
                
                Format:
                ### Problem / Scenario [Number]
                [Problem Description / Scenario Text]

                <details>
                <summary><b>View Model Answer / Solution Analysis</b></summary>

                **Model Solution:** [Comprehensive answer, breakdown, or proof]
                </details>

                ---
                """
                with st.spinner("Generating practice scenarios..."):
                    response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": f"You are an expert evaluator fluent in {language}."},
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.3-70b-versatile"
                    )
                    st.success("🎉 Practice Scenarios Ready!")
                    st.markdown(response.choices[0].message.content, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")
