import argparse

from .api import GitHubAPI
from .analyzer import GitHubAnalyzer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box



console = Console()


def display_results(results):
    """Display analysis results with Rich formatting."""
    
    # Repository Overview
    overview = results['overview']
    overview_text = f"""[bold cyan]Name:[/bold cyan] {overview.name}
[bold cyan]Description:[/bold cyan] {overview.description}
[bold cyan]Stars:[/bold cyan] {overview.stars} ⭐
[bold cyan]Forks:[/bold cyan] {overview.forks} 🍴
[bold cyan]Language:[/bold cyan] {overview.language}
[bold cyan]Created:[/bold cyan] {overview.created_at.strftime('%Y-%m-%d')}
[bold cyan]Updated:[/bold cyan] {overview.updated_at.strftime('%Y-%m-%d')}"""
    
    console.print(Panel(overview_text, title="📊 Repository Overview", border_style="cyan"))
    
    # Commit Stats
    stats = results['commit_stats']
    stats_text = f"""[bold]Total Commits:[/bold] {stats.total_commits}
[bold]Commits/Day:[/bold] {stats.commits_per_day}
[bold]Most Active Day:[/bold] {stats.most_active_day}
[bold]Most Active Hour:[/bold] {stats.most_active_hour}:00 UTC"""
    
    console.print(Panel(stats_text, title="📈 Commit Analysis", border_style="green"))
    
    # Contributors Table
    table = Table(title="👥 Top Contributors", box=box.ROUNDED)
    table.add_column("#", style="cyan", justify="right")
    table.add_column("Contributor", style="magenta")
    table.add_column("Commits", justify="right", style="green")
    table.add_column("% Total", justify="right", style="yellow")
    
    for i, contrib in enumerate(results['contributors'][:10], 1):
        table.add_row(
            str(i),
            contrib.login,
            str(contrib.contributions),
            f"{contrib.percentage:.1f}%"
        )
    
    console.print(table)
    
    # Languages
    languages = results['languages']
    lang_text = "\n".join([f"[bold]{lang}:[/bold] {pct}%" for lang, pct in languages.items()])
    console.print(Panel(lang_text, title="💻 Language Breakdown", border_style="blue"))
    
    # Health Score
    health = results['health']
    
    # Color code the rating
    if health.rating == "EXCELLENT":
        rating_color = "green"
    elif health.rating == "GOOD":
        rating_color = "yellow"
    elif health.rating == "FAIR":
        rating_color = "orange"
    else:
        rating_color = "red"
    
    health_text = f"""[bold]Activity Score:[/bold] {health.activity_score}/100
[bold]Contributor Score:[/bold] {health.contributor_score}/100
[bold]Documentation Score:[/bold] {health.documentation_score}/100

[bold]Overall Score:[/bold] {health.overall_score}/100
[bold]Rating:[/bold] [{rating_color}]{health.rating}[/{rating_color}]"""
    
    console.print(Panel(health_text, title="✅ Repository Health", border_style=rating_color))


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze GitHub repositories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Interactive mode
  python main.py torvalds/linux     # Analyze specific repo
  python main.py --no-cache facebook/react
        """
    )
    
    parser.add_argument(
        'repository',
        nargs='?',
        help='Repository in owner/repo format'
    )
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help='Disable caching'
    )
    
    args = parser.parse_args()
    
    console.print(Panel.fit(
        "[bold cyan]GitHub Repository Analyzer[/bold cyan]\n[dim]Analyze any public GitHub repository[/dim]",
        border_style="cyan"
    ))
    
    # Get repository - either from args or prompt
    if args.repository:
        repo_input = args.repository
    else:
        repo_input = console.input("\n[bold cyan]Enter repository (owner/repo):[/bold cyan] ")
    
    try:
        owner, repo = repo_input.split('/')
    except ValueError:
        console.print("[red]❌ Invalid format! Use: owner/repo[/red]")
        return
    
    # Initialize API and Analyzer
    api = GitHubAPI(use_cache=not args.no_cache)
    analyzer = GitHubAnalyzer(api)
    
    # Analyze with progress indicator
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task(f"[cyan]Analyzing {owner}/{repo}...", total=None)
        
        try:
            results = analyzer.analyze_repository(owner, repo)
            progress.update(task, completed=True)
        except Exception as e:
            console.print(f"[red]❌ Error: {e}[/red]")
            return
    
    # Display results
    console.print()
    display_results(results)


if __name__ == "__main__":
    main()
