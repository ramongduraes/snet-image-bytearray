# Install SingularityNET

> SNET-Daemon v0.1.4 | SNET-CLI v0.1.9

> This tutorial will guide you through the steps required to have working versions of all of SingularityNET components so that you can either publish your own AI/machine learning service onto the platform or use someone else's service through SNET's Command Line Interface (CLI). 

## Introduction

SingularityNET is an open-source protocol and collection of smart contracts for a decentralized market of coordinated AI services. Within this framework, anyone can add an AI/machine learning service to SingularityNET for use by the network, and receive network payment tokens in exchange.

For an AI/machine learning service developer to expose their service onto the SingularityNET, it is necessary to run an instance of **SNET Daemon** alongside it. The Daemon interacts with the blockchain to facilitate authorization and payment for services and acts as a pass-through for making API calls to the service.

Published services are then listed at **SNET Registry**: open and uncensorable registry of organizations and services that are accessible to anyone within the SingularityNET Network. Services can hence be called by users, or by other services, through **SNET's Command Line Interface (SNET-cli)** - and will soon be available at **SNET DApp**: the marketplace for buying and selling AI.

This tutorial will guide you through installing SNET Daemon and SNET CLI. 

## SNET Daemon
> If you run the following scripts inside a docker container, please remove the `sudo` commands or install it by running `apt-get install sudo`.

