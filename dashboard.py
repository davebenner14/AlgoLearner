import streamlit as st
import pandas as pd
import os

st.title("AlgoLearner Dashboard")

# Display the current portfolio value from portfolio.txt
if os.path.exists('portfolio.txt'):
    with open('portfolio.txt', 'r') as f:
        portfolio_value = f.read().strip()
    st.subheader(f"Current Portfolio Value: ${portfolio_value}")
else:
    st.subheader("Portfolio Value Not Available Yet")

# Button to show trade history from trade_history.csv
if st.button("Show Trade History"):
    if os.path.exists('trade_history.csv'):
        df = pd.read_csv('trade_history.csv')
        st.write("### Previous Trades", df)
    else:
        st.write("No trade history available yet.")
