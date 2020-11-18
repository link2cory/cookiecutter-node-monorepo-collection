def activate_gitignore(os):
    os.rename("gitignore", ".gitignore")


def initialize_local_repo(os, repo, initial_commit_msg):
    print("initializing local git repository")
    activate_gitignore(os)

    local_repo = repo.init(os.getcwd())
    local_repo.git.add(A=True)
    local_repo.index.commit(initial_commit_msg)
    print("done initializing local repository")
    return local_repo


def initialize_remote_repo(local_repo, remote, token, project_slug):
    local_repo, remote, token, project_slug
    print("initializing remote repository")
    remote_repo = create_remote_repo(remote, token, project_slug)
    return remote_repo


def create_remote_repo(remote, token, project_slug):
    print("creating remote repository")
    remote_repo = remote(token).get_user().create_repo(project_slug)
    print("successfully created remote repository")
    return remote_repo


def add_remote_to_local_repo(local_repo, remote_repo_url):
    return local_repo.create_remote("origin", remote_repo_url)


def push_to_remote(remote):
    remote.push(refspec="{}:{}".format("master", "master"))


def install_dependencies(subprocess):
    print("installing dependencies")
    subprocess.run(["yarn", "install"])
    print("finished installing dependencies")


def install_subpackage_dependencies(subprocess):
    print("installing dependencies")
    subprocess.run(["yarn", "lerna", "bootstrap"])
    print("finished installing dependencies")
