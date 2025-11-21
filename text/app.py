import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from gtts import gTTS
from streamlit_extras.stylable_container import stylable_container
import base64

# Load model from Hugging Face Hub
MODEL_NAME = "babbilibhavani/nllb-translator"  # <-- Replace with your Hugging Face repo

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

# Language codes
LANG_CODES = {
    "Hindi": "hin_Deva",
    "Bengali": "ben_Beng",
    "Marathi": "mar_Deva",
    "Telugu": "tel_Telu",
    "Tamil": "tam_Taml",
    "Gujarati": "guj_Gujr",
    "Urdu": "urd_Arab",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Punjabi": "pan_Guru",
}

# gTTS language map
gtts_lang_map = {
    "Hindi": "hi",
    "Bengali": "bn",
    "Marathi": "mr",
    "Telugu": "te",
    "Tamil": "ta",
    "Gujarati": "gu",
    "Urdu": "ur",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
}

st.title("Language Translator")

text_input = st.text_area("Enter text")

col1, col2 = st.columns(2)
source_lang = col1.selectbox("Source", LANG_CODES.keys())
target_lang = col2.selectbox("Target", LANG_CODES.keys())

if st.button("Translate"):
    tokenizer.src_lang = LANG_CODES[source_lang]

    inputs = tokenizer(text_input, return_tensors="pt")
    output_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[LANG_CODES[target_lang]],
    )
    translated_text = tokenizer.batch_decode(output_tokens, skip_special_tokens=True)[0]

    st.session_state["translated_text"] = translated_text

    # Generate audio
    tts = gTTS(translated_text, lang=gtts_lang_map[target_lang])
    audio_path = "translated_audio.mp3"
    tts.save(audio_path)

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    st.session_state["audio_base64"] = base64.b64encode(audio_bytes).decode("utf-8")

if "translated_text" in st.session_state:
    st.text_area("Translated Text", st.session_state["translated_text"], height=150)

    # PLAY BUTTON WITHOUT REFRESH
    with stylable_container(
        key="play_button",
        css_styles="""
        button {
            background-color: #ffffff00;
            border: none;
            font-size: 40px;
            cursor: pointer;
        }
    """,
    ):
        if st.button("🔊Listen"):
            audio_html = f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{st.session_state["audio_base64"]}">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
