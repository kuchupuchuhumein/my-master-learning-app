import streamlit as st
from groq import Groq

# Page Setup
st.set_page_config(
    page_title="Universal Mastery & Olympiad Hub", 
    page_icon="🏆", 
    layout="centered"
)

st.title("🏆 Universal Mastery & Olympiad Hub")
st.write("Practice pre-loaded Olympiad questions or generate AI-powered custom quizzes!")

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Global & Exam Settings")
    api_key = st.text_input(
        "Enter your Groq API Key:", 
        type="password", 
        help="Get your free key from console.groq.com"
    )
    
    st.markdown("---")
    
    language = st.selectbox(
        "🌐 Output Language:",
        ["English", "Hindi", "Spanish", "French", "German", "Mandarin Chinese"]
    )
    
    exam_level = st.selectbox(
        "🎯 Rigor / Level:",
        [
            "IOQM / RMO / INMO (Math Olympiads)",
            "JEE Advanced (Physics, Chemistry, Math)",
            "JEE Main",
            "International Science Olympiads (IPhO, IChO, IBO)"
        ]
    )

# App Tabs
tab1, tab2, tab3 = st.tabs(["🔥 10 Practice Olympiad MCQs", "✨ AI Custom Generator", "📖 Concept Masterclass"])

# ---------------------------------------------------------
# TAB 1: Pre-loaded 10 Olympiad MCQs
# ---------------------------------------------------------
with tab1:
    st.subheader("🏆 10 Advanced Math Olympiad Questions")
    st.write("Test your knowledge on Number Theory, Combinatorics, Algebra, and Geometry.")

    olympiad_questions = [
        {
            "num": 1,
            "q": "Find the number of positive integers $n \\le 1000$ such that $2^n + 1$ is divisible by $n$.",
            "opts": ["A) 1", "B) 3", "C) 9", "D) 0"],
            "ans": "A) 1",
            "exp": "Only $n = 1$ satisfies the condition. For any $n > 1$, analyzing the smallest prime factor $p$ of $n$ leads to a contradiction via Fermat's Little Theorem."
        },
        {
            "num": 2,
            "q": "In a group of 6 people, every pair consists of either mutual friends or mutual strangers. What is the minimum guaranteed number of monochromatic triangles that must exist?",
            "opts": ["A) 1", "B) 2", "C) 3", "D) 4"],
            "ans": "B) 2",
            "exp": "By counting non-monochromatic triples at each vertex in $K_6$, the minimum number of monochromatic triangles guaranteed by Ramsey theory is strictly 2."
        },
        {
            "num": 3,
            "q": "Let $a, b, c$ be positive real numbers such that $abc = 1$. What is the minimum value of $\\frac{1}{a^3(b+c)} + \\frac{1}{b^3(a+c)} + \\frac{1}{c^3(a+b)}$?",
            "opts": ["A) 3/2", "B) 3", "C) 1/2", "D) 2"],
            "ans": "A) 3/2",
            "exp": "Substitute $x=1/a, y=1/b, z=1/c$. The expression transforms to $\\frac{x^2}{y+z} + \\frac{y^2}{x+z} + \\frac{z^2}{x+y} \\ge \\frac{x+y+z}{2} \\ge \\frac{3}{2}$ by Cauchy-Schwarz."
        },
        {
            "num": 4,
            "q": "In triangle $ABC$ with side lengths $AB = 6$, $BC = 8$, and $CA = 10$, let $H$ be the orthocenter and $O$ be the circumcenter. What is the distance $OH$?",
            "opts": ["A) 5", "B) 0", "C) √5", "D) 2√5"],
            "ans": "A) 5",
            "exp": "$ABC$ is a right triangle with right angle at $B$. The orthocenter $H$ lies at $B$, and the circumcenter $O$ is the midpoint of hypotenuse $AC$. Thus $OH = 10/2 = 5$."
        },
        {
            "num": 5,
            "q": "Find $f(5)$ if $f: \\mathbb{R} \\to \\mathbb{R}$ satisfies $f(x + y) = f(x) + f(y) + 2xy$ for all $x, y$, given that $f(1) = 2$.",
            "opts": ["A) 30", "B) 25", "C) 20", "D) 35"],
            "ans": "A) 30",
            "exp": "The equation reduces to $f(x) = x^2 + cx$. Using $f(1) = 1 + c = 2 \\implies c = 1$. So $f(x) = x^2 + x$, and $f(5) = 25 + 5 = 30$."
        },
        {
            "num": 6,
            "q": "Let $P(x)$ be an integer polynomial such that $P(1) = 3$ and $P(3) = 5$. Which of the following CANNOT be $P(7)$?",
            "opts": ["A) 12", "B) 9", "C) 21", "D) 33"],
            "ans": "A) 12",
            "exp": "For integer polynomials, $(a-b) \\mid (P(a)-P(b))$. Here $(7-1)=6$ must divide $P(7)-3$. Since $12-3=9$ is not divisible by 6, 12 is impossible."
        },
        {
            "num": 7,
            "q": "What is the remainder when $3^{100}$ is divided by 13?",
            "opts": ["A) 3", "B) 1", "C) 9", "D) 12"],
            "ans": "A) 3",
            "exp": "By Fermat's Little Theorem, $3^{12} \\equiv 1 \\pmod{13}$. Thus $3^{100} = (3^{12})^8 \\cdot 3^4 \\equiv 1^8 \\cdot 81 \\equiv 3 \\pmod{13}$."
        },
        {
            "num": 8,
            "q": "For positive real numbers $x, y, z$ satisfying $x + y + z = 3$, what is the maximum possible value of $\\sqrt{x} + \\sqrt{y} + \\sqrt{z}$?",
            "opts": ["A) 3", "B) 3√3", "C) 3√2", "D) 1"],
            "ans": "A) 3",
            "exp": "By Cauchy-Schwarz: $(\\sqrt{x} + \\sqrt{y} + \\sqrt{z})^2 \\le (1+1+1)(x+y+z) = 3 \\times 3 = 9$. Taking square roots gives 3."
        },
        {
            "num": 9,
            "q": "How many paths of length 6 exist from $(0,0)$ to $(3,3)$ moving right or up without crossing above $y = x$?",
            "opts": ["A) 5", "B) 14", "C) 20", "D) 42"],
            "ans": "A) 5",
            "exp": "The number of non-crossing lattice paths is given by the 3rd Catalan number $C_3 = \\frac{1}{4}\\binom{6}{3} = 5$."
        },
        {
            "num": 10,
            "q": "A regular hexagon has inradius $r$ and circumradius $R$. What is the ratio $r/R$?",
            "opts": ["A) √3 / 2", "B) 1/2", "C) √2 / 2", "D) 2/3"],
            "ans": "A) √3 / 2",
            "exp": "For side length $s$, circumradius $R = s$ and inradius $r = \\frac{\\sqrt{3}}{2}s$. Thus $r/R = \\frac{\\sqrt{3}}{2}$."
        }
    ]

    for item in olympiad_questions:
        st.markdown(f"### Question {item['num']}")
        st.markdown(item["q"])
        for opt in item["opts"]:
            st.write(opt)
        
        with st.expander("Show Solution & Explanation"):
            st.write(f"**Correct Answer:** {item['ans']}")
            st.write(f"**Explanation:** {item['exp']}")
        st.markdown("---")

