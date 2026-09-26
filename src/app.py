"""Beginner-friendly Streamlit interface for the finance analyses."""

import streamlit as st

from analysis import get_financials, get_news, get_stock_price_and_ratings


st.title("Stock Analysis")
st.write("Choose an analysis and enter a ticker symbol to get started.")

ticker = st.text_input("Ticker symbol", value="AAPL", help="For example: AAPL or GOOG")
analysis_type = st.selectbox(
    "Analysis type",
    ("Filings", "News", "Stock price ratings"),
)

if st.button("Run"):
    try:
        if analysis_type == "Filings":
            results = get_financials(ticker)
            for title, table in results.items():
                st.write(title)
                if table is None or table.empty:
                    st.write("No data available.")
                else:
                    st.dataframe(table)

        elif analysis_type == "News":
            articles = get_news(ticker)
            st.write(f"Recent news for {ticker.strip().upper()}")
            if articles.empty:
                st.write("No news found.")
            else:
                st.dataframe(articles, use_container_width=True)

        else:
            results = get_stock_price_and_ratings(ticker)
            st.write(f"Stock price and analyst ratings for {results['ticker']}")
            if results["price"] is None:
                st.write("Current price is not available.")
            else:
                st.metric("Current price", f"${results['price']:,.2f}")

            st.write("Latest analyst recommendations")
            if results["recommendations"].empty:
                st.write("No analyst recommendations found.")
            else:
                st.dataframe(results["recommendations"], use_container_width=True)

    except Exception as error:
        st.error(f"Could not complete the analysis: {error}")