# Install SingularityNET

> SNET-Daemon v0.1.4 | SNET-CLI v0.1.9

> This tutorial will guide you through the steps required to have working versions of all of SingularityNET components so that you can either publish your own AI/machine learning service onto the platform or use someone else's service through SNET's Command Line Interface (CLI). 

> The tutorial was created for (and tested in) Ubuntu 18.04 but should probably work for other versions as well. The steps in this tutorial will be put into a Docker image to provide a working environment out of the box. If you do choose to run a Docker container, make sure to expose a port to your service's Daemon so that it can communicate with the blockchain.


## Introduction

SingularityNET is an open-source protocol and collection of smart contracts for a decentralized market of coordinated AI services. Within this framework, anyone can add an AI/machine learning service to SingularityNET for use by the network, and receive network payment tokens in exchange.

For an AI/machine learning service developer to expose their service onto the SingularityNET, it is necessary to run an instance of **SNET Daemon** alongside it. The Daemon interacts with the blockchain to facilitate authorization and payment for services and acts as a pass-through for making API calls to the service.

Published services are then listed at **SNET Registry**: open and uncensorable registry of organizations and services that are accessible to anyone within the SingularityNET Network. Services can hence be called by users, or by other services, through **SNET's Command Line Interface (SNET-cli)** - and will soon be available at **SNET DApp**: the marketplace for buying and selling AI.

This tutorial will guide you through installing SNET Daemon and SNET CLI. 

## Install SNET Daemon
> If you run the following scripts in your system make sure to grant super user access to the commands.

```bash
# Install SNET Daemon dependencies
apt-get update
apt-get install -y git wget

# Set up directories
export SINGNET_REPOS=/opt/singnet
mkdir -p ${SINGNET_REPOS} && \
cd ${SINGNET_REPOS}

# Install SNET Daemon
mkdir snet-daemon && \
cd snet-daemon && \
wget -q https://github.com/singnet/snet-daemon/releases/download/v0.1.4/snetd-0.1.4.tar.gz && \
tar -xvf snetd-0.1.4.tar.gz && \
mv ./snetd-0.1.4/snetd-linux-amd64 /usr/bin/snetd
```

Because no daemon configuration file was provided, running `snetd` on your terminal should return:

<details>
  <summary> 
    stuff with *mark* **down**
  </summary>
  <p>
<!-- the above p cannot start right at the beginning of the line and is mandatory for everything else to work -->

## *formatted* **heading** with [a](link)

```java
code block
```
</p></details>

