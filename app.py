from pathlib import Path
import joblib
import streamlit as st

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon=str(Path(__file__).parent / "logo.png"),
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at top left, #302065 0%, transparent 45%),
        radial-gradient(ellipse at bottom right, #063b60 0%, transparent 45%),
        #080e25;
    color: #f3f5ff;
}
[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    max-width: 950px;
    padding-top: 3rem;
    padding-bottom: 2rem;
}
.brand {
    font-size: 22px;
    font-weight: 700;
    color: #85dbff;
    margin-bottom: 32px;
}
.hero {
    text-align: center;
    margin-bottom: 32px;
}
.hero h1 {
    color: #f5f6ff;
    font-size: clamp(32px, 5vw, 52px);
    font-weight: 800;
    line-height: 1.15;
}
.gradient-text {
    background: linear-gradient(90deg, #b65cff, #23d5f5);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    color: #b4c1e5;
    font-size: 17px;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(23, 33, 61, 0.88);
    border: 1px solid #9868ed !important;
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.22);
}
[data-testid="stTextArea"] textarea {
    background: #101b34 !important;
    color: #f3f5ff !important;
    caret-color: #29d6f5;
    border: 1px solid #7183b5 !important;
    border-radius: 12px;
    font-size: 16px;
}
[data-testid="stTextArea"] textarea::placeholder {
    color: #a1afd0 !important;
}
[data-testid="stTextArea"] label,
[data-testid="stTextArea"] label p {
    color: #e3eaff !important;
}
.stButton > button {
    background: #15213d;
    color: #dce7ff;
    border: 1px solid #6686b8;
    border-radius: 12px;
    min-height: 46px;
    font-weight: 600;
}
.stButton > button:hover {
    border-color: #32d9f6;
    color: #63e3ff;
    background: #1c2a49;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #9229f4, #087ffc);
    border: none;
    color: white;
    min-height: 52px;
}
.stButton > button[kind="primary"]:hover {
    filter: brightness(1.12);
    color: white;
}
.card-heading {
    color: #f3f5ff;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 4px;
}
.card-description {
    color: #b4c1e5;
    margin-bottom: 18px;
}
.result {
    padding: 18px 20px;
    border-radius: 14px;
    margin-top: 20px;
}
.result h3 {
    margin: 0 0 6px;
    padding: 0;
    font-size: 22px;
    color: inherit;
}
.result p {
    margin: 0;
}
.result-spam {
    background: #351829;
    border: 1px solid #fb7185;
    color: #fecdd3;
}
.result-ham {
    background: #0d302e;
    border: 1px solid #2dd4bf;
    color: #99f6e4;
}
.features {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
    margin: 28px 0;
}
.feature {
    flex: 1;
    min-width: 180px;
    text-align: center;
    color: #e6ecff;
}
.feature-icon {
    font-size: 27px;
    margin-bottom: 8px;
}
.feature p {
    color: #aab9dc;
    font-size: 13px;
    margin-top: 5px;
}
.footer {
    border-top: 1px solid #293653;
    padding-top: 22px;
    text-align: center;
    color: #aab9dc;
    font-size: 13px;
}
.footer strong {
    color: #61d7ff;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    path = Path(__file__).parent / "spam_model.joblib"
    return joblib.load(path)


def clear_result():
    st.session_state.pop("prediction", None)


def set_message(text):
    st.session_state["message"] = text
    clear_result()


model = load_model()

if "message" not in st.session_state:
    st.session_state["message"] = ""

logo_column, title_column = st.columns([1, 8])

with logo_column:
    st.image(str(Path(__file__).parent / "logo.png"), width=70)

with title_column:
    st.markdown(
        '<div class="brand">SMS Spam Detector</div>',
        unsafe_allow_html=True
    )

st.markdown("""
<div class="hero">
    <h1>Check messages<br>
    <span class="gradient-text">Spot spam</span></h1>
    <p>A smarter way to spot spam</p>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("""
    <div class="card-heading">💬 Analyze a message</div>
    <div class="card-description">
        Paste your message below to get started.
    </div>
    """, unsafe_allow_html=True)

    st.text_area(
        "Your message",
        placeholder="Type or paste an SMS message here...",
        height=180,
        key="message",
        on_change=clear_result
    )

    example_normal, example_spam = st.columns(2)

    with example_normal:
        st.button(
            "💬 Try normal message",
            on_click=set_message,
            args=("Hey, are we meeting at the library tomorrow?",),
            use_container_width=True
        )

    with example_spam:
        st.button(
            "🎁 Try spam message",
            on_click=set_message,
            args=(
                "Congratulations! You won a FREE cash prize of £1000. "
                "Call now to claim your reward!",
            ),
            use_container_width=True
        )

    analyze_column, clear_column = st.columns([3, 1])

    with analyze_column:
        analyze = st.button(
            "🔍 Analyze Message",
            type="primary",
            use_container_width=True
        )

    with clear_column:
        st.button(
            "Clear",
            on_click=set_message,
            args=("",),
            use_container_width=True
        )

    if analyze:
        message = st.session_state["message"].strip()

        if not message:
            clear_result()
            st.warning("Please enter a message first.")
        else:
            st.session_state["prediction"] = model.predict([message])[0]

    prediction = st.session_state.get("prediction")

    if prediction == "spam":
        st.markdown("""
        <div class="result result-spam">
            <h3>⚠️ Prediction: Spam</h3>
            <p>The model identified patterns associated with spam.</p>
        </div>
        """, unsafe_allow_html=True)

    elif prediction == "ham":
        st.markdown("""
        <div class="result result-ham">
            <h3>✓ Prediction: Not Spam</h3>
            <p>The model classified this as a normal message.
            This does not guarantee it is safe.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="features">
    <div class="feature">
        <div class="feature-icon">📝</div>
        <strong>Text analysis</strong>
        <p>Examines word patterns</p>
    </div>
    <div class="feature">
        <div class="feature-icon">🧠</div>
        <strong>Machine learning</strong>
        <p>Powered by your trained model</p>
    </div>
    <div class="feature">
        <div class="feature-icon">⚡</div>
        <strong>Quick predictions</strong>
        <p>Check a message with one click</p>
    </div>
</div>
<div class="footer">
    <p>A learning project: predictions may be incorrect.</p>
    <p>Built by <strong>ASHOK ANDRA</strong></p>
</div>
""", unsafe_allow_html=True)