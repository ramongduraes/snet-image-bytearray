#!/usr/bin/env python3

import sys
import json
import logging

log = logging.getLogger("basic_template")
fh = logging.FileHandler('./service/executable_service.log')
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

    log.debug("Running service.")

    # Getting data from stdin
    # for line in sys.stdin:
    # while True:
    #    line = sys.stdin.readline()
    #    params = json.loads(line)
    method = sys.argv[1]
    log.debug("RECEIVED - Method: {}".format(method))

    if method == "add":
        log.debug("Method recognized.")
        input_args = ""
        with sys.stdin:
            for line in sys.stdin:
                input_args += line
            log.debug("STDIN: {}".format(input_args))
            params = json.loads(input_args)
            add_class = AdditionServicer()
            result = add_class.add(params)

            return_json = "{\n" + "    \"value\": {}\n".format(str(result)) + "}\n"
            sys.stdout.write(return_json)
            log.debug(return_json)
            #return_dict = dict()
            #return_dict["result"] = result
            #json_return = json.dumps(return_dict)
            #log.debug("Returns: {}".format(json_return))
            #sys.stdout.write("\'" + json_return + "\'")
        exit(0)
