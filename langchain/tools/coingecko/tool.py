"""Tool for the CoinGecko API."""
import re

from langchain.tools.base import BaseTool
from langchain.utilities import CoinGeckoAPIWrapper


class CoinGeckoQueryRun(BaseTool):
    """Tool that adds the capability to query using the CoinGecko API."""

    api_wrapper: CoinGeckoAPIWrapper

    name = "CoinGecko"
    description = (
        "A wrapper around CoinGecko API. "
        "Useful for fetching information for specified cryptocurrencies. "
        "Input should be a comma-separated list of coin IDs (e.g., 'bitcoin,ethereum') "
        "followed by an optional list of comma-separated currencies (e.g., 'usd,eur'). "
        "If no currencies are provided, it defaults to 'usd'. "
    )

    def __init__(self) -> None:
        self.api_wrapper = CoinGeckoAPIWrapper()

    def _run(self, tool_input: str) -> str:
        """Use the CoinGecko tool."""
        inputs = tool_input.split()
        coin_ids = ",".join(re.findall(r"\w+", inputs[0]))
        vs_currencies = "usd"
        if len(inputs) > 1:
            vs_currencies = ",".join(re.findall(r"\w+", inputs[1]))

        coin_data = self.api_wrapper.run(coin_ids, vs_currencies)

        return str(coin_data)

    async def _arun(self, tool_input: str) -> str:
        """Use the CoinGecko tool asynchronously."""
        raise NotImplementedError("CoinGecko does not support async")
