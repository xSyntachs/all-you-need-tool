import requests

def get_latest_version(user, repo):
    response = requests.get(f'https://api.github.com/repos/{user}/{repo}/tags')
    data = response.json()
    if data:
        return data[0]['name']  # Der neueste Tag ist der erste in der Liste
    else:
        return None

user = 'xSyntachs'
repo = 'all-you-need-tool'
latest_version = get_latest_version(user, repo)
if latest_version:
    print(f'Die neueste Version von {user}/{repo} ist {latest_version}.')
else:
    print(f'Es gibt keine Tags oder Releases für {user}/{repo}.')
