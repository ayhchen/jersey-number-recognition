import sys
import pkg_resources
import importlib

def verify_imports():
    # Map package names to their import names where different
    package_import_map = {
        'opencv-python': 'cv2',
        'scikit-learn': 'sklearn',
        # Add other packages that have different import names here
    }

    required_packages = [
        'torch',
        'torchvision',
        'numpy',
        'pandas',
        'opencv-python',
        'albumentations',
        'matplotlib',
        'seaborn',
        'wandb',
        'tensorboard',
        'tqdm',
        'pytest',
        'black',
        'isort',
        'flake8',
        'SoccerNet'
    ]

    print("Python version:", sys.version)
    
    for package in required_packages:
        try:
            # Use the mapped import name if it exists, otherwise use the package name
            import_name = package_import_map.get(package, package).replace('-', '_')
            importlib.import_module(import_name)
            version = pkg_resources.get_distribution(package).version
            print(f"✓ {package:<20} {version}")
        except ImportError as e:
            print(f"✗ {package:<20} Not installed (Import Error: {str(e)})")
        except Exception as e:
            print(f"? {package:<20} Error: {str(e)}")

    # Additional PyTorch checks
    if 'torch' in sys.modules:
        import torch
        print("\nPyTorch specific checks:")
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        if sys.platform == "darwin":  # macOS
            print(f"MPS available: {torch.backends.mps.is_available()}")

if __name__ == "__main__":
    verify_imports()