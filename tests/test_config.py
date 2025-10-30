import sys
from pathlib import Path

#Added parent file
sys.path.insert(0, str(Path(__file__).parent.parent))

from github_analyzer.config import GITHUB_TOKEN

if GITHUB_TOKEN:
    print(f"Token loaded: {GITHUB_TOKEN[:10]}...")
else:
    print("No token found!")