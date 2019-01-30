# Example Process Service

> This tutorial will guide you through the steps required to have a process-type service registered onto the SingularityNET. It assumes you have successfully installed all of SingularityNET components. To do that, refer to TODO: THIS TUTORIAL or simply run a docker container from the Dockerfile provided. If you choose to run a Docker container, make sure to expose a port so that SNET Daemon can communicate with the blockchain.

## Introduction

SingularityNET is an open-source protocol and collection of smart contracts for a decentralized market of coordinated AI services. Within this framework, anyone can add an AI/machine learning service to SingularityNET for use by the network, and receive network payment tokens in exchange.

As an AI/machine learning service developer, you can expose your service to the SingularityNET by running an instance of SNET Daemon alongside it. The Daemon interacts with the blockchain to facilitate authorization and payment for services and acts as a pass-through for making API calls to the service.  There are currently 3 ways by which the Daemon can communicate with a service:

- Through stdin/stdout as an executable/process;
- Through JSON-RPC;
- Through gRPC.

This tutorial will guide you through integrating process-type services that receive their input from SNET Daemon via the standard input stream (`stdin`) and return their output via the standard output stream (`stdout`). If you're already familiar with SingularityNET and know how to create, publish and call a service that communicates with SNET Daemon through JSON-RPC or gRPC, you can skip to the [Summary](#summary) section.

### Tutorial Structure

The main steps of this tutorial are:

1) [Write the code for your service](#1-writing-the-code-for-your-service) taking and returning well-defined JSON data via stdin and stdout;
2) [Publish it as an SNET service](#2-publishing-the-service-onto-singularitynet):
    - Create the service model (protobuf file);
    - Create the service metadata;
    - Write the Daemon configuration file;
    - Publish the service under your organization;
3) [Call the service](#3-calling-your-service).


## 1. Writing the code for your service

For this tutorial we'll write an example executable service in [Python](https://www.python.org/) but this approach can be applied to other programming languages as well.

To keep the directory structure of the services and follow the standard file paths, we'll create the following directories: 

```bash
mkdir -p example-executable-service/service/service_spec && \
cd example-executable-service/service
```

Inside the service folder, create a file for the main code of your service (in our case, `example-executable-service.py`). For demonstration purposes, we'll create a very simple service that adds two numbers. Here's the Python code for it, have a look at the code and its comments.

```python
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

```

To test this code locally, you can run `./example-executable-service.py add <<< '{"a": 2.1, "b":6.7}'`, and it should return `{"value": 8.8}`. 

The main things to notice here are:
- The service method ("add", in this case) will be received through `argv[1]` while the remaining parameters will be received through stdin;
- Once your code is ready, avoid printing any debug or status messages since they'll be sent to `stdout`, where SNET Daemon awaits the JSON-encoded return data;
- Since this code will be interpreted as executable, you need to tell your operating system what interpreter to use by adding the shebang `#!/usr/bin/env python3`, for Python3, or an equivalent for your programming language of choice.

## 2. Publishing the service onto SingularityNET

### Specify the service model

The first step towards publishing your service onto SingularityNET is specifying a service model. We do that through a [protobuf](https://developers.google.com/protocol-buffers/docs/overview) file, in which we define `services` (or methods) and `messages` that are received or sent by those services. By default, the `.proto` file is stored inside the `service/service_spec` folder. Here's the protobuf file for our example executable service:

```bash
syntax = "proto3";

message Numbers {
    float a = 1;
    float b = 2;
}

message Result {
    float value = 1;
}

service Addition {
    rpc add(Numbers) returns (Result) {}
}
```

You may copy this code into a `example-executable-service.proto` file inside `example-executable-service/service/service_spec`. This is a very simple example of a protobuf file, if you're writing a more complex service, you may use several variable types and define more messages and services. Learn more about protobuf syntax [here](https://developers.google.com/protocol-buffers/docs/proto3).



### Create the service metadata

```bash
snet service metadata-init service/service_spec example-executable-service 0xD416d832F6AE2Ca7d9C7C05f9255Ab49b70c0fe4 --endpoints http://54.203.198.53:7018 --service-type process --encoding json --fixed-price 0
```

### Write the Daemon configuration file

GIVE EXAMPLES FOR BOTH ROPSTEN AND KOVAN
```bash
{
   "DAEMON_END_POINT": "http://IP:PORT",
   "ETHEREUM_JSON_RPC_ENDPOINT": "https://kovan.infura.io",
   "IPFS_END_POINT": "http://ipfs.singularitynet.io:80",
   "REGISTRY_ADDRESS_KEY": "REGISTRY_ADDRESS",
   "PASSTHROUGH_ENABLED": true,
   "EXECUTABLE_PATH": "EXECUTABLE_PATH",
   "ORGANIZATION_ID": "ORG_ID",
   "SERVICE_ID": "SERVICE_ID",
   "PAYMENT_CHANNEL_STORAGE_SERVER": {
       "DATA_DIR": "/opt/singnet/etcd/"
   },
   "LOG": {
       "LEVEL": "debug",
       "OUTPUT": {
              "TYPE": "stdout"
           }
   }
}
```

```bash
{
   "DAEMON_END_POINT": "http://54.203.198.53:7018",
   "ETHEREUM_JSON_RPC_ENDPOINT": "https://kovan.infura.io",
   "IPFS_END_POINT": "http://ipfs.singularitynet.io:80",
   "REGISTRY_ADDRESS_KEY": "0xe331bf20044a5b24c1a744abc90c1fd711d2c08d",
   "PASSTHROUGH_ENABLED": true,
   "EXECUTABLE_PATH": "./service/example-executable-service.py",
   "ORGANIZATION_ID": "ramonduraes",
   "SERVICE_ID": "example-executable-service",
   "PAYMENT_CHANNEL_STORAGE_SERVER": {
       "DATA_DIR": "/opt/singnet/etcd/"
   },
   "LOG": {
       "LEVEL": "debug",
       "OUTPUT": {
              "TYPE": "stdout"
           }
   }
}
```


### Publish the service under your organization

Refer to the [Setting up a Session](TODO) tutorial to learn how to create an organization.

```bash
snet service publish snet example-executable-service
```

## 3. Calling your service

## Summary

In service_metadata.json:

--service-type process --encoding json

In snetd.config.json:

"EXECUTABLE_PATH": "./service/example-executable-service.py" 

Make sure to add the shebang to your code

## Conclusion
