import os, subprocess, sys
from collections import OrderedDict
from cookiecutter.main import cookiecutter
from github import Github
from git import Repo

sys.path.insert(0, "{{ cookiecutter.project_root }}")
from common import utils


# context will be rendered in by cookiecutter at render time
context = {{cookiecutter}}

utils.install_dependencies(subprocess)

#  git stuff
local_repo = utils.initialize_local_repo(os, Repo, "initial commit")
remote_repo = utils.initialize_remote_repo(
    local_repo, Github, context["github_token"], context["project_slug"]
)
remote = utils.add_remote_to_local_repo(local_repo, remote_repo.ssh_url)
utils.push_to_remote(remote)
print("project available at: " + remote_repo.clone_url)
