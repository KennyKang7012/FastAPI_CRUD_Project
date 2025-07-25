# FastAPI CRUD

## Quick Start

1. **Read GEMINI.md first** - Contains essential rules for Gemini Code
2. Follow the pre-task compliance checklist before starting any work
3. Use proper module structure under `src/main/[language]/`
4. Commit after every completed task

## Universal Flexible Project Structure

Choose the structure that fits your project:

**Simple Projects:** Basic src/, tests/, docs/, output/ structure
**Standard Projects:** Full application structure with modular organization  
**AI/ML Projects:** Complete MLOps-ready structure with data, models, experiments

## Development Guidelines

- **Always search first** before creating new files
- **Extend existing** functionality rather than duplicating  
- **Use Task agents** for operations >30 seconds
- **Single source of truth** for all functionality
- **Language-agnostic structure** - works with Python, JS, Java, etc.
- **Scalable** - start simple, grow as needed
- **Flexible** - choose complexity level based on project needs

## How to Run the Project

1.  **Install Dependencies (using virtual environment):**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the Application (development mode):**
    ```bash
    uvicorn src.main:app --reload
    ```
    After starting, you can browse `http://127.0.0.1:8000/docs` to view and test the automatically generated interactive API documentation.

## How to Run Tests

1.  **Activate the virtual environment:**
    ```bash
    .\venv\Scripts\activate
    ```
2.  **Run tests:**
    ```bash
    pytest
    ```