def callback(commit):
    if commit.author_name == b"mayu200" or commit.committer_name == b"mayu200":
        commit.skip()
