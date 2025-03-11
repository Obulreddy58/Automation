import requests

url_commits = f'https://api.github.com/repos/kubernetes/kubernetes/commits'

response = requests.get(url_commits)

if response.status_code == 200:
    commits_requests = response.json()

    commit_creators = {}

    for commits in commits_requests:
        creator = commits['author']['login']
        if creator in commit_creators:
            commit_creators[creator] += 1
        else:
            commit_creators[creator] = 1

    print("PR creators and commits:")

    for creator, count in commit_creators.items():
        print(f'{creator} and {count}  commits')

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
