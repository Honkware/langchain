# flake8: noqa
COINGECKO_API_DOCS = """BASE URL: https://api.coingecko.com/api/v3

API Documentation
The API endpoints are organized by categories such as simple, coins, exchanges, derivatives, and more. Below are some of the commonly used endpoints:

1. /simple/price - Required: ids, vs_currencies
2. /coins/{id}/market_chart - Required: id, vs_currency, days; Optional: interval
3. /coins/markets - Required: vs_currency; Optional: order, per_page, page, sparkline, price_change_percentage
4. /coins/{id} - Required: id; Optional: localization, tickers, market_data, community_data, developer_data, sparkline
5. /global - No required parameters.
6. /search - Required: query
7. /exchanges - Optional: per_page, page
8. /coins/categories/list - No required parameters.
9. /derivatives/exchanges - Optional: per_page, page
10. /dexes - Optional: per_page, page
11. /defi/protocols - Optional: per_page, page
12. /nfts/list - Optional: per_page, page
13. /finance_platforms - Optional: per_page, page
14. /finance_products - Optional: per_page, page
15. /exchange_rates - No required parameters.
16. /defi/protocols/{id} - Required: id
17. /defi/leaderboard - Optional: per_page, page
18. /centralized_exchanges - Optional: per_page, page
19. /coins/{id}/history - Required: id, date; Optional: localization
20. /coins/{id}/ohlc - Required: id, vs_currency; Optional: days
21. /indexes - Optional: per_page, page
22. /coins/trending - Optional: per_page
23. /search/trending - No required parameters.
24. /search/trending/{id} - Required: id
25. /coins/{id}/market_chart/range - Required: id, vs_currency, from, to
26. /coins/list - No required parameters.
27. /simple/token_price/{id} - Required: id, contract_addresses, vs_currencies
28. /coins/{id}/contract/{contract_address}/holders/{type} - Required: id, contract_address; Optional: page, limit
29. /coins/{id}/contract/{contract_address}/holders/count - Required: id, contract_address
30. /coins/{id}/contract/{contract_address}/market_chart - Required: id, contract_address, vs_currency, days; Optional: interval
"""