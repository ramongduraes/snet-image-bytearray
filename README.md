# Example Process Service

> This tutorial will guide you through all the steps required to have a "process" type service registered onto the SingularityNET.

## Introduction

An AI service developer exposes their service to the network by running the SNET Daemon alongside their service. The SNET Daemon interacts with the blockchain to facilitate authorization and payment for services and acts as a passthrough for making API calls to the service.

There are currently 3 ways the Daemon can communicate with a service can communicate with 

This tutorial assumes you have successfully installed all of SingularityNET components. To do that, refer to THIS TUTORIAL or simply run a docker container from the Dockerfile provided. If you choose to run a Docker container, make sure to expose a port so that SNET Daemon can comunicate with the blockchain.

1) Create an executable code that takes and returns well-defined JSON data via stdin and stdout;
2) Publish it as an SNET service;
    - Write the .proto file;
    - Create the service metadata;
    - Write the Daemon configuration file;
    - Publish the service under your organization;
3) Call the service.



- Written in Python but could be any other language.
Example of an executable SNET service that communicates with the Daemon through stdin/stdout.




### 1. Write the code for your service

