# scaffold_project.py

import os

project_dirs = [
    "data",                     # Your processed training data (not committed)
    "notebooks",                # For EDA, prototyping
    "scripts",                  # CLI scripts for training/evaluation
    "configs",                  # YAML/JSON config files for model/dataset settings
    "tests",                    # Unit tests (we’ll use pytest)
    "src",                      # Source code base
    "src/data",                 # Data loading & preprocessing
    "src/features",             # Feature extraction from JSON
    "src/models",               # Training, saving, loading models
    "src/evaluation",           # Metrics and evaluation functions
    "src/serving",              # Inference + API logic
    "src/utils"                 # Logging, config helpers, etc.
]

files_to_create = {
    ".gitignore": "\n".join([
        "__pycache__/",
        "*.pyc",
        ".env",
        "venv/",
        "data/",
        ".ipynb_checkpoints/",
        "logs/",
        "*.log"
    ]),
    "README.md": "# AI Antivirus – Malware Classifier with Static Analysis",
    "requirements.txt": "# Add dependencies here",
    "Dockerfile": """\
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \\
    pip install -r requirements.txt

CMD ["python"]
""",
    "pyproject.toml": "# Optional if you want to use poetry or modern packaging later"
}

# Create folders
for path in project_dirs:
    os.makedirs(path, exist_ok=True)

# Create initial files
for filename, content in files_to_create.items():
    with open(filename, "w") as f:
        f.write(content)

print("✅ Project scaffolded successfully!")
