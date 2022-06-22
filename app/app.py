from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve()
sys.path.append(str(BASE_DIR))

print('hello')