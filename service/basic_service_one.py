#!/usr/bin/env python3

import sys
import json
import logging

log = logging.getLogger("basic_template")
fh = logging.FileHandler('executable_service.log')
formatter = logging.Formatter("%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
fh.setFormatter(formatter)
log.addHandler(fh)
log.setLevel(logging.DEBUG)
# formatter = logging.basicConfig(level=10, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")

"""
Simple arithmetic service to test the Snet Daemon (gRPC), dApp and/or Snet-CLI.
The user must provide the method (arithmetic operation) and
two numeric inputs: "a" and "b".
"""


class AdditionServicer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = 0
        # Just for debugging purpose.
        log.debug("AdditionServicer created")

    # The method that will be exposed to the snet-cli call command.
    # request: incoming data
    # context: object that provides RPC-specific information (timeout, etc).
    def add(self, arguments):
        # In our case, request is a Numbers() object (from .proto file)
        self.a = arguments["a"]
        self.b = arguments["b"]

        # To respond we need to create a Result() object (from .proto file)
        self.result = self.a + self.b

        log.debug("add({},{})={}".format(self.a, self.b, self.result))
        return self.result


if __name__ == "__main__":
    """
    Runs the gRPC server to communicate with the Snet Daemon.
    """
    log.debug("Running service.")
    for line in sys.stdin:
        log.debug("Input received: {}".format(line))
        params = json.loads(line)
        add_class = AdditionServicer()
        return_dict = dict()
        return_dict["result"] = add_class.add(params)
        json_return = json.dumps(return_dict)
        log.debug("Returns".format(json_return))
        sys.stdout.write(json_return)
        exit(0)
