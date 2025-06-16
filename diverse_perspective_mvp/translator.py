import os
from typing import List, Tuple

import openai
from dotenv import load_dotenv

# Load API key from .env if present
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def translate_text(text: str, src: str, tgt: str) -> str:
    """Translate text from src language to tgt language via ChatCompletion."""
    prompt = f"Translate the following text from {src} to {tgt}:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()


def run_translation_chain(source_text: str, language_path: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """Run sequential translations along the given language path."""
    text = source_text
    results = []
    for src, tgt in language_path:
        text = translate_text(text, src, tgt)
        results.append((tgt, text))
    return results
