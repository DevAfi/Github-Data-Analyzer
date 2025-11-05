import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from github_analyzer.api import GitHubAPI
from github_analyzer.analyzer import GitHubAnalyzer


def test_analyzer():
    """Test the full analyzer"""
    api = GitHubAPI(use_cache=True)
    analyzer = GitHubAnalyzer(api)
    
    results = analyzer.analyze_repository("Naumanpatell", "Cognivue")
    
    print("\n" + "="*60)
    print("REPOSITORY OVERVIEW")
    print("="*60)
    overview = results['overview']
    print(f"Name: {overview.name}")
    print(f"Description: {overview.description}")
    print(f"Stars: {overview.stars} ⭐")
    print(f"Forks: {overview.forks} 🍴")
    print(f"Language: {overview.language}")
    
    print("\n" + "="*60)
    print("COMMIT STATS")
    print("="*60)
    stats = results['commit_stats']
    print(f"Total Commits: {stats.total_commits}")
    print(f"Commits/Day: {stats.commits_per_day}")
    print(f"Most Active Day: {stats.most_active_day}")
    print(f"Most Active Hour: {stats.most_active_hour}:00")
    
    print("\n" + "="*60)
    print("TOP CONTRIBUTORS")
    print("="*60)
    for i, contrib in enumerate(results['contributors'][:5], 1):
        print(f"{i}. {contrib.login}: {contrib.contributions} commits ({contrib.percentage:.1f}%)")
    
    print("\n" + "="*60)
    print("LANGUAGES")
    print("="*60)
    for lang, pct in results['languages'].items():
        print(f"{lang}: {pct}%")
    
    print("\n" + "="*60)
    print("HEALTH SCORE")
    print("="*60)
    health = results['health']
    print(f"Activity: {health.activity_score}/100")
    print(f"Contributors: {health.contributor_score}/100")
    print(f"Documentation: {health.documentation_score}/100")
    print(f"\nOverall: {health.overall_score}/100 - {health.rating}")


if __name__ == "__main__":
    test_analyzer()