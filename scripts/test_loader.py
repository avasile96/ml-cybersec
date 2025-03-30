# scripts/test_loader.py

import sys
import os

# Add src to the module search path
sys.path.append(os.path.abspath("."))

from src.data.load_ember import load_ember_dataset

# Use the actual location where ember2018 lives
EMBER_PATH = "D:/ai-antivirus-data/ember/ember2018"

# Load a few samples from the training set
features, labels = load_ember_dataset(EMBER_PATH, split="train", max_samples=3)

# Sanity checks
print("✅ Loaded", len(features), "samples")
print("🧩 First sample keys:", features[0].keys())
print("🔖 First label:", labels[0])
