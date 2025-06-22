import os
import streamlit as st
from . import core_logic
from . import dicom_handler

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

st.header("医用画像ビューワー")
uploaded = st.file_uploader("DICOMファイルをアップロード", type=["dcm"])
if uploaded:
    ds = dicom_handler.load_dicom_file(uploaded)
    if hasattr(ds, "pixel_array"):
        st.image(ds.pixel_array, caption="Uploaded DICOM")
    info = {"PatientID": ds.get("PatientID", ""), "Modality": ds.get("Modality", "")}
    st.json(info)

st.header("DICOMweb から自動取込")
base_url = st.text_input("DICOMweb URL")
study_uid = st.text_input("Study Instance UID")
if st.button("DICOMweb取込"):
    if base_url and study_uid:
        out_dir = "downloaded_dicoms"
        os.makedirs(out_dir, exist_ok=True)
        try:
            files = dicom_handler.retrieve_dicom_web(base_url, study_uid, out_dir)
            st.success(f"{len(files)} files downloaded")
        except Exception as e:
            st.error(f"Failed to retrieve: {e}")
