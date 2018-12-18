# Example Process Service

> This tutorial will guide you through the steps required to have a process-type service registered onto the SingularityNET. It assumes you have successfully installed all of SingularityNET components. To do that, refer to TODO: THIS TUTORIAL or simply run a docker container from the Dockerfile provided. If you choose to run a Docker container, make sure to expose a port so that SNET Daemon can communicate with the blockchain.

## Introduction

SingularityNET is an open-source protocol and collection of smart contracts for a decentralized market of coordinated AI services. Within this framework, anyone can add an AI/machine learning service to SingularityNET for use by the network, and receive network payment tokens in exchange.

As an AI/machine learning service developer, you can expose your service to the SingularityNET by running an instance of SNET Daemon alongside it. The Daemon interacts with the blockchain to facilitate authorization and payment for services and acts as a pass-through for making API calls to the service.  There are currently 3 ways by which the Daemon can communicate with a service:

- As an executable/process through stdin and stdout;
- Using JSON-RPC;
- Using gRPC.

This tutorial will guide you through integrating process-type services that receive their input from SNET Daemon via the standard input stream (`stdin`) and return their output via the standard output stream (`stdout`). 

### Tutorial Structure

The main steps of this tutorial are:

1) [Create an executable code](#1-writing-the-code-for-your-service) that takes and returns well-defined JSON data via stdin and stdout;
2) [Publish it as an SNET service](#2-publishing-the-service-onto-singularitynet);
    - Write the protobuf file;
    - Create the service metadata;
    - Write the Daemon configuration file;
    - Publish the service under your organization;
3) [Call the service](#3-calling-your-service).

If you're already familiar with SingularityNET and know how to create, publish and call a service that communicates with SNET Daemon through JSON-RPC or gRPC, you can skip to the [Summary](#summary) section.

## 1. Writing the code for your service

For this tutorial we'll write an example executable service in [Python](https://www.python.org/) but this approach can be applied to the other programming languages as well.

First, create a directory for your service directory you want to create your service in, create a `service` subdirectory by running

```bash
mkdir example_executable_service
cd executable_service
mkdir service
cd service
nano example_executable_service.py
```








## 2. Publishing the service onto SingularityNET



## 3. Calling your service

## Summary

## Conclusion
