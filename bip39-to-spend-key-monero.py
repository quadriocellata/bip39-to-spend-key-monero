from bip_utils import (
    Bip39SeedGenerator,
    Bip32Secp256k1,
    Monero,
    MoneroCoins
)

# Replace * with you seed phrase words
BIP39_MNEMONIC = "mind indoor shy maid wonder define replace bread enough rule patient climb"

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