"""Util that calls CoinGecko."""
from typing import Any, Dict, Optional

from pydantic import Extra, root_validator

from langchain.tools.base import BaseModel
from langchain.utils import get_from_dict_or_env


class CoinGeckoAPIWrapper(BaseModel):
    """Wrapper for CoinGecko API using pycoingecko."""

    cg: Any
    coingecko_api_key: Optional[str] = None

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator(pre=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key exists in environment."""
        coingecko_api_key = get_from_dict_or_env(
            values, "coingecko_api_key", "COINGECKO_API_KEY", default=""
        )
        values["coingecko_api_key"] = coingecko_api_key

        try:
            import pycoingecko

        except ImportError:
            raise ImportError(
                "pycoingecko is not installed. "
                "Please install it with `pip install pycoingecko`"
            )

        cg = pycoingecko.CoinGeckoAPI(coingecko_api_key)
        values["cg"] = cg

        return values

    def run(self, coin_ids: str, vs_currencies: str = "usd") -> str:
        """Get the formatted coin information for specified coins and currencies."""
        coin_info = self.get_coin_info(coin_ids, vs_currencies)
        formatted_info = self.format_coin_info(coin_info, vs_currencies)

        # Concatenate the formatted coin information into a single column string.
        formatted_output = "\n\n".join(formatted_info.values())
        return formatted_output

    def get_coin_info(self, coin_ids: str, vs_currencies: str) -> Dict[str, Any]:
        """Get the coin information for specified coins."""
        coin_info = self.cg.get_price(
            ids=coin_ids,
            vs_currencies=vs_currencies,
            include_market_cap=True,
            include_24hr_vol=True,
            include_24hr_change=True,
        )
        return coin_info

    def format_coin_info(
        self, coin_info: Dict[str, Any], vs_currencies: str
    ) -> Dict[str, str]:
        """Format the coin information into a human-readable format."""
        formatted_output = {}
        currencies = vs_currencies.split(",")

        for coin_id, coin_data in coin_info.items():
            # Create a list to store formatted data for each coin.
            formatted_data = [f"Coin information for {coin_id}:"]
            for currency in currencies:
                currency_upper = currency.upper()
                formatted_data.append(f"  In {currency_upper}:")
                formatted_data.append(f"    Price: ${coin_data[currency]:,.2f}")
                formatted_data.append(
                    f"    Market cap: ${coin_data[f'{currency}_market_cap']:,.2f}"
                )
                formatted_data.append(
                    f"    24h volume: ${coin_data[f'{currency}_24h_vol']:,.2f}"
                )
                formatted_data.append(
                    f"    24h change: {coin_data[f'{currency}_24h_change']:.2f}%"
                )

            formatted_output[coin_id] = "\n".join(formatted_data)

        return formatted_output
