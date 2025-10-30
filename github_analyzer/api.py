import requests
from typing import Optional, Dict, Any, List
from .config import GITHUB_TOKEN, GITHUB_API_BASE

class GitHubAPI:
    def __init__(self, token: Optional[str] = None):
        """   Initialize the Github API client    """
        self.token = token or GITHUB_TOKEN
        self.base_url = GITHUB_API_BASE
        self.session = requests.Session()

        #Headers for all sessions
        self.session.headers.update({
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Analyzer-CLI' #KIM
        })

    #Generic request
    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
            """Make a GET request to the Github API"""
            url = f"{self.base_url}{endpoint}"

            response = self.session.get(url, params=params)
            response.raise_for_status()

            return response.json()
    
    def get_repo(self, owner: str, repo: str) -> Dict[str, Any]:
        """Get repo information"""
        return self._make_request(f"/repos/{owner}/{repo}")
    
    def get_commits(self, owner: str, repo: str, per_page: int = 100, page: int = 1) -> List[Dict[str, Any]]:
        """Get commits on a repo"""
        params = {"per_page": per_page, "page": page}
        return self._make_request(f"/repost/{owner}/{repo}/commits", params=params)
    
    def get_contributors(self, owner: str, repo: str) -> List[Dict[str, Any]]:
        """Get contributors to a repo"""
        return self._make_request(f"/repos/{owner}/{repo}/contributors")

    def get_languages(self, owner: str, repo: str) -> Dict[str, int]:
        """Get languages used in a repo"""
        return self._make_request(f"/repos/{owner}/{repo}/languages")
