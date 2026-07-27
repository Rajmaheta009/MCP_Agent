from mcp.server.fastmcp import FastMCP


def register_currency_tools(mcp: FastMCP):

    @mcp.tool()
    def convert_currency(
        amount: float,
        from_currency: str,
        to_currency: str
    ) -> str:
        """
        Currency Converter
        (Implementation coming later)
        """
        return (
            f"Currency conversion is under development.\n"
            f"Amount: {amount}\n"
            f"From: {from_currency}\n"
            f"To: {to_currency}"
        )