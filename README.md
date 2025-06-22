# satochizai

See MVP_PLAN.md for the development plan.

## Setup

1. Copy `.env.example` to `.env` and set your `OPENAI_API_KEY`.
2. Install dependencies:
   ```bash
   pip install -r diverse_perspective_mvp/requirements.txt
   ```
3. Run the prototype Streamlit app:
   ```bash
   streamlit run diverse_perspective_mvp/app.py
   ```

## Medical Image Workflow

The app allows manual upload of DICOM files as well as automatic retrieval via
DICOMweb. Retrieved images can be reviewed in the built-in viewer. Analysis
results may be exported back to PACS as DICOM overlays or Structured Reports.
