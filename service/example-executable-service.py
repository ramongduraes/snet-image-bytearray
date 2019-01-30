#!/usr/bin/env python3

import sys
import json
import logging

# Setting up a logger to log to a file.
# This is extra relevant in the case of a process-type service because SNET Daemon captures everything that is printed
# to stdout. If anything other than the json it expects is printed, a parsing error will be raised.
log = logging.getLogger("basic_template")
file_handler = logging.FileHandler('executable_service.log')
formatter = logging.Formatter("%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
log.setLevel(logging.DEBUG)


if __name__ == "__main__":
    log.debug("Running service.")

    # Read the method defined in the .proto file from argv.
    method = sys.argv[1]
    log.debug("RECEIVED - Method: {}".format(method))

    if method == "add":
        # Read input parameters from stdin
        with sys.stdin:
            input_args = ""
            for line in sys.stdin:
                log.debug("RECEIVED - Stdin: {}". format(line))
                input_args += line
        params = json.loads(input_args)  # Converts from string to python dict
        log.debug("STDIN: {}".format(input_args))

        # Add arguments
        result = params["a"] + params["b"]  # Dictionary key names must match the specifications in .proto.

        # Build the resulting json from a dictionary
        return_dict = dict()
        return_dict["value"] = result  # Dictionary key names must match the specifications in .proto.
        json_return = json.dumps(return_dict)

        # Return the resulting json and exit
        sys.stdout.write(json_return)
        log.debug("STDOUT: {}".format(json_return))
        exit(0)

    else:
        # This condition will never happen because snet-cli won't allow methods unknown to it (i.e. not in .proto file).
        exit(1)
