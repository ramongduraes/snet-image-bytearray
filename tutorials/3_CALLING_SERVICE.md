# Calling a Service Through SNET CLI

> This tutorial assumes you have successfully [installed](TODO) and [set up](TODO) SNET CLI.

Calling an AI service will mostly be done through our soon to be released [SNET DApp](TODO): a marketplace for exploring available AI services and interacting with them through a web-UI. However, if you're an AI developer interested in publishing a service, you should probably know how to call it through SNET's Command Line Interface so that you can test your service back-end independently. It is also useful in case you plan on creating a service that interacts with other services.

TODO: MPE here

## Finding Information about Organizations and Services

Having installed SNET CLI and set up a session, you may now access the list of organization IDs in SNET's Registry by running `snet organization list`. Once you find an organization of interest, you may view further information about it through `snet organization info ORG_ID`, including its name, the public keys of its owner and members and a list of all its services. If you're only interested in the list of services, you can view that using `snet organization list-services ORG_ID`.

Once you have decided on the organization and service of interest, another useful command is `snet service print-metadata ORG_ID SERVICE_ID`. That will print to terminal some off-chain information related to the service. For this tutorial, the most relevant information is the service's endpoint.

## 

2) SNET CLI Organizations, list, etc

Say that this will mostly be done through SNET DApp (or at least be way easier to accomplish there).

- get service metadata to know what it expects
- snet client call

3) MPE, channels, open and iniialize one

