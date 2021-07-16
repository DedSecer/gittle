from gittle3 import Gittle

from config import repo_path, repo_url, key_file

# Gittle repo
g = Gittle(repo_path, origin_uri=repo_url)

# Authentication
g.auth(pkey=key_file)

# Do push
g.push()
