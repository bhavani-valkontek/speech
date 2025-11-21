# import streamlit as st
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from gtts import gTTS
# import os

# # ---------------------
# # Load NLLB-200 model
# # ---------------------
# MODEL_NAME = r"C:\Users\admin\Downloads\nlp\program\nllb_model_zip"

# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
#     model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
#     return tokenizer, model

# tokenizer, model = load_model()

# # ---------------------
# # Language mapping for NLLB-200
# # ---------------------
# LANG_CODES = {
#     "Hindi": "hin_Deva",
#     "Bengali": "ben_Beng",
#     "Marathi": "mar_Deva",
#     "Telugu": "tel_Telu",
#     "Tamil": "tam_Taml",
#     "Gujarati": "guj_Gujr",
#     "Urdu": "urd_Arab",
#     "Kannada": "kan_Knda",
#     "Odia": "ory_Orya",
#     "Malayalam": "mal_Mlym",
#     "Punjabi": "pan_Guru",
#     "Assamese": "asm_Beng",
#     "Maithili": "mai_Deva",
#     "Santali": "sat_Olck",
#     "Kashmiri": "kas_Arab",
#     "Nepali": "npi_Deva",
#     "Sindhi": "snd_Arab",
#     "Dogri": "doi_Deva",
#     "Konkani": "kok_Deva",
#     "Manipuri (Meitei)": "mni_Mtei",
#     "Bodo": "brx_Deva",
#     "Gondi": "gon_Deva",
# }

# # ---------------------
# # Streamlit UI
# # ---------------------
# st.title("🇮🇳 Indian Language Translator + Voice (NLLB + gTTS)")
# st.write("Translate between Indian languages and generate speech output.")

# # User Input
# text_input = st.text_area("Enter text:", height=150)

# col1, col2 = st.columns(2)
# with col1:
#     source_lang = st.selectbox("Source Language", LANG_CODES.keys())
# with col2:
#     target_lang = st.selectbox("Target Language", LANG_CODES.keys())

# if st.button("Translate"):
#     if not text_input.strip():
#         st.error("Please enter some text.")
#     else:
#         with st.spinner("Translating..."):
#             src = LANG_CODES[source_lang]
#             tgt = LANG_CODES[target_lang]

#             inputs = tokenizer(text_input, return_tensors="pt", src_lang=src)
#             output = model.generate(
#                 **inputs,
#                 forced_bos_token_id=tokenizer.lang_code_to_id[tgt],
#                 max_length=200
#             )
#             translated_text = tokenizer.decode(output[0], skip_special_tokens=True)

#         st.success("Translation completed!")
#         st.text_area("Translated Text:", translated_text, height=150)

#         # ---------------------
#         # Text-to-Speech (gTTS)
#         # ---------------------
#         with st.spinner("Generating audio..."):
#             tts = gTTS(translated_text, lang="hi")  # gTTS auto-detects most Indian languages
#             audio_path = "output.mp3"
#             tts.save(audio_path)

#         st.audio(audio_path)
#         st.download_button("Download Audio", data=open(audio_path, "rb"), file_name="translated_audio.mp3")

#         st.success("Audio ready!")


# import streamlit as st
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from gtts import gTTS
# import os

# # ---------------------
# # Load NLLB-200 model
# # ---------------------
# MODEL_NAME = r"C:\Users\admin\Downloads\nlp\program\nllb_model"

# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained(
#         MODEL_NAME,
#         use_fast=True,
#         trust_remote_code=True
#     )
#     model = AutoModelForSeq2SeqLM.from_pretrained(
#         MODEL_NAME,
#         trust_remote_code=True
#     )
#     return tokenizer, model

# tokenizer, model = load_model()

# # ---------------------
# # Language mapping for NLLB-200
# # ---------------------
# LANG_CODES = {
#     "Hindi": "hin_Deva",
#     "Bengali": "ben_Beng",
#     "Marathi": "mar_Deva",
#     "Telugu": "tel_Telu",
#     "Tamil": "tam_Taml",
#     "Gujarati": "guj_Gujr",
#     "Urdu": "urd_Arab",
#     "Kannada": "kan_Knda",
#     "Odia": "ory_Orya",
#     "Malayalam": "mal_Mlym",
#     "Punjabi": "pan_Guru",
#     "Assamese": "asm_Beng",
#     "Maithili": "mai_Deva",
#     "Santali": "sat_Olck",
#     "Kashmiri": "kas_Arab",
#     "Nepali": "npi_Deva",
#     "Sindhi": "snd_Arab",
#     "Dogri": "doi_Deva",
#     "Konkani": "kok_Deva",
#     "Manipuri (Meitei)": "mni_Mtei",
#     "Bodo": "brx_Deva",
#     "Gondi": "gon_Deva",
# }

# # ---------------------
# # Streamlit UI
# # ---------------------
# st.title(" Language Translator ")
# # st.write("Translate between Indian languages and generate speech output.")

# # User Input
# text_input = st.text_area("Enter text:", height=150)

# col1, col2 = st.columns(2)
# with col1:
#     source_lang = st.selectbox("Source Language", LANG_CODES.keys())
# with col2:
#     target_lang = st.selectbox("Target Language", LANG_CODES.keys())

# if st.button("Translate"):
#     if not text_input.strip():
#         st.error("Please enter some text.")
#     else:
#         with st.spinner("Translating..."):

#             src = LANG_CODES[source_lang]
#             tgt = LANG_CODES[target_lang]

#             # ---------------------
#             # Correct NLLB usage
#             # ---------------------
#             tokenizer.src_lang = src  # <-- FIXED

#             inputs = tokenizer(
#                 text_input,
#                 return_tensors="pt"
#             ).to(model.device)

#             # Generate translation
#             output_tokens = model.generate(
#                 **inputs,
#                 forced_bos_token_id=tokenizer.lang_code_to_id[tgt],
#                 max_length=200
#             )

#             translated_text = tokenizer.batch_decode(
#                 output_tokens,
#                 skip_special_tokens=True
#             )[0]

#         st.success("Translation completed!")
#         st.text_area("Translated Text:", translated_text, height=150)

#         # ---------------------
#         # Text-to-Speech (gTTS)
#         # ---------------------
#         with st.spinner("Generating audio..."):

#             # Basic language mapping
#             gtts_lang_map = {
#                 "Hindi": "hi",
#                 "Bengali": "bn",
#                 "Marathi": "mr",
#                 "Telugu": "te",
#                 "Tamil": "ta",
#                 "Gujarati": "gu",
#                 "Urdu": "ur",
#                 "Kannada": "kn",
#                 "Malayalam": "ml",
#                 "Punjabi": "pa"
#             }

#             gtts_lang = gtts_lang_map.get(target_lang, "hi")

#             audio_path = "translated_audio.mp3"
#             tts = gTTS(translated_text, lang=gtts_lang)
#             tts.save(audio_path)
#         # Store in session state
#         st.session_state["audio_file"] = audio_path

#         # Listen button OUTSIDE translate block
#         if st.button("🔊 Listen"):
#             st.audio(st.session_state["audio_file"], autoplay=True)

#         # if st.button("🔊 Listen"):
                
#         #     st.audio(audio_path, autoplay=True)

#         # st.success("Audio ready!")

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from gtts import gTTS
from streamlit_extras.stylable_container import stylable_container
import base64

# Load model
MODEL_NAME = r"C:\Users\admin\Downloads\nlp\program\nllb_model"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

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

