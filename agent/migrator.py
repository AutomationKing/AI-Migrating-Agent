import yaml
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

import time

def load_config():
    return yaml.safe_load(open("config/settings.yaml"))

def get_llm():
    cfg = load_config()
    return ChatOpenAI(model=cfg["llm_model"], temperature=cfg["temperature"])

# Simple wrapper with retry for LLM calls
def migrate_java_to_ts(java_code: str, file_type="java", retries=2):
    llm = get_llm()
    template = (

        "You are an expert automation architect.\n"

        "Convert this Selenium Java (Cucumber) {file_type} to Playwright + TypeScript.\n"

        "Preserve behavior, naming, locators, and comments where possible.\n"

        "Return only the TypeScript file content. If conversion is not possible, explain why.\n\n"

        "### INPUT\n{code}\n\n### OUTPUT\n"

    )

    prompt = PromptTemplate(input_variables=["code", "file_type"], template=template)

    last_exc = None
    for attempt in range(retries + 1):
        try:
            response = llm.predict(prompt.format(code=java_code, file_type=file_type))
            return response
        except Exception as e:
            last_exc = e
            print(f"⚠️ LLM call failed (attempt {attempt+1}/{retries+1}): {e}")
            time.sleep(2 ** attempt)
    raise last_exc
