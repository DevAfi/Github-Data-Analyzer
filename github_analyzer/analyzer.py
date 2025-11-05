from .api import GitHubAPI
from .models import RepoOverview, Contributor, CommitStats, HealthScore
from .cache import SimpleCache
from typing import List, Dict, Tuple

class GitHubAnalyzer:
    def __init__(self, api: GitHubAPI):
        self.api = api