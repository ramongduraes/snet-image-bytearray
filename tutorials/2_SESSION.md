# Set Up a SingularityNET Session

> This tutorial assumes you have SNET CLI installed. If you don't please follow the [this tutorial](TODO). 

This tutorial will guide you through "signing up" to SingularityNET. This will be accomplished by creating an __identity__ and associating it to an __organization__ that is listed under SNET's Registry.

To proceed, you will need a private-public key pair. You can generate it for free using [Metamask](https://metamask.io). Make sure you store your private key somewhere safe since its _irrecoverable_! 

You will also need some AGI and ETH tokens to perform transactions on the Blockchain. SNET CLI's default Blockchain network is the [Kovan Testnet](https://kovan-testnet.github.io/website/), a "publicly accessible Blockchain for Ethereum; created and maintained by a consortium of Ethereum developers, to aide the Ethereum developer community". Therefore you do not have to worry about spending real money when following our tutorials. In fact, you can obtain ETH and AGI (SingularityNET's token) for free using your public key (ETH address) and Github account at:

* AGI: https://faucet.singularitynet.io/
* ETH: https://faucet.kovan.network/

Once you have your key pair and some ETH and AGI tokens in it, you're ready to proceed by creating an __identity__: a local alias for you private key. Your identities are kept private at your machine, so neither your identity name nor your private key (of course) will be available for other users or service providers. You will then associate your local identity's public key to an __organization__ listed under SingularityNET's Registry. That way, SingularityNET will know where to refer to whenever a transaction involving your account needs to be signed.

## Creating an Identity

The first step required to run any of SNET CLI's commands is to create an identity. An identity is a local alias for your private key at the Blockchain that will be used to sign your transactions. 

You can create an identity by running `snet identity create IDENTITY_NAME IDENTITY_TYPE`, in which `IDENTITY_NAME` is your chosen identity name and `IDENTITY_TYPE` is the type of your identity. The available identity types are:

- 'rpc': (yields to a required ethereum json-rpc endpoint for signing using a given wallet
          index)       
- 'mnemonic': (uses a required bip39 mnemonic for HDWallet/account derivation and signing
          using a given wallet index)
- 'key': (uses a required hex-encoded private key for signing)
- 'ledger': (yields to a required ledger nano s device for signing using a given wallet
          index)
- 'trezor': (yields to a required trezor device for signing using a given wallet index) 
    
In this tutorial we will create an example identity named `example_id` using our private key, hence the chosen 'IDENTITY_TYPE' is `key`. E.g.:

```bash
snet identity create example_id key
```

You will now be prompted for your private key, paste it at the terminal and press Enter. 

_Don't worry about providing your private key! This ID is just an alias kept locally to make it easier for you to refer to your private key, it won't be available to anyone._

That's it! If this your first identity you create, you will be shown a message saying that SNET CLI will automatically switch to it, meaning it will become the default identity for your next transactions, and that it is not bind to any network. You can find more information about your session, including current identity and network, by running `snet session`. Also, notice that you may create several local identities and switch between them by running `snet identity IDENTITY_NAME`.

## Creating an Organization

The last step needed to interact with AI services is to associate your identity with an organization registered under SingularityNET. That can be done by either creating a new organization or associating your identity (i.e. your public key) with an existing one.

To create an organization, all you need is to provide an organization name and its ID by running `snet organization create ORG_NAME --org-id ORG_ID`. Organization names can have spaces, special characters, capital letters and can even repeat. Organization IDs, however, are unique and should be named following our [naming standardization guidelines](https://github.com/singnet/dev-portal/blob/master/docs/all/naming-standard.md), by sticking to lowercase letters and using dashes instead of spaces or underscores.

Let's create an example organization called 'Example Organization' under the ID 'example-organization':

> Notice that if you try to run the following command without changing the ID you'll probably see an error saying that it already exists.

```bash
snet organization create 'Example Organization' --org-id example-organization
```

Confirm your transaction and you should now have your organization listed in SingularityNET's Registry! 

If you want to join an existing organization, provide your public key to the organization owner so that they can add you as a member (by running `snet organization add-members ORG_ID YOUR_PUBLIC_KEY`). 

To delete your organizations, simply run `snet organization delete ORG_ID`. You can get a list of all organization related commands available by typing `snet organization`.

____

Previous: [INSTALL](TODO)

Next: [CALL SERVICE](TODO)