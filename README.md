# GitHub CLI Test Repository

Test repository to demonstrate GitHub CLI capabilities and API integration.

## Overview

This repository showcases various GitHub CLI features and includes a Python script that demonstrates how to interact with the GitHub API programmatically.

## Features

- **GitHub API Integration**: Python script to fetch user information and repositories
- **CLI Demonstrations**: Examples of GitHub CLI commands and workflows
- **Repository Management**: Shows how to create, clone, and manage repositories

## Files

- `github_api_demo.py`: Python script demonstrating GitHub API usage
- `requirements.txt`: Python dependencies
- `README.md`: This documentation file

## Installation

1. Clone this repository:
   ```bash
   gh repo clone Vibe-Marketer/github-cli-test
   cd github-cli-test
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the GitHub API demo script:

```bash
python3 github_api_demo.py
```

This will display information about the default GitHub user and their repositories.

## GitHub CLI Commands Demonstrated

### Authentication
```bash
gh auth status
```

### Repository Management
```bash
# List repositories
gh repo list --limit 10

# Create a new repository
gh repo create my-repo --public --add-readme

# Clone a repository
gh repo clone username/repo-name
```

### Data Fetching
```bash
# Get user information
gh api user

# List commits
gh api repos/owner/repo/commits

# Repository statistics
gh api repos/owner/repo
```

### Issues and Pull Requests
```bash
# List issues
gh issue list --repo owner/repo

# Create an issue
gh issue create --title "Bug report" --body "Description"

# List pull requests
gh pr list --repo owner/repo
```

## API Capabilities

The GitHub CLI provides access to the full GitHub REST API through the `gh api` command, allowing you to:

- Fetch user profiles and statistics
- Manage repositories, issues, and pull requests
- Access commit history and repository metadata
- Manage releases, deployments, and workflows
- Interact with GitHub Actions and packages

## Created

This repository was created using GitHub CLI as a demonstration of its capabilities.

**Created**: September 2025  
**Purpose**: GitHub CLI feature demonstration and testing
