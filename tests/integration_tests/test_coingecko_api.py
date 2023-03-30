from langchain.utilities.coingecko import CoinGeckoAPIWrapper

def test_call() -> None:
    """Test that CoinGeckoAPIWrapper returns correct info for bitcoin and ethereum in USD and EUR."""

    coingecko = CoinGeckoAPIWrapper()
    coin_info = coingecko.run("bitcoin,ethereum", "usd,eur")

    assert coin_info is not None

    # Check for Bitcoin information
    assert "Coin information for bitcoin" in coin_info
    assert "In USD:" in coin_info
    assert "In EUR:" in coin_info
    assert "Price: $" in coin_info
    assert "Market cap: $" in coin_info
    assert "24h volume: $" in coin_info
    assert "24h change:" in coin_info

    # Check for Ethereum information
    assert "Coin information for ethereum" in coin_info
    assert "In USD:" in coin_info
    assert "In EUR:" in coin_info
    assert "Price: $" in coin_info
    assert "Market cap: $" in coin_info
    assert "24h volume: $" in coin_info
    assert "24h change:" in coin_info
