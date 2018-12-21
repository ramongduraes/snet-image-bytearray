# Set Up a SingularityNET Session

> This tutorial assumes you have SNET CLI installed. If you don't please follow the [Install SNET](TODO) tutorial.

You may have noticed that after installing SNET Command Line Interface (CLI), if you try to run commands such as `snet organization list-services ORGANIZATION_ID` (that lists the services registered onto SingularityNET under a particular organization), it will tell you to create an identity: 

```
Please create your first identity by running 'snet identity create'.

The available identity types are:
    - 'rpc' (yields to a required ethereum json-rpc endpoint for signing using a given wallet
          index)
    - 'mnemonic' (uses a required bip39 mnemonic for HDWallet/account derivation and signing
          using a given wallet index)
    - 'key' (uses a required hex-encoded private key for signing)
    - 'ledger' (yields to a required ledger nano s device for signing using a given wallet
          index)
    - 'trezor' (yields to a required trezor device for signing using a given wallet index)
```

An identity 
- is a local alias for your private key.
- you can have several identities





account through which you'll be able to interact with the SingularityNET. 

it is necessary to create an identity so that you can call or publish your services onto the network.





To do that, you need to...

# STEP

## Metamask

Write something about the necessity of an account on Ethereum and how installing Metamask helps. Maybe make this a separate tutorial right before this one.

## Get AGI and ETH

You need some AGI and ETH tokens. 
> TODO: WHY???
> TODO: We're on Kovan, so everything is free

You can get them for free using your github account here:

- AGI: https://faucet.singularitynet.io/
- ETH: https://faucet.kovan.network/

## Create an Identity

From this point on, we follow the tutorial in the Docker container's prompt.

Create an "alias" for your private key.

'''
# snet identity create MY_ID_NAME KEY_TYPE
'''

Replace MY_ID_NAME by an id to identify your key in the SNET CLI. This id will not be seen by anyone. It's just a way to make it easier for you to refer to your private key (you may have many, btw) in following snet commands. This alias is kept locally in the container and will vanish when it's shutdown. KEY_TYPE can be either

key
rpc
mnemonic
ledger
trezor
In this tutorial we'll use KEY_TYPE == key. Enter your private key when prompted.

```bash
snet identity create ramon_snet key
```

It will prompt you for your private key. Again, don't worry! It is just about associating your private key with a local alias that is easy to use. Your identity ID will not be seen by anyone.

### RPC
### Mnemonic
### Key
### Ledger
### Trezor

## CREATE AN ORGANIZATION

> This step is optional if you're already part of an organization.




create an account = set up your snet session
after you've installed -> create an account -> identity -> organization -> 

Previous: [BLOCKCHAIN](TODO)

Next: [CALL SERVICE](TODO)