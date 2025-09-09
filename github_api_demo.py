#!/usr/bin/env python3
"""
GitHub API Demo Script
Demonstrates how to interact with GitHub API using Python
"""

import requests
import json
from datetime import datetime

def get_user_info(username):
    """Fetch user information from GitHub API"""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_user_repos(username, limit=5):
    """Fetch user repositories from GitHub API"""
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": "updated", "per_page": limit}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return []

def display_user_summary(username):
    """Display a summary of user information and repositories"""
    print(f"GitHub User Summary for: {username}")
    print("=" * 50)
    
    # Get user info
    user_info = get_user_info(username)
    if user_info:
        print(f"Name: {user_info.get('name', 'N/A')}")
        print(f"Bio: {user_info.get('bio', 'N/A')}")
        print(f"Public Repos: {user_info.get('public_repos', 0)}")
        print(f"Followers: {user_info.get('followers', 0)}")
        print(f"Following: {user_info.get('following', 0)}")
        print(f"Created: {user_info.get('created_at', 'N/A')}")
    
    print("\nRecent Repositories:")
    print("-" * 30)
    
    # Get recent repos
    repos = get_user_repos(username)
    for repo in repos:
        print(f"• {repo['name']}")
        print(f"  Language: {repo.get('language', 'N/A')}")
        print(f"  Stars: {repo.get('stargazers_count', 0)}")
        print(f"  Updated: {repo.get('updated_at', 'N/A')}")
        print()

def main():
    """Main function to demonstrate GitHub API usage"""
    username = "Vibe-Marketer"  # Default username for demo
    display_user_summary(username)
    
    print(f"\nScript executed at: {datetime.now()}")

if __name__ == "__main__":
    main()

