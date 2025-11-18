import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="Risk-O-Meter", layout="wide")

st.title("Stock Risk-O-Meter")

st.sidebar.header("Search Stock")
ticker = st.sidebar.text_input("Enter Stock Symbol", "AAPL")

if ticker:
    data = yf.Ticker(ticker)
    info = data.info

    st.subheader(f"{info.get('shortName', ticker)} — {ticker}")

    st.write("### Basic Info")
    st.write({
        "Current Price": info.get("currentPrice"),
        "Market Cap": info.get("marketCap"),
        "P/E Ratio": info.get("trailingPE"),
        "Dividend Yield": info.get("dividendYield"),
        "52 Week High": info.get("fiftyTwoWeekHigh"),
        "52 Week Low": info.get("fiftyTwoWeekLow")
    })

    st.write("### Risk Layers (Resco Meter)")

    layers = {
        "1. Market Risk": info.get("beta"),
        "2. Volatility": info.get("regularMarketDayHigh") - info.get("regularMarketDayLow"),
        "3. Valuation Risk": info.get("trailingPE"),
        "4. Financial Health": info.get("debtToEquity"),
        "5. Liquidity Risk": info.get("currentRatio"),
        "6. Profit Stability": info.get("profitMargins")
    }

    for name, value in layers.items():
        st.write(f"{name}: {value}")


# requirements.txt
# streamlit
yfinance
pandas
numpy
scikit-learn
plotly

# README.md
# Risk-O-Meter
A Streamlit app that analyzes stock risk using six layers of financial indicators.

## How to run
```
pip install -r requirements.txt
streamlit run app.py
