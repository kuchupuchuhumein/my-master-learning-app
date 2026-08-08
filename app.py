import streamlit as st
from groq import Groq

# 1. Page Setup
st.set_page_config(
    page_title="✨ Master Learning & AIR 1 Portal ✨", 
    page_icon="🎓", 
    layout="wide"
)

# 2. Cute & Modern CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }
    
    .main-title {
        font-family: 'Comic Sans MS', 'Chalkboard SE', cursive, sans-serif;
        color: #ff6b6b;
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .sub-title {
        text-align: center;
        color: #576574;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #ff7675, #6c5ce7) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 25px !important;
        padding: 10px 25px !important;
        border: none !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header Title
st.markdown("<h1 class='main-title'>🎓 ✨ Master Learning & Rank 1 Portal ✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Learn <b>any language or subject</b> deeply step-by-step & practice unlimited non-repeating questions! 🚀</p>", unsafe_allow_html=True)

# 4. Sidebar Controls
st.sidebar.markdown("## ⚙️ **Control Panel**")
api_key = st.sidebar.text_input("🔑 Enter Groq API Key:", type="password")

category = st.sidebar.selectbox(
    "📚 Choose Learning Domain:",
    [
        "Physics",
        "Chemistry",
        "Mathematics",
        "Psychology",
        "Business Studies & Economics",
        "Sign Language (ISL / ASL)",
        "Language Learning (Any World Language)",
        "UPSC / History / Polity",
        "Custom Subject"
    ]
)

level = st.sidebar.radio(
    "🎯 Select Difficulty Level:",
    ["🌱 Basics (Absolute Beginner)", "📈 Intermediate Level", "🏆 AIR 1 / Master Level"]
)

# Track session state for infinite non-repeating question generations
if "generated_count" not in st.session_state:
    st.session_state["generated_count"] = 0

# 5. Main Navigation Tabs
tab1, tab2 = st.tabs(["📚 Study & Practice Material", "💬 Instant Doubt Solver Chat"])

# --- TAB 1: UNLIMITED PRACTICE & DEEP STUDY MATERIAL ---
with tab1:
    st.markdown("### 🛠️ **Customization**")

    col1, col2 = st.columns(2)

    with col1:
        feature = st.radio(
            "✨ Select What You Want to Generate:",
            [
                "📚 Deep & Complete Topic Explanation",
                "📄 Formula / Grammar Rules / Cheat Sheet",
                "🎯 10 Unique Practice Questions with Solutions"
            ]
        )

    with col2:
        if category == "Language Learning (Any World Language)":
            target_lang = st.text_input("🌐 Language to Learn:", "Japanese")
            topic = st.text_input("📌 Specific Topic / Grammar Area:", "Greetings & Basic Sentence Structure")
            subject_str = f"Language: {target_lang}"
        else:
            if category == "Custom Subject":
                subject_str = st.text_input("📖 Custom Subject Name:", "Computer Science")
            else:
                subject_str = category
            topic = st.text_input("📌 Specific Topic / Chapter:", "General Fundamentals")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✨ Generate Material / Questions ✨", use_container_width=True):
        if not api_key:
            st.error("⚠️ Please enter your Groq API key in the left sidebar to start!")
        else:
            st.session_state["generated_count"] += 1
            client = Groq(api_key=api_key)

            with st.spinner("🌟 Generating deep study material for you..."):
                try:
                    if "10 Unique Practice Questions" in feature:
                        prompt = f"""
                        You are an elite professor and paper-setter for '{subject_str}' for topic '{topic}'.
                        Target level: '{level}'.
                        Unique Attempt Seed (ensures questions NEVER repeat across requests): {st.session_state['generated_count']}.

                        Generate **10 BRAND NEW, UNIQUE, non-repetitive practice questions** tailored to '{level}'.
                        Include options A, B, C, D for multiple-choice questions.

                        Format clearly as:
                        ### 🎯 10 Practice Questions ({level} - Set #{st.session_state['generated_count']})

                        Format each question like:
                        **Question X:** [Write question here]
                        ---

                        Insert this EXACT divider line:
                        |||SPLIT|||

                        ### 🧠 Step-by-Step Answer Keys & Comprehensive Solutions
                        Provide exhaustive, step-by-step explanations and answers for all 10 questions!
                        """
                    elif "Formula / Grammar Rules" in feature:
                        prompt = f"""
                        Provide a complete, deep **Cheat Sheet (Formulas, Vocabulary, or Key Rules)** for '{subject_str}', topic '{topic}' at level '{level}'.
                        Include:
                        1. Comprehensive Formulas, Vocabulary Lists, or Key Rules
                        2. Clear Definitions of Variables / Technical Terms
                        3. Memory Tricks, Shortcuts & Exam Hacks
                        4. Common Trap Mistakes to Avoid
                        """
                    else:
                        prompt = f"""
                        You are an expert professor teaching '{subject_str}' for the topic '{topic}'.
                        The student is at '{level}' level and requires an EXTREMELY DETAILED, IN-DEPTH, AND COMPREHENSIVE explanation.

                        Explain everything deeply step-by-step using this exact structure:

                        ### 1. 🌟 Fundamental Core Concept & Big Picture
                        Explain the core intuition in depth using simple analogies, conceptual models, and mental frameworks.

                        ### 2. 🔬 Deep-Dive Technical & Theoretical Breakdown
                        Break down every sub-concept, mathematical foundation, mechanism, or grammatical rule step-by-step without skipping steps.

                        ### 3. 📐 Formulas, Derivations & Notations (if applicable)
                        List all relevant formulas, definitions, and step-by-step logic.

                        ### 4. 💡 Comprehensive Worked Examples
                        Provide 2 concrete, fully-solved, step-by-step examples demonstrating how this concept is applied.

                        ### 5. ⚠️ Traps, Common Misconceptions & Ranker Insights
                        Detail common student errors, edge cases, and high-yield strategy tips.
                        """

                    response = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.3-70b-versatile",
                        max_completion_tokens=4000
                    )

                    raw_content = response.choices[0].message.content

                    if "|||SPLIT|||" in raw_content:
                        q_part, sol_part = raw_content.split("|||SPLIT|||")
                        st.session_state["content_main"] = q_part
                        st.session_state["content_sub"] = sol_part
                    else:
                        st.session_state["content_main"] = raw_content
                        st.session_state["content_sub"] = None

                except Exception as e:
                    st.error(f"❌ Error fetching data: {e}")

    # Render Study Content
    if "content_main" in st.session_state:
        st.markdown("---")
        st.markdown(st.session_state["content_main"])

    if st.session_state.get("content_sub"):
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💡 Show Answer Key & Detailed Solutions"):
            st.success(st.session_state["content_sub"])


# --- TAB 2: INSTANT DOUBT SOLVER CHATBOT ---
with tab2:
    st.markdown("### 💬 **Ask Your Doubts Anytime!**")
    st.write(f"Currently helping you with **{category}** ({level})")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f"Hi there! 👋 I'm your private tutor. Ask me any doubt about **{category}** or any other topic, and I'll explain it in simple, step-by-step detail!"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_doubt := st.chat_input("Type your question or doubt here..."):
        if not api_key:
            st.error("⚠️ Please enter your Groq API key in the left sidebar to chat!")
        else:
            st.chat_message("user").markdown(user_doubt)
            st.session_state.messages.append({"role": "user", "content": user_doubt})

            system_instruction = {
                "role": "system",
                "content": f"You are a friendly, genius AI professor helping a student learn {category} at {level} level. Explain doubts deeply step-by-step with clear examples."
            }

            full_messages = [system_instruction] + [
                {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
            ]

            client = Groq(api_key=api_key)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing doubt..."):
                    try:
                        response = client.chat.completions.create(
                            messages=full_messages,
                            model="llama-3.3-70b-versatile",
                            max_completion_tokens=3000
                        )
                        reply = response.choices[0].message.content
                        st.markdown(reply)
                        st.session_state.messages.append({"role": "assistant", "content": reply})
                    except Exception as e:
                        st.error(f"Error: {e}")
