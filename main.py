import streamlit as st
from modules.ccxt_handler import CCXTHandler
from modules.strategies import sample_strategy
from modules.utils import display_ohlcv

st.title("Auto Trader Streamlit Demo")

# انتخاب صرافی و نماد
exchange_name = st.selectbox("Exchange", ["binance"])
symbol = st.text_input("Symbol", "BTC/USDT")

if st.button("Fetch Data"):
    ccxt_handler = CCXTHandler(exchange_name)
    ohlcv = ccxt_handler.fetch_ohlcv(symbol)
    
    if ohlcv:
        st.success("Data fetched successfully!")
        display_ohlcv(ohlcv)
        signal = sample_strategy(ohlcv)
        st.info(f"Strategy signal: {signal}")
    else:
        st.error("Failed to fetch data.")
