# AI Migration Agent (Selenium Java + Cucumber -> Playwright TypeScript)

This is a project skeleton for an LLM-powered migration agent that clones a GitHub repository,
analyzes Java + Cucumber files, and migrates them to Playwright + TypeScript.

## Quick start
1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI / LLM API key in environment variables (example for OpenAI):
   ```bash
   export OPENAI_API_KEY="your_api_key_here"   # macOS/Linux
   setx OPENAI_API_KEY "your_api_key_here"     # Windows (restart needed)
   ```
4. Run the migration (example):
   ```bash
   python main.py https://github.com/your-org/selenium-cucumber-java
   ```

## Notes
- This skeleton uses LangChain + ChatOpenAI as a placeholder for LLM calls. Replace model names and credentials as needed.
- The migrator currently makes simple prompt-based conversions. For production, consider adding Java AST parsing (javaparser), vector DB memory, and validation/self-heal loops.
- The generated Playwright project will be placed in the folder configured in `config/settings.yaml` (default `playwright-migrated`).
