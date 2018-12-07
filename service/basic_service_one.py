#!/usr/bin/env python3

import sys
import json
import logging

# Setting up a logger to log to a file.
# This is extra relevant in the case of a process-type service because since SNET Daemon captures everything that is
# printed to stdout
log = logging.getLogger("basic_template")
fh = logging.FileHandler('./service/executable_service.log')
formatter = logging.Formatter("%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
fh.setFormatter(formatter)
log.addHandler(fh)

log.setLevel(logging.DEBUG)


class AdditionServicer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = 0
        # Just for debugging purpose.
        log.debug("AdditionServicer created")

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
    method = sys.argv[1]
    log.debug("RECEIVED - Method: {}".format(method))

    if method == "add":
        log.debug("Method recognized.")

        # Read input parameters from stdin
        with sys.stdin:
            input_args = ""
            for line in sys.stdin:
                input_args += line
            log.debug("STDIN: {}".format(input_args))
            params = json.loads(input_args)  # Converts from string to python dict

            add_class = AdditionServicer()
            result = add_class.add(params)

            return_dict = dict()
            return_dict["value"] = result
            json_return = json.dumps(return_dict)
            log.debug("STDOUT: {}".format(json_return))
            sys.stdout.write(json_return)
        exit(0)