```bash
INFO[0000] Cobra initialized                            
INFO[0000] Configuration file is not set, using default configuration 
INFO[0000]                                               PaymentChannelStorageServer="&{ID:storage-1 Scheme:http Host:127.0.0.1 ClientPort:2379 PeerPort:2380 Token:unique-token Cluster:storage-1=http://127.0.0.1:2380 StartupTimeout:1m0s Enabled:true DataDir:storage-data-dir-1.etcd LogLevel:info}"
INFO[0000]                                               PaymentChannelStorageServer="&{ID:storage-1 Scheme:http Host:127.0.0.1 ClientPort:2379 PeerPort:2380 Token:unique-token Cluster:storage-1=http://127.0.0.1:2380 StartupTimeout:1m0s Enabled:true DataDir:storage-data-dir-1.etcd LogLevel:info}"
INFO[0000]                                               ClientURL="http://127.0.0.1:2379"
INFO[0000]                                               PeerURL="http://127.0.0.1:2380"
2018-12-18 18:38:54.293446 I | embed: listening for peers on http://127.0.0.1:2380
2018-12-18 18:38:54.293538 I | embed: listening for client requests on 127.0.0.1:2379
2018-12-18 18:38:54.297152 I | etcdserver: name = storage-1
2018-12-18 18:38:54.297175 I | etcdserver: data dir = storage-data-dir-1.etcd
2018-12-18 18:38:54.297196 I | etcdserver: member dir = storage-data-dir-1.etcd/member
2018-12-18 18:38:54.297217 I | etcdserver: heartbeat = 100ms
2018-12-18 18:38:54.297235 I | etcdserver: election = 1000ms
2018-12-18 18:38:54.297252 I | etcdserver: snapshot count = 100000
2018-12-18 18:38:54.297273 I | etcdserver: advertise client URLs = http://127.0.0.1:2379
2018-12-18 18:38:54.297290 I | etcdserver: initial advertise peer URLs = http://127.0.0.1:2380
2018-12-18 18:38:54.297314 I | etcdserver: initial cluster = storage-1=http://127.0.0.1:2380
2018-12-18 18:38:54.301823 I | etcdserver: starting member 1c8a507c0cf9f246 in cluster c4a01860a4e6dcdb
2018-12-18 18:38:54.301858 I | raft: 1c8a507c0cf9f246 became follower at term 0
2018-12-18 18:38:54.301882 I | raft: newRaft 1c8a507c0cf9f246 [peers: [], term: 0, commit: 0, applied: 0, lastindex: 0, lastterm: 0]
2018-12-18 18:38:54.301901 I | raft: 1c8a507c0cf9f246 became follower at term 1
2018-12-18 18:38:54.307087 W | auth: simple token is not cryptographically signed
2018-12-18 18:38:54.310004 I | etcdserver: starting server... [version: 3.3.10, cluster version: to_be_decided]
2018-12-18 18:38:54.310500 I | etcdserver: 1c8a507c0cf9f246 as single-node; fast-forwarding 9 ticks (election ticks 10)
2018-12-18 18:38:54.311179 I | etcdserver/membership: added member 1c8a507c0cf9f246 [http://127.0.0.1:2380] to cluster c4a01860a4e6dcdb
2018-12-18 18:38:55.202325 I | raft: 1c8a507c0cf9f246 is starting a new election at term 1
2018-12-18 18:38:55.202373 I | raft: 1c8a507c0cf9f246 became candidate at term 2
2018-12-18 18:38:55.202399 I | raft: 1c8a507c0cf9f246 received MsgVoteResp from 1c8a507c0cf9f246 at term 2
2018-12-18 18:38:55.202440 I | raft: 1c8a507c0cf9f246 became leader at term 2
2018-12-18 18:38:55.202466 I | raft: raft.node: 1c8a507c0cf9f246 elected leader 1c8a507c0cf9f246 at term 2
2018-12-18 18:38:55.202732 I | etcdserver: setting up the initial cluster version to 3.3
2018-12-18 18:38:55.203618 N | etcdserver/membership: set the initial cluster version to 3.3
2018-12-18 18:38:55.203678 I | etcdserver/api: enabled capabilities for version 3.3
2018-12-18 18:38:55.203734 I | etcdserver: published {Name:storage-1 ClientURLs:[http://127.0.0.1:2379]} to cluster c4a01860a4e6dcdb
2018-12-18 18:38:55.203829 I | embed: ready to serve client requests
2018-12-18 18:38:55.204862 N | embed: serving insecure client requests on 127.0.0.1:2379, this is strongly discouraged!
2018-12-18 18:38:55.209077 I | etcdserver: skipped leadership transfer for single member cluster
panic: (*logrus.Entry) (0x130df40,0xc4204221e0)

goroutine 1 [running]:
github.com/singnet/snet-daemon/vendor/github.com/sirupsen/logrus.Entry.log(0xc4200aa3c0, 0xc420982720, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/root/singnet/src/github.com/singnet/snet-daemon/vendor/github.com/sirupsen/logrus/entry.go:126 +0x2d2
github.com/singnet/snet-daemon/vendor/github.com/sirupsen/logrus.(*Entry).Panic(0xc420422190, 0xc4200174e8, 0x1, 0x1)
	/root/singnet/src/github.com/singnet/snet-daemon/vendor/github.com/sirupsen/logrus/entry.go:194 +0xaa
github.com/singnet/snet-daemon/blockchain.getMetaDataUrifromRegistry(0x0, 0x0, 0x0)
	/root/singnet/src/github.com/singnet/snet-daemon/blockchain/serviceMetadata.go:98 +0x578
github.com/singnet/snet-daemon/blockchain.ServiceMetaData(0xc4200e0cb0)
	/root/singnet/src/github.com/singnet/snet-daemon/blockchain/serviceMetadata.go:55 +0x4c
github.com/singnet/snet-daemon/snetd/cmd.(*Components).ServiceMetaData(0xc4201d93e0, 0xc4200e0cb0)
	/root/singnet/src/github.com/singnet/snet-daemon/snetd/cmd/components.go:98 +0x2f
github.com/singnet/snet-daemon/snetd/cmd.(*Components).Blockchain(0xc4201d93e0, 0xf)
	/root/singnet/src/github.com/singnet/snet-daemon/snetd/cmd/components.go:85 +0x81
github.com/singnet/snet-daemon/snetd/cmd.newDaemon(0xc4201d93e0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, ...)
	/root/singnet/src/github.com/singnet/snet-daemon/snetd/cmd/serve.go:112 +0x2ed
github.com/singnet/snet-daemon/snetd/cmd.glob..func3(0x1f21340, 0x1fa7ac0, 0x0, 0x0)
	/root/singnet/src/github.com/singnet/snet-daemon/snetd/cmd/serve.go:55 +0x149
github.com/singnet/snet-daemon/snetd/cmd.glob..func2(0x1f21340, 0x1fa7ac0, 0x0, 0x0)
	/root/singnet/src/github.com/singnet/snet-daemon/snetd/cmd/flags.go:39 +0x9b
github.com/singnet/snet-daemon/vendor/github.com/spf13/cobra.(*Command).execute(0x1f21340, 0xc4200301b0, 0x0, 0x0, 0x1f21340, 0xc4200301b0)
	/root/singnet/src/github.com/singnet/snet-daemon/vendor/github.com/spf13/cobra/command.go:766 +0x2c1
github.com/singnet/snet-daemon/vendor/github.com/spf13/cobra.(*Command).ExecuteC(0x1f21340, 0xc4204a7f78, 0x406aec, 0xc42009a058)
	/root/singnet/src/github.com/singnet/snet-daemon/vendor/github.com/spf13/cobra/command.go:852 +0x30a
github.com/singnet/snet-daemon/vendor/github.com/spf13/cobra.(*Command).Execute(0x1f21340, 0x0, 0x0)
	/root/singnet/src/github.com/singnet/snet-daemon/vendor/github.com/spf13/cobra/command.go:800 +0x2b
main.main()
	/root/singnet/src/github.com/singnet/snet-daemon/snetd/main.go:10 +0x31
```

