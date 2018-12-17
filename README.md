# Example Process Service

> This tutorial will guide you through the steps required to have a process-type service registered onto the SingularityNET. It assumes you have successfully installed all of SingularityNET components. To do that, refer to TODO: THIS TUTORIAL or simply run a docker container from the Dockerfile provided. If you choose to run a Docker container, make sure to expose a port so that SNET Daemon can communicate with the blockchain.

## Introduction

### Background

SingularityNET is... TODO

Whats a service??? TODO

As an AI service developer, you can expose your service to the SingularityNET by running an instance of SNET Daemon alongside it. The daemon interacts with the blockchain to facilitate authorization and payment for services and acts as a pass-through for making API calls to the service.  There are currently 3 ways by which the Daemon can communicate with a service:

- As an executable/process through stdin and stdout;
- Using JSON-RPC;
- Using gRPC.

This tutorial will guide you through integrating process-type services that receive their input from SNET Daemon via the standard input stream (`stdin`) and return their output via the standard output stream (`stdout`). 

### Tutorial Structure

The main steps of this tutorial are:

1) Create an executable code that takes and returns well-defined JSON data via stdin and stdout;
2) Publish it as an SNET service;
    - Write the `.proto` file;
    - Create the service metadata;
    - Write the Daemon configuration file;
    - Publish the service under your organization;
3) Call the service.

- Written in Python but could be any other language.
Example of an executable SNET service that communicates with the Daemon through stdin/stdout.

If you're already familiar with SingularityNET and how to create and publish a service that communicate with SNET Daemon through JSON-RPC or gRPC, you can skip to the [Summary](#summary) section.

## 1. Writing the code for your service

.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.


## 2. Publishing the service onto SingularityNET

## 3. Calling your service

## Summary

