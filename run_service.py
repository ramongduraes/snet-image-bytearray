#!/usr/bin/env python3

import pathlib
import subprocess
import os


def main():
    """
    Utility function to remove snetd ,db files and start snet daemon. The Daemon listens to the blockchain and starts
    the service when it receives a call.
    Could be substituted by simply running "snetd serve $(pwd)" from the root path of the service.
    """
    root_path = pathlib.Path(__file__).absolute().parent

    # Removing all previous snetd .db file
    os.system("rm snetd*.db")

    # Starting SNET Daemon
    start_snetd(root_path)


def start_snetd(cwd):
    """
    Starts SNET Daemon
    """
    cmd = ["snetd", "serve"]
    subprocess.Popen(cmd, cwd=str(cwd))
    return True


if __name__ == "__main__":
    main()
