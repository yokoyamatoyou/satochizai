# Phase 1 Implementation Guide

The goal of Phase 1 is to create the basic project structure and prepare the environment. These instructions are for Codex agents in a separate conversation who will begin the implementation.

## Repository Layout
Create a directory named `diverse_perspective_mvp` at the repository root with the following structure:

```
/diverse_perspective_mvp
|-- app.py            # Streamlit GUI entry point (placeholder)
|-- core_logic.py     # Core processing functions (empty for now)
|-- data_handler.py   # Data loading and preprocessing (empty for now)
|-- requirements.txt  # List of dependencies
|-- .env              # API keys (not committed)
|-- /data             # Data files go here
```

## Tasks
1. **Set up directories and files**
   - Create the folder and files listed above. Add minimal comments or placeholder code so that the files exist in the repository.

2. **Populate `requirements.txt`**
   - Include the initial dependencies:
     ```
     openai
     pandas
     numpy
     requests
     sentence-transformers
     scikit-learn
     plotly
     streamlit
     gdelt
     ```

3. **Environment file**
   - Create `.env` with the variable `OPENAI_API_KEY=`. Leave the value blank. This file should not be committed.
   - Add `.env` to `.gitignore` if it is not already present.

4. **Update Progress**
   - Once the directory structure and files are created, update `MANUAL.md` to mark Phase 1 as "in progress".

Follow these steps to initialize the project for further development.
