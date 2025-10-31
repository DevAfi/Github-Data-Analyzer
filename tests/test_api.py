import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from github_analyzer.api import GitHubAPI

def test_generic_request():
    """Test a generic API request"""
    api = GitHubAPI()

    data = api._make_request("/repos/octocat/Hello-World")

    print(f"✅ API connection works!")
    print(f"   Repo: {data['name']}")
    print(f"   Stars: {data['stargazers_count']}")
    print(f"   Owner: {data['owner']['login']}")

def test_all_requests():
    """Test all specific API requests"""
    api = GitHubAPI()
    owner = "octocat"
    repo = "Hello-World"

    # Test get_repo
    repo_data = api.get_repo(owner, repo)
    print(f"✅ get_repo works! Repo name: {repo_data['name']}")
    # Test get_commits
    commits = api.get_commits(owner, repo)
    print(f"✅ get_commits works! Number of commits fetched: {len(commits)}")
    # Test get_contributors
    contributors = api.get_contributors(owner, repo)
    print(f"✅ get_contributors works! Number of contributors fetched: {len(contributors)}")
    # Test get_languages
    languages = api.get_languages(owner, repo)
    print(f"✅ get_languages works! Languages: {list(languages.keys())}")

def test_rate_limit():
    """Test rate limit checking"""
    api = GitHubAPI()
    
    rate_limit = api.get_rate_limit()
    core = rate_limit['resources']['core']
    
    print(f"✅ Rate Limit Info:")
    print(f"   Limit: {core['limit']} requests/hour")
    print(f"   Remaining: {core['remaining']}")
    print(f"   Resets at: {core['reset']}")
    
    # Test with invalid repo to see error handling
    print("\n Testing error handling...")
    try:
        api.get_repo("invalid", "repo-that-does-not-exist-12345")
    except Exception as e:
        print(f"✅ Error caught: {e}")


if __name__ == "__main__":
    #test_generic_request()
    #test_all_requests()
    test_rate_limit()