"""Small Yahoo Finance helpers used by the Streamlit app."""

import pandas as pd
import yfinance as yf


def _clean_ticker(ticker):
    """Return a normalized ticker or raise a helpful error."""
    ticker = ticker.strip().upper()
    if not ticker:
        raise ValueError("Enter a ticker symbol, such as AAPL.")
    return ticker


def get_financials(ticker):
    """Return the latest income statement, balance sheet, and cash flow."""
    stock = yf.Ticker(_clean_ticker(ticker))
    return {
        "Income statement": stock.financials,
        "Balance sheet": stock.balance_sheet,
        "Cash flow": stock.cashflow,
    }


def get_news(ticker):
    """Return up to five recent news articles as a table."""
    stock = yf.Ticker(_clean_ticker(ticker))
    articles = stock.news or []
    rows = []

    for article in articles[:5]:
        content = article.get("content", article)
        rows.append(
            {
                "Title": content.get("title", "No title"),
                "Description": content.get("description", "No description"),
                "Published": content.get("pubDate", content.get("providerPublishTime")),
                "Link": content.get("canonicalUrl", content.get("link")),
            }
        )

    return pd.DataFrame(rows)


def get_stock_price_and_ratings(ticker):
    """Return the current price and recent analyst recommendations."""
    ticker = _clean_ticker(ticker)
    stock = yf.Ticker(ticker)
    price = stock.info.get("currentPrice")
    if price is None:
        price = stock.fast_info.get("last_price")

    recommendations = stock.recommendations
    if recommendations is None:
        recommendations = pd.DataFrame()
    else:
        recommendations = recommendations.tail(10)

    return {"ticker": ticker, "price": price, "recommendations": recommendations}