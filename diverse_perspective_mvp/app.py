import streamlit as st
from . import core_logic

st.title("多角的理解支援システム (MVP)")

source_text = st.text_area("分析したいテキストをここに貼り付けてください:", height=200)

if st.button("分析開始"):
    if not source_text.strip():
        st.warning("テキストを入力してください")
    else:
        st.write("多様な言語経路を選択中...")
        translations = core_logic.translate_via_diverse_path(source_text, 'en')
        st.write("翻訳結果:")
        for lang, text in translations:
            st.subheader(lang)
            st.write(text)
