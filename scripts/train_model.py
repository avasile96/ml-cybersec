import sys
from pathlib import Path
from src.models.train import train_model
import joblib

DATA_DIR = Path("data")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

print("🚀 Training model...")
model, metrics = train_model(DATA_DIR)

model_path = MODEL_DIR / "ember_lgbm.pkl"
joblib.dump(model, model_path)

print(f"✅ Model saved to: {model_path}")
print("📊 Metrics:")
for k, v in metrics.items():
    print(f"  {k}: {v:.4f}")
