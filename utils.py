import pandas as pd
import streamlit as st

def display_ohlcv(ohlcv):
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    st.dataframe(df)
