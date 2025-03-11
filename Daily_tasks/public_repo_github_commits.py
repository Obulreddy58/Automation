import requests

# Fetch commits from the GitHub repository (no authentication needed for public repos)
def fetch_commits(repo_url):
    """Fetch commits from the public GitHub repository."""
    response = requests.get(repo_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        exit(1)

def process_commits(commits_requests):
    """Process the commit data and return a dictionary of commit counts by author."""
    commit_creator = {}
    for commit in commits_requests:
        if commit['author']:
            creator = commit['author']['login']
            commit_message = commit['commit']['message']
            
            if creator in commit_creator:
                commit_creator[creator]['count'] += 1
                commit_creator[creator]['messages'].append(commit_message)
            else:
                commit_creator[creator] = {'count': 1, 'messages': [commit_message]}
    
    return commit_creator

def display_commit_info(commit_creator):
    """Display the commit data."""
    print("\nPR creators and commit counts:")
    for creator, data in commit_creator.items():
        print(f'{creator}: {data["count"]} commits')
        print("Commit messages:")
        for msg in data["messages"]:
            print(f"- {msg}")
        print('-' * 50)

def main():
    """Main function to orchestrate the process."""
    # Define the URL of the public GitHub repository's commits endpoint
    repo_url = 'https://api.github.com/repos/kubernetes/kubernetes/commits'
    
    # Fetch commit data
    commits_requests = fetch_commits(repo_url)
    
    # Process the commit data
    commit_creator = process_commits(commits_requests)
    
    # Display the commit information
    display_commit_info(commit_creator)

if __name__ == "__main__":
    main()
