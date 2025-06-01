"""
Cryptocurrency database and data structures for the CryptoWise Advisor Chatbot.
Contains predefined cryptocurrency data with key metrics for analysis.
"""

# Cryptocurrency database with key metrics
crypto_db = {
    "Bitcoin": {
        "symbol": "BTC",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 5,
        "project_viability": "high",
        "description": "The original cryptocurrency, known for its security and widespread adoption."
    },
    "Ethereum": {
        "symbol": "ETH",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 7,
        "project_viability": "high",
        "description": "A decentralized platform enabling smart contracts and decentralized applications."
    },
    "Cardano": {
        "symbol": "ADA",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
        "project_viability": "high",
        "description": "A proof-of-stake blockchain platform focused on sustainability and scalability."
    },
    "Solana": {
        "symbol": "SOL",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
        "project_viability": "medium",
        "description": "High-performance blockchain supporting decentralized applications and marketplaces."
    },
    "Polkadot": {
        "symbol": "DOT",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "project_viability": "high",
        "description": "A multi-chain network enabling different blockchains to transfer messages and value."
    }
}

# Constants for analysis
SUSTAINABILITY_THRESHOLD = 7
MARKET_CAP_WEIGHTS = {
    "high": 3,
    "medium": 2,
    "low": 1
}

PRICE_TREND_WEIGHTS = {
    "rising": 3,
    "stable": 2,
    "falling": 1
}

ENERGY_USE_WEIGHTS = {
    "low": 3,
    "medium": 2,
    "high": 1
}

def get_trending_cryptos():
    """Returns cryptocurrencies with rising price trends."""
    return {name: data for name, data in crypto_db.items() 
            if data["price_trend"] == "rising"}

def get_sustainable_cryptos():
    """Returns cryptocurrencies with high sustainability scores."""
    return {name: data for name, data in crypto_db.items() 
            if data["sustainability_score"] >= SUSTAINABILITY_THRESHOLD}

def get_profitable_cryptos():
    """Returns cryptocurrencies with high market cap and rising trends."""
    return {name: data for name, data in crypto_db.items() 
            if data["market_cap"] == "high" and data["price_trend"] == "rising"}

def calculate_sustainability_score(crypto_data):
    """Calculates a weighted sustainability score for a cryptocurrency."""
    energy_score = ENERGY_USE_WEIGHTS.get(crypto_data["energy_use"], 0)
    base_score = crypto_data["sustainability_score"]
    return (energy_score + base_score) / 2

def get_crypto_info(crypto_name):
    """Returns detailed information about a specific cryptocurrency."""
    return crypto_db.get(crypto_name.title()) 