# ---------------------------------------------------------
# TAB 2: AI Custom Quiz Generator
# ---------------------------------------------------------
with tab2:
    st.subheader("✨ Generate Custom AI Quizzes")
    topic = st.text_input("Enter topic:", placeholder="e.g., Organic Chemistry, Quantum Physics, Combinatorics")
    num_q = st.slider("Number of questions:", 1, 10, 5)
    
    if st.button("🚀 Generate Quiz", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the sidebar.")
        elif not topic.strip():
            st.warning("⚠️ Enter a topic first.")
        else:
            try:
                client = Groq(api_key=api_key)
                prompt = f"Create a {num_q}-question MCQ quiz on '{topic}' at {exam_level} level in {language}. Use expandable solution boxes."
                
                with st.spinner("Generating quiz..."):
                    res = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.3-70b-versatile"
                    )
                    st.markdown(res.choices[0].message.content, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

# ---------------------------------------------------------
# TAB 3: Study Notes
# ---------------------------------------------------------
with tab3:
    st.subheader("📖 Concept Explanations")
    concept = st.text_input("Enter concept to study:", placeholder="e.g., Ramsey Theory, Cauchy-Schwarz Inequality")
    if st.button("✨ Generate Notes", type="primary"):
        if not api_key:
            st.error("⚠️ Please enter your Groq API Key in the sidebar.")
        elif not concept.strip():
            st.warning("⚠️ Enter a concept first.")
        else:
            try:
                client = Groq(api_key=api_key)
                prompt = f"Provide detailed study notes on '{concept}' for {exam_level} in {language}."
                with st.spinner("Writing notes..."):
                    res = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.3-70b-versatile"
                    )
                    st.markdown(res.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
