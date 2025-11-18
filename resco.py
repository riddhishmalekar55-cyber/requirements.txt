import streamlit as st
import yfinance as yf

st.title("Simple Resco Meter")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)
    info = stock.info

    st.subheader(f"{info.get('shortName', ticker)} — {ticker}")

    # Simple Risk Factors
    beta = info.get("beta", 0)
    pe = info.get("trailingPE", 0)
    debt = info.get("debtToEquity", 0)
    volatility = info.get("regularMarketDayHigh", 0) - info.get("regularMarketDayLow", 0)

    st.write("### Basic Data")
    st.write({
        "Current Price": info.get("currentPrice"),
        "52W High": info.get("fiftyTwoWeekHigh"),
        "52W Low": info.get("fiftyTwoWeekLow")
    })

    st.write("### Resco Meter (Simple Risk Levels)")
    st.write(f"**Market Risk (Beta):** {beta}")
    st.write(f"**Valuation Risk (P/E):** {pe}")
    st.write(f"**Financial Risk (Debt/Equity):** {debt}")
    st.write(f"**Volatility:** {volatility}")

    # Simple Risk conclusion
    risk_score = 0

    if beta and beta > 1:
        risk_score += 2
    if pe and pe > 25:
        risk_score += 2
    if debt and debt > 80:
        risk_score += 2
    if volatility and volatility > 5:
        risk_score += 2

    st.write("### Final Risk
