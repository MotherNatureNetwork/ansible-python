testinfra_hosts = ["mnn.python-01"]


def test_python_installed(Command):
    cmd = Command("python --version")

    assert '2.7.12' in cmd.stderr
