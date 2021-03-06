__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


# Exchanges
BINANCE = "binance"
BINANCE_DEX = "binance_dex"
UPHOLD = "uphold"
OKEX = "okex"
IDEX = "idex"
SWITCHEO = "switcheo"
HOTBIT = "hotbit"
BIBOX = "bibox"
OKCOIN = "okcoin"
BITHUMB = "bithumb"
COINBENE = "coinbene"
DCOIN = "dcoin"
BITMAX = "bitmax"
BILAXY = "bilaxy"
BITSTAMP = "bitstamp"
KUCOIN = "kucoin"
COINBASE_PRO = "coinbase_pro"
LIQUID = "liquid"


EXCHANGES = [
    BINANCE,
    BINANCE_DEX,
    UPHOLD,
    OKEX,
    IDEX,
    SWITCHEO,
    HOTBIT,
    BIBOX,
    OKCOIN,
    BITHUMB,
    COINBENE,
    DCOIN,
    BITMAX,
    BILAXY,
    BITSTAMP,
    KUCOIN,
    COINBASE_PRO,
    LIQUID,
]


SYMBOLS_PER_EXCHANGE = []

# Binance
SYMBOLS_PER_EXCHANGE.append(
    {
        BINANCE: {
            "pairs": [
                ("BTC", "USDT"),
                ("ETH", "USDT"),
                ("ETH", "BTC"),
                ("LTC", "USDT"),
                ("BNB", "USDT"),
                ("BNB", "BTC"),
                ("XRP", "USDT"),
                ("XLM", "USDT"),
                ("XMR", "USDT"),
                ("ADA", "USDT"),
                ("XTZ", "USDT"),
                ("ICX", "USDT"),
                ("VET", "USDT"),
                ("NANO", "USDT"),
                ("ONT", "USDT"),
                ("LINK", "USDT"),
                ("LINK", "BTC"),
                ("HBAR", "USDT"),
                ("HBAR", "BTC"),
                ("LTO", "USDT"),
                ("LTO", "BTC"),
                ("FTM", "USDT"),
                ("FTM", "BTC"),
                ("REN", "USDT"),
                ("REN", "BTC"),
                ("KNC", "USDT"),
                ("KNC", "BTC"),
                ("LEND", "USDT"),
                ("LEND", "BTC"),
            ],
        }
    }
)

# Bitstamp
SYMBOLS_PER_EXCHANGE.append(
    {BITSTAMP: {"pairs": [("BTC", "USD"), ("ETH", "USD"),]}}
)

# OKEx
SYMBOLS_PER_EXCHANGE.append(
    {OKEX: {"pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("LTC", "USDT"),]}}
)

# Coinbase Pro
SYMBOLS_PER_EXCHANGE.append(
    {COINBASE_PRO: {"pairs": [("BTC", "USD"), ("ETH", "USD"),]}}
)

# Kucoin
SYMBOLS_PER_EXCHANGE.append(
    {KUCOIN: {"pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("EWT", "BTC"),]}}
)

# BIBOX
SYMBOLS_PER_EXCHANGE.append(
    {BIBOX: {"pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("LTC", "USDT"),]}}
)

# Bitmax
SYMBOLS_PER_EXCHANGE.append(
    {
        BITMAX: {
            "pairs": [("LTO", "USDT"), ("LTO", "BTC"), ("BTMX", "USDT"),],
            "single_request": True,
        }
    }
)

# IDEX
SYMBOLS_PER_EXCHANGE.append(
    {
        IDEX: {
            "pairs": [
                ("LTO", "ETH"),
                ("LQD", "ETH"),
                ("IDEX", "ETH"),
                ("CARD", "ETH"),
            ]
        }
    }
)

# OKCoin
SYMBOLS_PER_EXCHANGE.append(
    {OKCOIN: {"pairs": [("BTC", "USD"), ("ETH", "USD"), ("LTC", "USD"),]}}
)

# LIQUID
SYMBOLS_PER_EXCHANGE.append(
    {LIQUID: {"pairs": [("EWT", "BTC"), ("EWT", "ETH"),]}}
)

# Coinbene
SYMBOLS_PER_EXCHANGE.append(
    {COINBENE: {"pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("LTC", "USDT"),]}}
)

# Hotbit
SYMBOLS_PER_EXCHANGE.append(
    {
        HOTBIT: {
            "pairs": [
                ("LTO", "USDT"),
                ("LTO", "BTC"),
                ("LTO", "ETH"),
                ("LQD", "ETH"),
                ("LQD", "BTC"),
                ("CARD", "ETH"),
            ],
            "single_request": True,
        }
    }
)

# Bilaxy
SYMBOLS_PER_EXCHANGE.append(
    {
        BILAXY: {
            "pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("LQD", "ETH"),],
            "single_request": True,
        }
    }
)

# Uphold
SYMBOLS_PER_EXCHANGE.append(
    {UPHOLD: {"pairs": [("BTC", "USD"), ("ETH", "USD"), ("LTC", "USD"),]}}
)

# Binance DEX
SYMBOLS_PER_EXCHANGE.append(
    {BINANCE_DEX: {"pairs": [("LTO", "BNB"),], "single_request": True,}}
)

# DCoin
SYMBOLS_PER_EXCHANGE.append({DCOIN: {"pairs": [], "single_request": True,}})

# Switcheo
SYMBOLS_PER_EXCHANGE.append({SWITCHEO: {"pairs": [], "single_request": True,}})


EXCHANGES_AND_PAIRS_OF_REFERENCE = {
    "BTC": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "ETH": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "LTC": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "BNB": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "XRP": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "XLM": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "XMR": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "ADA": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "VET": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "ICX": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "XTZ": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "NANO": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "ONT": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "LINK": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "HBAR": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "BTMX": {"pair": "USDT", "name": BITMAX,},
    "LTO": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "FTM": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "KNC": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "LEND": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "REN": {"pair": "USDT", "name": BINANCE, "market_depth": BINANCE},
    "IDEX": {"pair": "ETH", "name": IDEX, "market_depth": IDEX},
    "LQD": {"pair": "ETH", "name": BILAXY, "market_depth": IDEX},
    "CARD": {"pair": "ETH", "name": HOTBIT, "market_depth": IDEX},
    "EWT": {"pair": "ETH", "name": LIQUID,},
}

# Check to make sure that ALL configured symbols must have an
# exchange and pair referenced
from xtcryptosignals.common.utils import get_coin_tokens  # noqa: E402

assert sorted(get_coin_tokens(SYMBOLS_PER_EXCHANGE)) == sorted(
    list(EXCHANGES_AND_PAIRS_OF_REFERENCE.keys())
)
