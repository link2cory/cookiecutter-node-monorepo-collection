import sys, subprocess

#  from collections import OrderedDict
#  from cookiecutter.main import cookiecutter
#  from github import Github
#  from git import Repo

sys.path.insert(0, "{{ cookiecutter.project_root }}")
from common import utils

utils.install_subpackage_dependencies(subprocess)
