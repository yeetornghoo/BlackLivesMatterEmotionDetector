import subprocess


def commit(commit_msg):
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", commit_msg])


def push(commit_msg):
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", commit_msg])
    subprocess.call(["git", "pull"])
    subprocess.call(["git", "push"])