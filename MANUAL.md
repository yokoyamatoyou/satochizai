# MVP Development Plan: Multi-Perspective Understanding Support System

This manual summarizes the tasks and procedures required to build the "Multi-Perspective Understanding Support System" as a GUI application using the OpenAI API. The project demonstrates the concept of presenting diverse cultural and interpretive viewpoints for better understanding.

## Overview

- The application is written in **Python 3.10+**.
- Core functionality relies on the **OpenAI API** for translation and analysis.
- External data sources (Hofstede, WALS, GDELT) should be retrieved via an accessible API whenever possible. API keys are provided through environment variables.
- When data is missing, retry the retrieval. If it still fails, skip the record and log the skipped entry.
- A sample input uses a news article. Output is displayed on the GUI and saved as plain text.

## Development Phases

### Phase 1: Project Setup
1. Create the following structure:
   ```
   /diverse_perspective_mvp
   |-- app.py            # Streamlit GUI
   |-- core_logic.py     # Core processing functions
   |-- data_handler.py   # Data loading and preprocessing
   |-- requirements.txt  # Library list
   |-- .env              # API keys (not committed)
   |-- /data
   ```
2. Install required libraries listed in `requirements.txt`.

### Phase 2: Data Retrieval and Preparation
1. Implement `data_handler.py` to download Hofstede scores, WALS features, and GDELT data. Use the OpenAI API or other accessible endpoints.
2. Handle missing values by retrying. If data remains missing, skip the entry and record the skip.
3. Store cleaned CSV files under `/data`.

### Phase 3: Core Scoring Functions (`core_logic.py`)
1. Implement:
   - `calculate_cds(country1_code, country2_code)` using Hofstede data.
   - `calculate_gis(country1_code, country2_code)` using GDELT.
   - `calculate_lds(lang1_code, lang2_code)` using WALS features.
2. Create `select_diverse_languages(source_language, num_pivots=3)` that picks translation paths maximizing diversity.

### Phase 4: Translation Pipeline
1. Add `translate_text(text, source_lang, target_lang)` utilizing the OpenAI API. API key is read from the environment variable `OPENAI_API_KEY`.
2. Implement `run_translation_chain(source_text, language_path)` to execute translations sequentially and store each step.

### Phase 5: Semantic Analysis and Visualization
1. Embed each translation using `sentence-transformers`.
2. Calculate semantic drift with cosine distance.
3. Visualize trajectory with `plotly` or `matplotlib`.

### Phase 6: GUI Integration (`app.py`)
1. Build a Streamlit interface where users paste a news article as input.
2. On "Analyze" button press, run language selection, translation chain, and visualization.
3. Display results in the GUI, including translation steps and drift plot.

### Phase 7: Finalization
1. Add error handling for API failures or missing files.
2. Update `README.md` with setup instructions, including creating `.env` with the `OPENAI_API_KEY`.
3. Provide a script or instructions for running `streamlit run app.py`.

## Notes
- This manual should remain in the repository so future agents can reference the current plan, even if the conversation context is lost.
- Update this document as tasks are completed or requirements change.

## Current Progress

At this stage only the project documentation has been created. No code or data files
have been implemented yet.

### Status by Phase

- **Phase 1: Project Setup** – *pending*
- **Phase 2: Data Retrieval and Preparation** – *pending*
- **Phase 3: Core Scoring Functions** – *pending*
- **Phase 4: Translation Pipeline** – *pending*
- **Phase 5: Semantic Analysis and Visualization** – *pending*
- **Phase 6: GUI Integration** – *pending*
- **Phase 7: Finalization** – *pending*

The next step is to start Phase&nbsp;1 by creating the directory structure
and installing the required libraries listed in `requirements.txt`.