Notice that if you're only interested in publishing a service (i.e. in a Docker container), installing SNET Daemon should be enough.

Refer to [SNET-Daemon](https://github.com/singnet/snet-daemon) for further information including a list of available commands.

## Install SNET CLI

Installing SNET CLI requires installing Python3 and specific versions of some of its packages. Since different projects usually share several packages, it is a good practice to set up virtual environments to isolate new projects. Doing that guarantees that the versions of SNET-CLI's required packages don't override already existing ones and that new projects dont break your current installation of SNET-CLI.

Several tools can be used to create a virtual environment for Python, a very popular example being [Anaconda](TODO). If you have already installed Anaconda, you can create a new environment (e.g. named `singnet`) by running `conda create -n singnet python=3.6`. You can then activate the environment (in Linux and macOS) using `source activate anaconda` and deactivate it by using `source deactivate`.

If all you want is to have a minimal installation of SNET-CLI Since many of our service deployments are made inside [Docker](TODO) containers, minimal installations 

Here, however, we'll use Python's package `virtualenv` to ensure minimal installations. 

### Install Python 3

There are a few things to keep in mind at this step:

- The Python installation commands used in the script are only guaranteed to work for Ubuntu 18.04;
- Python3 usually comes pre-installed as default Python interpreter for Ubuntu 18.04 desktop and server, however if you're running minimal installations (e.g. a Docker container) it will need to be installed manually;
- If you have other versions of Python installed in your system, you'll need to make sure that SNET-CLI is using Python3 >= 3.6.5. 

```bash
# Install Python >= 3.6.5
apt-get install -y \
        python3 \
        python3-pip
```

### Create a Virtual Environment




<!-- TODO: Nodejs and NPM probably only if you're not installing via pip. Change once `pip3 install snet-cli` works properly.-->
- libudev
- libusb 1.0
- nodejs
- npm
- Python3
- pip


```bash
# Blockchain script's return:
/opt/singnet/snet-cli/blockchain
+-- singularitynet-platform-contracts@0.2.5 
| `-- openzeppelin-solidity@1.11.0 
`-- singularitynet-token-contracts@2.0.0 
  `-- zeppelin-solidity@1.4.0 

npm WARN blockchain No description
npm WARN blockchain No repository field.
npm WARN blockchain No license field.
```

The script below will install SNET-CLI and all of its requirements:

```bash
# Install nodejs npm
apt-get install -y nodejs npm

# Install other dependencies
apt-get install -y \
        libudev-dev \
        libusb-1.0-0-dev

# Install snet-cli
cd ${SINGNET_REPOS} && \
git clone https://github.com/singnet/snet-cli && \
cd snet-cli
./scripts/blockchain install
pip3 install -e .
```

The `snet` command should now be available at your terminal!

<!---
You may now install snet-cli via pip3:

```bash
pip3 install snet-cli
```
-->

Refer to [SNET-CLI](https://github.com/singnet/snet-cli) for further information, including a list of available commands.

## Summary



## Conclusion

You now have a working SingularityNET environment! The commands listed here were condensed into a [bash script](TODO) as well as a [Dockerfile](TODO).

Next: [Set up a session]()
___________________

## FAQ: Install SNET-CLI 

1. Running `./scripts/blockchain install` should return. If you encounter a different error message at this step, make sure that the `blockchain` script is actually using Python3.6 (even Python3.5 will cause an error). You can do that by specifying the Python version on the shebang bash (the first line) of the script, changing it from `#!/usr/bin/env python3` to `#!/usr/bin/env python3.6`.
