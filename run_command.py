import subprocess
import pathlib


class Command():
    def __init__(self, _command):
        self.command = _command

    def run(self, relative_path=""):

        package_path = (pathlib.Path().cwd() / relative_path)

        result = subprocess.run(
            self.command, capture_output=True, shell=True, cwd=package_path)
        if not result.stdout == "":
            print(result.stdout.decode(encoding="utf-8"))


