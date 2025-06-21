# AI Antivirus – Malware Classifier with Static Analysis

## Overview

This project aims to create an AI-powered antivirus system capable of detecting malware using **static analysis** and advanced machine learning. By leveraging feature extraction from executable files and training ML models (e.g., XGBoost, LightGBM), it classifies binaries as benign or malicious without executing them. The project is built for flexibility, GPU acceleration, and reproducible research.

## Features

- **Static Malware Detection:** Uses the EMBER dataset for learning from real-world PE (Windows Portable Executable) files.
- **Modern ML Pipeline:** Modular design for data loading, feature extraction, model training, and evaluation.
- **GPU Acceleration:** Out-of-the-box support for GPU training with XGBoost and LightGBM.
- **Dockerized Environment:** Easily run experiments and serve models in isolated containers.
- **Extensible Structure:** Well-organized folders for data, scripts, configs, and source code to support research and experimentation.

## Project Structure

```
.
├── data/                # Processed training/test data (not committed)
├── notebooks/           # Prototyping & EDA (Jupyter/IPython notebooks)
├── scripts/             # CLI scripts for training/evaluation
├── configs/             # YAML/JSON config files
├── tests/               # Unit tests (pytest)
├── src/
│   ├── data/            # Data loading & preprocessing
│   ├── features/        # Feature extraction
│   ├── models/          # Model training, saving, loading
│   ├── evaluation/      # Metrics and evaluation
│   ├── serving/         # Inference & API logic
│   └── utils/           # Helpers (logging, configs, etc.)
├── requirements.txt
├── Dockerfile
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/avasile96/ml-cybersec.git
cd ml-cybersec
```

### 2. Prepare the Data

- Download the [EMBER dataset](https://github.com/endgameinc/ember) (or use your own PE dataset).
- Place the dataset in the `data/` directory or update the path in your config/scripts.

### 3. Build the Docker Image (Recommended)

```bash
docker build -t ai-antivirus .
```

Or, set up Python 3.11+ and install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Train a Model

```bash
python scripts/train_model.py
```

- This will load data, train a GPU-accelerated XGBoost model, and save it to `models/ember_lgbm.pkl`.

### 5. Run Unit Tests

```bash
pytest tests/
```

## Example: Training Script

The training pipeline (`scripts/train_model.py`) loads features, trains a classifier, saves the model, and prints metrics:

```python
from src.models.train import train_model
model, metrics = train_model(data_dir="data")
print(metrics)  # {'auc': 0.98, 'accuracy': 0.97}
```

## Technologies Used

- **Python 3.11+**
- **XGBoost** & **LightGBM** (with GPU support)
- **EMBER Dataset** (feature extraction for PE files)
- **Docker** (for reproducible environments)
- **Pytest** (for testing)

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

**Author:** [@avasile96](https://github.com/avasile96)
