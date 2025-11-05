## 📊 GitHub Data Analyzer CLI

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![API](https://img.shields.io/badge/API-GitHub%20REST-orange.svg)](https://docs.github.com/en/rest)
[![UI](https://img.shields.io/badge/UI-Rich%20Terminal-purple.svg)](https://rich.readthedocs.io/)

### Overview
A powerful command-line tool for analyzing GitHub repositories with beautiful terminal output. Get comprehensive insights about any public repository including commit patterns, contributor statistics, language distribution, and health scores. Features include:

- **📊 Repository Overview** - Name, description, stars, forks, language, and creation/update dates
- **📈 Commit Analysis** - Total commits, commits per day, most active day and hour patterns
- **👥 Contributor Statistics** - Top contributors with contribution counts and percentages
- **💻 Language Breakdown** - Percentage distribution of programming languages used
- **✅ Health Score** - Comprehensive repository health rating based on activity, contributors, and documentation
- **🎨 Beautiful Rich UI** - Colored tables, panels, and progress indicators
- **⚡ Intelligent Caching** - Local caching system to reduce API calls and improve performance
- **🔐 GitHub API Integration** - Full support for authenticated requests with rate limit handling

This repo includes a complete CLI tool for analyzing GitHub repositories with professional-grade terminal output and comprehensive data insights.

### Tech Stack
- **Python 3.9+**
- **Rich**: Beautiful terminal UI with tables, panels, and colored output
- **requests**: HTTP library for GitHub API interactions
- **python-dotenv**: Environment variable management for GitHub tokens
- **pickle**: Local caching system for API responses
- **argparse**: Command-line argument parsing
- **dataclasses**: Type-safe data models for repository analysis

### Why I Built This

I created this GitHub analyzer to solve a real problem I faced when evaluating repositories - getting quick, comprehensive insights about a project's health, activity, and contributor patterns. While GitHub's web interface provides some metrics, I wanted something that was:

- **⚡ Fast** - Quick analysis without navigating through multiple pages
- **📊 Comprehensive** - All key metrics in one place with calculated insights
- **💻 Terminal-native** - Command-line workflow that integrates with my development environment
- **🎨 Beautiful** - Rich terminal UI that makes data analysis actually enjoyable
- **🔍 Educational** - Learn about GitHub API, data analysis, and CLI design patterns
- **🚀 Performance-optimized** - Caching system to minimize API calls and respect rate limits

This project demonstrates my approach to building production-ready CLI tools with clean architecture, proper error handling, and user-friendly interfaces.

### Project Structure
```text
github_analyzer/
  __init__.py          # Package initialization
  api.py               # GitHub API client with caching and rate limit handling
  analyzer.py          # Core analysis logic and statistics calculation
  cache.py             # Local caching system using pickle
  cli.py               # Rich-powered command-line interface
  config.py            # Configuration management with dotenv
  models.py            # Data models (RepoOverview, Contributor, CommitStats, HealthScore)
  main.py              # CLI entrypoint
  cache/               # Local cache directory (auto-generated)
  tests/               # Unit tests
    test_analyzer.py
    test_api.py
    test_config.py
  requirements.txt     # Python dependencies
  README.md
  venv/                # Virtual environment (optional)
```

### Security & Rate Limits
- **GitHub Token Support** - Optional authentication via `GITHUB_TOKEN_CODE` environment variable
- **Rate Limit Handling** - Automatic tracking and warnings when approaching API limits
- **Caching System** - Reduces API calls by caching responses locally
- **Error Handling** - Graceful handling of 403 (rate limit), 404 (not found), and network errors
- **Unauthenticated Mode** - Works without token but with lower rate limits (60 requests/hour)

### Getting Started

#### 1) Requirements
- Python 3.9+
- Windows/macOS/Linux supported

#### 2) Create and activate a virtual environment (optional but recommended)
```bash
# from project root
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows PowerShell
./venv/Scripts/Activate.ps1
# or Command Prompt
venv\Scripts\activate.bat
# or Git Bash
source venv/Scripts/activate
```

#### 3) Install dependencies
```bash
pip install -r requirements.txt
```

#### 4) Set up GitHub Token (Optional but Recommended)
Create a `.env` file in the project root:
```bash
GITHUB_TOKEN_CODE=your_github_personal_access_token_here
```

**Why use a token?**
- **Higher rate limits**: 5,000 requests/hour vs 60 requests/hour unauthenticated
- **Access to private repos**: If you have access
- **Better reliability**: Less likely to hit rate limits

**How to get a token:**
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `public_repo` scope
3. Copy token to `.env` file

### Usage

#### Interactive Mode
Run without arguments for interactive mode:
```bash
python main.py
```
You'll be prompted to enter a repository in `owner/repo` format.

#### Command-Line Mode
Analyze a specific repository directly:
```bash
python main.py owner/repo
```

**Examples:**
```bash
# Analyze a popular repository
python main.py torvalds/linux

# Analyze a React repository
python main.py facebook/react

# Disable caching for fresh data
python main.py --no-cache microsoft/vscode
```

#### CLI Options
- `repository` (positional): Repository in `owner/repo` format
- `--no-cache`: Disable caching and fetch fresh data from API

### Output Breakdown

#### 📊 Repository Overview
- Repository name and full name
- Description
- Star and fork counts
- Primary programming language
- Creation and last update dates

#### 📈 Commit Analysis
- **Total Commits**: Number of commits analyzed (limited to API pagination)
- **Commits/Day**: Average commits per day based on date range
- **Most Active Day**: Day of week with most commits (Monday-Sunday)
- **Most Active Hour**: Hour of day (UTC) with most commit activity

#### 👥 Top Contributors
- Ranked list of top 10 contributors
- Contribution counts per contributor
- Percentage of total contributions
- Formatted in a beautiful table

#### 💻 Language Breakdown
- Percentage distribution of all languages used
- Calculated from GitHub's language statistics API
- Shows relative code distribution

#### ✅ Repository Health Score
Comprehensive health rating based on three factors:

**Activity Score (40% weight):**
- 100 points: Updated within last 7 days
- 80 points: Updated within last 14 days
- 60 points: Updated within last 30 days
- 40 points: Updated more than 30 days ago

**Contributor Score (30% weight):**
- 100 points: 50+ contributors
- 80 points: 20-49 contributors
- 60 points: 10-19 contributors
- 40 points: 5-9 contributors
- 20 points: Less than 5 contributors

**Documentation Score (30% weight):**
- 40 points: Has description
- 30 points: Has license
- 30 points: Has wiki enabled

**Overall Rating:**
- **EXCELLENT**: 80-100 points
- **GOOD**: 60-79 points
- **FAIR**: 40-59 points
- **POOR**: 0-39 points

### Configuration Files
- **`.env`**: GitHub personal access token (optional)
- **`cache/`**: Local cache directory storing pickled API responses
- **`requirements.txt`**: Python package dependencies

### Roadmap (Future Enhancements)
- **Phase 2: Advanced Analytics** 🔄
  - Issue and PR statistics
  - Release history analysis
  - Dependency analysis
  - Security vulnerability scanning
  - Commit message sentiment analysis
  - Code quality metrics (complexity, test coverage)
- **Phase 3: Export & Reporting** 🔄
  - Export results to JSON/CSV/PDF
  - Generate comparison reports between repositories
  - Historical tracking and trend analysis
  - Batch repository analysis
- **Phase 4: Polish & Optimization** 🔄
  - Comprehensive unit tests and CI/CD
  - Performance optimizations for large repositories
  - README visuals (demo GIFs/screenshots)
  - Advanced filtering and search options
  - Custom health score weights configuration

### Lessons Learned & Challenges Faced

**🔌 API Integration Challenges:**
- **Rate Limiting**: Learned the importance of caching and rate limit tracking to avoid hitting GitHub's API limits
- **Pagination**: Understanding GitHub API pagination and how to handle large datasets efficiently
- **Error Handling**: Implementing robust error handling for network issues, authentication failures, and missing repositories
- **Token Management**: Balancing security (environment variables) with usability (optional authentication)

**📊 Data Analysis Insights:**
- **Statistical Calculations**: Implementing meaningful metrics from raw API data (commits per day, activity patterns)
- **Time Zone Handling**: Properly handling UTC timestamps and converting to meaningful local patterns
- **Data Aggregation**: Efficiently processing large lists of commits and contributors
- **Health Score Algorithm**: Designing a balanced scoring system that accurately reflects repository health

**🎨 UI/UX Design:**
- **Rich Library Mastery**: Learning Rich's table, panel, and styling system for professional terminal output
- **Color Coding**: Using colors strategically to convey meaning (health scores, activity levels)
- **Progress Indicators**: Providing user feedback during API calls
- **Information Hierarchy**: Organizing complex data into digestible sections

**🏗️ Architecture Decisions:**
- **Modular Design**: Separating API, analysis, caching, and UI into distinct modules for maintainability
- **Caching Strategy**: Implementing a simple but effective caching system to improve performance
- **Type Safety**: Using dataclasses for type-safe data models
- **Error Propagation**: Designing clean error handling that doesn't expose implementation details

**⚡ Performance Considerations:**
- **Caching System**: Reducing API calls significantly improves response time and respects rate limits
- **API Efficiency**: Minimizing the number of API calls required for comprehensive analysis
- **Data Processing**: Efficiently processing and aggregating commit and contributor data
- **Memory Usage**: Managing memory when dealing with repositories with thousands of commits

**🛠️ Development Process:**
- **Testing Strategy**: Learning to test API integrations with mocking and fixtures
- **Documentation**: Balancing comprehensive documentation with code clarity
- **CLI Design**: Creating an intuitive command-line interface with both interactive and programmatic modes

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Optional: Set up GitHub token in .env file
echo "GITHUB_TOKEN_CODE=your_token_here" > .env

# Run in interactive mode
python main.py

# Or analyze a specific repo
python main.py owner/repo
```

### Development Notes
- **Code style**: Follow descriptive variable naming, type hints where appropriate
- **API**: Uses GitHub REST API v3 with proper authentication headers
- **Caching**: Pickle-based caching system with MD5 hashing for cache keys
- **UI**: Rich library provides beautiful terminal interfaces with tables, panels, and colored output
- **Architecture**: Modular design with separate files for API, analysis, caching, and UI components
- **Error Handling**: Comprehensive error handling for API errors, network issues, and invalid inputs

### Troubleshooting

**Rate Limit Exceeded:**
- Set up a GitHub personal access token in `.env` file for higher rate limits
- Use caching (default enabled) to reduce API calls
- Wait for rate limit to reset (check with `api.get_rate_limit()`)

**Repository Not Found:**
- Verify the repository exists and is public
- Check the format: `owner/repo` (e.g., `facebook/react`)
- Ensure you have access if it's a private repository (requires token)

**Installation Issues:**
- Ensure Python 3.9+ is installed
- Use a virtual environment to avoid dependency conflicts
- On some systems, `requests` may require additional system libraries

**Cache Issues:**
- Clear cache by deleting the `cache/` directory
- Use `--no-cache` flag to bypass cache
- Cache files are stored as pickle files in `cache/` directory

**Display Issues:**
- If colors don't display properly, ensure your terminal supports ANSI colors
- Rich library should work on most modern terminals
- Try running in a different terminal emulator if issues persist

### API Rate Limits

**Without Authentication:**
- 60 requests per hour
- IP-based rate limiting

**With Authentication:**
- 5,000 requests per hour
- Token-based rate limiting
- More reliable for batch operations

**Current Usage:**
- Each repository analysis requires ~4 API calls (repo, commits, contributors, languages)
- With caching enabled, repeated analyses use cached data
- Rate limit remaining is displayed in warnings when below 10 requests

### Contributing

Contributions are welcome! Areas for improvement:
- Additional analysis metrics
- Better caching strategies
- Export functionality
- Performance optimizations
- Test coverage improvements

### License
MIT

