# Jersey Number Recognition Project

## Overview
This repository contains our implementation for the SoccerNet Jersey Number Recognition Challenge 2023. The project focuses on developing deep learning models to recognize jersey numbers in soccer videos.

## Project Structure
```
jersey-number-recognition/
├── configs/                    # Configuration files
│   ├── model/                 # Model architecture configs
│   │   └── model_config.yaml
│   ├── data/                  # Dataset and augmentation configs
│   │   └── data_config.yaml
│   └── training/              # Training hyperparameters
│       └── train_config.yaml
├── data/                      # Data directory
│   ├── raw/                   # Original dataset
│   │   ├── train/
│   │   ├── test/
│   │   └── challenge/
│   ├── processed/             # Preprocessed dataset
│   └── splits/                # Train/val/test splits
├── notebooks/                 # Jupyter notebooks
│   ├── exploratory/           # Data exploration
│   ├── experiments/           # Model experiments
│   └── analysis/              # Results analysis
├── src/                       # Source code
│   ├── __init__.py           # Main package initialization
│   ├── data/                 # Data processing
│   │   ├── __init__.py
│   │   ├── dataset.py        # Dataset classes
│   │   ├── augment.py        # Augmentation pipeline
│   │   ├── preprocess.py     # Data preprocessing
│   │   └── download_soccer_data.py  # Script to download SoccerNet data
│   ├── models/               # Model implementations
│   │   ├── __init__.py
│   │   ├── backbone.py       # CNN backbone (placeholder)
│   │   ├── neck.py          # Feature processing (placeholder)
│   │   └── head.py          # Classification head (placeholder)
│   └── utils/                # Utility functions
│       ├── __init__.py
│       ├── metrics.py        # Evaluation metrics (placeholder)
│       ├── visualization.py  # Visualization tools (placeholder)
│       └── logging.py        # Logging utilities (placeholder)
├── tests/                    # Unit tests
│   ├── __init__.py
│   ├── test_data/           # Data processing tests
│   │   └── __init__.py
│   ├── test_models/         # Model tests
│   │   └── __init__.py
│   └── test_utils/          # Utility tests
│       └── __init__.py
├── docs/            # Progress journal, meeting Logs/notes and other project documentations
├── requirements.txt          # Project dependencies
├── verify_setup.py          # Installation verification script
└── README.md                # Project documentation
```

## Setup Instructions

### For macOS (Apple Silicon M1/M2)

1. Install Python 3.10 using Homebrew:
```bash
# Update Homebrew
brew update

# Install Python 3.10
brew install python@3.10
```

2. Create and activate virtual environment:
```bash
# Create venv with Python 3.10
python3.10 -m venv venv

# Activate it
source venv/bin/activate
```

3. Install dependencies:
```bash
# Upgrade pip
pip install --upgrade pip

# Install PyTorch first (specific to M2 Mac)
pip install torch torchvision torchaudio

# Install other requirements
pip install -r requirements.txt
```

### For Windows

1. Install Python 3.10:
   - Download Python 3.10 from [Python Downloads](https://www.python.org/downloads/)
   - During installation, check "Add Python 3.10 to PATH"

2. Create and activate virtual environment:
```bash
# Create venv
python -m venv venv

# Activate it
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install PyTorch first
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other requirements
pip install -r requirements.txt
```

### Verify Installation
Run this script to verify all required packages are installed correctly:
```bash
python verify_setup.py
```

### Data Setup
1. Download the SoccerNet dataset:
```bash
# Run the download script
python src/data/download_soccer_data.py
```

2. After download completes, unzip the downloaded files:
   - Extract train.zip to `data/raw/train/`
   - Extract test.zip to `data/raw/test/`
   - Extract challenge.zip to `data/raw/challenge/`
   - After extraction, delete the `/path` directory 

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use Black for code formatting
- Use isort for import sorting
- Type hints are required for all function definitions

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- SoccerNet for providing the dataset and organizing the challenge
- PyTorch team for the deep learning framework
