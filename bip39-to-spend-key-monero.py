from bip_utils import (
    Bip39SeedGenerator,
    Bip32Secp256k1,
    Monero,
    MoneroCoins
)

# Insert 12 seed phrase words into "" seperated by spaces
# E.g. "busy shallow nothing casino choose obvious work soldier bachelor trouble equal extend"
BIP39_MNEMONIC = ""

def derive_keys(mnemonic):
    """
    Takes (Monero) BIP39 12 word mnemonic and derives the keys
    """
    seed = Bip39SeedGenerator(mnemonic).Generate()
    mst = Bip32Secp256k1.FromSeed(seed)
    der = mst.DerivePath("m/44'/128'/0'/0/0")
    mw = Monero.FromSeed(
        der.PrivateKey().Raw().ToBytes(),
        MoneroCoins.MONERO_MAINNET
    )

    return {
        "mnemonic": mnemonic,
        "spend": mw.PrivateSpendKey().Raw().ToHex(),
        "addr": mw.PrimaryAddress()
    }

print(derive_keys(BIP39_MNEMONIC))