Refer to [MPE Contracts](https://dev.singularitynet.io/docs/all/mpe/mpe/)


Previous: [IDENTITY](TODO)

Next: [PUBLISH](TODO)

___ 

# DRAFT

MPE : A smart contract that facilitates transactions between users and AI service developers. It provides a wallet functionality (deposit and withdraw funds) as well as uni-directional payment channels between users and AI service developers enabling users to pay for service invocations

REFER TO: [Using the SNET-CLI to pass parameters to a service](https://dev.singularitynet.io/docs/all/mpe/snet-cli/)

### Example

super resolution

```bash
(snet) ramon@winterfell:~$ snet account balance
    account: 0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0
    ETH: 0.099458052
    AGI: 0.99999995
    MPE: 0.00000005



(snet) ramon@winterfell:~$ snet account deposit 0.00000001
    transaction:
        chainId: 42
        data: '0x095ea7b300000000000000000000000039f31ac7b393fe2c6660b95b878feb16ea8f31560000000000000000000000000000000000000000000000000000000000000001'
        from: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
        gas: 45552
        gasPrice: 1000000000
        nonce: 6
        to: '0x3b226fF6AAd7851d3263e53Cb7688d13A07f6E81'
        value: 0

Proceed? (y/n): y
Submitting transaction...

    event_summaries:
    -   args:
            owner: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
            spender: '0x39f31Ac7B393fE2C6660b95b878FEB16eA8f3156'
            value: 1
        event: Approval
    receipt_summary:
        blockHash: '0xdb34a6705208cf80088d38e6b466e9a8a088759693f1d831b4ccffa835625758'
        blockNumber: 10021233
        cumulativeGasUsed: 100048
        gasUsed: 45552
        transactionHash: '0x2425338d45d318072c9891e1ea9b8937234b962472203ba1e486c97c461906d0'

    transaction:
        chainId: 42
        data: '0xb6b55f250000000000000000000000000000000000000000000000000000000000000001'
        from: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
        gas: 50637
        gasPrice: 1000000000
        nonce: 7
        to: '0x39f31Ac7B393fE2C6660b95b878FEB16eA8f3156'
        value: 0

Proceed? (y/n): y
Submitting transaction...

    event_summaries:
    -   args:
            amount: 1
            sender: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
        event: DepositFunds
    receipt_summary:
        blockHash: '0x053c2911a112706f4fe8794fb7a014d99733be2ef2967b2131ea5214b4883aa1'
        blockNumber: 10021235
        cumulativeGasUsed: 4002855
        gasUsed: 35637
        transactionHash: '0x191b82106847c709c986b625be50304a17ed121d33374d3bb11d6ef3b42e4793'



(snet) ramon@winterfell:~$ snet channel block-number
10021246
(snet) ramon@winterfell:~$ snet channel open-init snet example-service 0.00000002 10500000
!!! We must check that hash in IPFS is correct (we cannot be sure that ipfs is not compromized) !!! Please implement it !!!
!!! We must check that hash in IPFS is correct (we cannot be sure that ipfs is not compromized) !!! Please implement it !!!
    transaction:
        chainId: 42
        data: '0xe3b39250000000000000000000000000ceb196e0236c5b4ee62d5c87692284fbd52fcbd0000000000000000000000000a6e06cf37110930d2906e6ae70ba6224eded917b3316f32001b03a80c3b87035f53bee95de91bbe2c5ad05b327be4b6733f48aa200000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000a037a0'
        from: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
        gas: 163515
        gasPrice: 1000000000
        nonce: 8
        to: '0x39f31Ac7B393fE2C6660b95b878FEB16eA8f3156'
        value: 0

Proceed? (y/n): y
Submitting transaction...

    event_summaries:
    -   args:
            amount: 2
            channelId: 42
            expiration: 10500000
            groupId: 3316f32001b03a80c3b87035f53bee95de91bbe2c5ad05b327be4b6733f48aa2
            nonce: 0
            recipient: '0xA6E06cF37110930D2906e6Ae70bA6224eDED917B'
            sender: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
            signer: '0xCEb196e0236C5B4EE62d5C87692284FBd52fCBD0'
        event: ChannelOpen
    receipt_summary:
        blockHash: '0xf2053f687d2441f6d25ebd97e2bd4c53174e4af3ce4ce7593e67f043c334a234'
        blockNumber: 10021281
        cumulativeGasUsed: 277177
        gasUsed: 163515
        transactionHash: '0xab0996f4559f147a6888490ef939e3b07f6dfa99d4d121866ed57e20debdd374'

#channel_id
42
!!! We must check that hash in IPFS is correct (we cannot be sure that ipfs is not compromized) !!! Please implement it !!!



(snet) ramon@winterfell:~$ snet channel print-initialized
#channelId  nonce  recipient  groupId(base64) value(AGI)  expiration(blocks)
42 0 0xA6E06cF37110930D2906e6Ae70bA6224eDED917B MxbzIAGwOoDDuHA19Tvuld6Ru+LFrQWzJ75LZzP0iqI= 0.00000002 10500000



(snet) ramon@winterfell:~$ snet service print-metadata snet example-service
!!! We must check that hash in IPFS is correct (we cannot be sure that ipfs is not compromized) !!! Please implement it !!!
{
    "version": 1,
    "display_name": "example-service",
    "encoding": "proto",
    "service_type": "grpc",
    "payment_expiration_threshold": 40320,
    "model_ipfs_hash": "QmcL5dL7RDPBUmjFTvszszTcsQtpckabkhJjRAVHPYJBtb",
    "mpe_address": "0x39f31Ac7B393fE2C6660b95b878FEB16eA8f3156",
    "pricing": {
        "price_model": "fixed_price",
        "price_in_cogs": 1
    },
    "groups": [
        {
            "group_name": "default_group",
            "group_id": "MxbzIAGwOoDDuHA19Tvuld6Ru+LFrQWzJ75LZzP0iqI=",
            "payment_address": "0xA6E06cF37110930D2906e6Ae70bA6224eDED917B"
        }
    ],
    "endpoints": [
        {
            "group_name": "default_group",
            "endpoint": "http://54.203.198.53:7002"
        }
    ]
}



(snet) ramon@winterfell:~$ snet client get-channel-state 42 54.203.198.53:7002
current_nonce                  = 0
current_signed_amount_in_cogs  = 0
current_unspent_amount_in_cogs = 2



(snet) ramon@winterfell:~$ snet client call 42 0.00000001 54.203.198.53:7002 div '{"a":56, "b":7}'
unspent_amount_in_cogs before call (None means that we cannot get it now):2
value: 8.0
```
