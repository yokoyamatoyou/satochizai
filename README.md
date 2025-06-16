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

Phase 3 utilities for semantic drift analysis and trajectory visualization are
implemented in `diverse_perspective_mvp/core_logic.py`.
