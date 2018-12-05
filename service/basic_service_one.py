#!/usr/bin/env python3

import sys
import json
import logging

logging.basicConfig(level=10, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
log = logging.getLogger("basic_template")


"""
Simple arithmetic service to test the Snet Daemon (gRPC), dApp and/or Snet-CLI.
The user must provide the method (arithmetic operation) and
two numeric inputs: "a" and "b".

e.g:
With dApp:  'method': mul
            'params': {"a": 12.0, "b": 77.0}
Resulting:  response:
                value: 924.0


Full snet-cli cmd:
$ snet client call mul '{"a":12.0, "b":77.0}'

Result:
(Transaction info)
Signing job...

Read call params from cmdline...

Calling service...

    response:
        value: 924.0
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
    print("Running service.")
    for line in sys.stdin:
        print("Received: {}".format(line))
        params = json.loads(line)
        add_class = AdditionServicer()
        return_dict = dict()
        return_dict["result"] = add_class.add(params)
        json_return = json.dumps(return_dict)
        sys.stdout.write(json_return)
        exit(0)