SNET Daemon is available as pre-compiled binaries for Linux and macOS at [Github](https://github.com/singnet/snet-daemon/releases/). The script below installs a few dependencies, downloads SNET Daemon, moves it to the user's bin folder and cleans up.

```bash
# Install SNET Daemon dependencies
sudo apt-get update
sudo apt-get install -y wget

# Install SNET Daemon
sudo mkdir snet-daemon && \
cd snet-daemon && \
sudo wget -q https://github.com/singnet/snet-daemon/releases/download/v0.1.4/snetd-0.1.4.tar.gz && \
sudo tar -xvf snetd-0.1.4.tar.gz && \
sudo mv ./snetd-0.1.4/snetd-linux-amd64 /usr/bin/snetd

# Delete folder and downloaded files
cd ..
sudo rm -rf snet-daemon
```

That's it for the daemon installation! Because no daemon configuration file was provided, running `snetd` on your terminal should return:

<details>
  <summary> 
    Click to expand!
  </summary>
  <p>
  
```
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
</p></details>

Notice that if you're only interested in publishing a service (i.e. in a Docker container), installing SNET Daemon should be enough.

Refer to [SNET-Daemon](https://github.com/singnet/snet-daemon) for further information including a list of available commands.

## SNET CLI

Here are the main requirements for installing SNET CLI:
<!-- TODO: Nodejs and NPM probably only if you're not installing via pip. Change once `pip3 install snet-cli` works properly.-->

- libudev
- libusb 1.0
- nodejs
- npm
- Python3
- pip

Installing SNET CLI requires installing Python3 and specific versions of some of its packages. Since different projects usually share several packages, it is a good practice to set up virtual environments to isolate new projects. Doing that guarantees that the versions of SNET CLI's required packages don't override already existing ones and that new projects dont break your current installation of SNET CLI.

Several tools can be used to create a virtual environment for Python, a very popular example being [Anaconda](TODO). If you already have Anaconda installed, you can create a new environment (e.g. named `snet`) by running `conda create -n snet python=3.6`. You can then activate the environment (in Linux and macOS) using `source activate snet` and deactivate it by using `source deactivate`. Skip to [SNET CLI installation instructions](#install-snet-cli).

However, if all you want is to have a minimal installation of SNET CLI - as we do for services deployed inside [Docker](TODO) containers, you can simply instal Python3 and use its `virtualenv` package as shown in the steps below.

### Install General Dependencies

The script below will also install a few of SNET CLI dependencies.

```bash
# Install SNET CLI dependencies
sudo apt-get install -y \
    git \
    libudev-dev \
    libusb-1.0-0-dev \
    nodejs \
    npm
```

### Install Python 3

There are a few things to keep in mind at this step:

- The Python installation commands used in the script are only guaranteed to work for Ubuntu 18.04;
- Python3 usually comes pre-installed as default Python interpreter for Ubuntu 18.04 desktop and server, however if you're running minimal installations (e.g. a Docker container) it will need to be installed manually;
- If you have other versions of Python installed in your system, make sure that SNET CLI is using Python3 >= 3.6.5. 

```bash
# Install Python >= 3.6.5
sudo apt-get install -y \
    python3 \
    python3-pip
```

### Create a Virtual Environment

Here, we'll install `virtualenv`, create and activate a virtual environment named `snet` inside `~/Workspaces` and call that directory `SNET_DIR`.

```bash
# Install virtualenv and create one
pip3 install virtualenv && \
cd ~ && \
mkdir Workspaces && \
cd Workspaces && \
sudo virtualenv snet && \
source snet/bin/activate

export SNET_DIR=~/Workspaces/snet
```

Notice that the name of the environment will appear between parentheses at the beginning of your command line. To deactivate the environment, simply type `deactivate`.

### Install SNET CLI

<!---
You may now install snet-cli via pip3:

```bash
pip3 install snet-cli
```
-->

You may now install SNET CLI through `pip` as a developer package by running:

```bash
# Install snet-cli
cd ${SNET_DIR} && \
git clone https://github.com/singnet/snet-cli && \
cd snet-cli && \
./scripts/blockchain install && \
pip3 install -e .
```

The `snet` command should now be available at your terminal! 

<details>
  <summary> 
    If you have other versions of Python3 installed and have not created a virtual environment for SNET CLI, a problem may occur while running `./scripts/blockchain install`. Click here to see how to fix it.
  </summary>
  <p>
  
  While running `./scripts/blockchain install`, make sure it returns:
  
```
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

If it doesn't, it may be the case that the `blockchain` script is using an inadequate version os Python. Fix it by specifying the Python version on the shebang bash (the first line) of the script, changing it from `#!/usr/bin/env python3` to `#!/usr/bin/env python3.6`.

</p></details>

Refer to [SNET-CLI](https://github.com/singnet/snet-cli) for further information, including a list of available commands.

## Docker Container Installation Script:

Here's a quick script to install both SNET Daemon and SNET CLI inside a docker container. 

```bash
# Update
apt-get update 

# Install SNET Daemon and its dependencies
apt-get install -y wget && \
mkdir snet-daemon && \
cd snet-daemon && \
wget -q https://github.com/singnet/snet-daemon/releases/download/v0.1.4/snetd-0.1.4.tar.gz && \
tar -xvf snetd-0.1.4.tar.gz && \
mv ./snetd-0.1.4/snetd-linux-amd64 /usr/bin/snetd && \
cd .. && \
rm -rf snet-daemon

# Install SNET CLI dependencies and Python3.6
apt-get install -y \
    git \
    libudev-dev \
    libusb-1.0-0-dev \
    nodejs \
    npm \
    python3 \
    python3-pip
       
# Install snet-cli
cd /opt && \
git clone https://github.com/singnet/snet-cli && \
cd snet-cli && \
./scripts/blockchain install && \
pip3 install -e .
```

## Conclusion

You now have a working SingularityNET environment! The commands listed here were condensed into a [bash script](TODO) as well as a [Dockerfile](TODO).

Next: [Set up a session](TODO)

## Uninstall 

To uninstall SNET Daemon, simply delete its precompiled binary by running `rm /usr/bin/snetd`. SNET CLI may be uninstalled via pip (make sure your virtual environment is active) by running `pip3 uninstall snet-cli`. 

<!-- 
TODO: change this once SNET CLI pip is working
-->

<details>
  <summary> 
    Click here if you run into the message "Can't uninstall 'snet-cli'. No files were found to uninstall.".
  </summary>
  <p>
  This error may occur due to SNET CLI being installed in "editable mode". It also means you probably haven't set up a virtual environment for SNET components or something has gone wrong when using it. 
  
  You can uninstall SNET CLI by navigating to its folder (i.e. `snet-cli`, obtained via `git clone`) and running `sudo rm -r $(find . -name '*.egg-info')`. Remove its binaries by running `sudo rm $(which) snet`.
  
</p></details>

To clean up your machine (i.e. delete all of SNET files and its virtual environment), run:

```bash
# Clean up (remove virtual environment and snet-cli files)
deactivate || \
cd ${SNET_DIR} && \
cd .. && \
rm -rf snet && \
unset SNET_DIR
```

That's it!

___

NEXT: [SET UP A SESSION](TODO)
