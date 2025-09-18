"""
financial_analysis_streamlit.py - analysis of a company's financial performance
    using Yahoo Finance and then leveraging an LLM to analyze performance and make a final investment recommendation based purely on financial performance.

Author: Manish Bhobe
My experiments with Python, ML and Generative AI.
Code is meant for illustration purposes ONLY. Use at your own risk!
Author is not liable for any damages arising from direct/indirect use of this code.
"""

import numpy as np
from numpy._core.numeric import True_
import streamlit as st
import yfinance as yf
from typing import Iterator

from agno.agent import RunOutput
from agno.utils.log import logger
from agents.financial_analysis_agent import financial_analysis_agent

# Page configuration
st.set_page_config(page_title="Financial Analyzer", page_icon="📊", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .stock-input {
        max-width: 400px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state
if "analysis_generated" not in st.session_state:
    st.session_state.analysis_generated = False


def is_valid_stock_symbol(symbol: str) -> bool:
    """checks if stock symbol entered is valid or not"""
    ticker = yf.Ticker(symbol.upper())
    # try to download 1 days stock price
    hist = ticker.history(period="1d")
    # if I get some history, symbol is valid!
    if hist.empty:
        logger.fatal(f"ERROR: {symbol.upper()} is not a valid stock symbol.")
        return False
    return True


def generate_financial_analysis(symbol: str):
    prompt = f"Generate financial analysis for {symbol}"
    response: RunOutput = financial_analysis_agent.run(prompt, markdown=True)
    return response.content, response.metrics


# Main UI
st.markdown(
    "<h1 class='main-header'>Investment Analyzer 📈</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <center>
    This Agent based application performs an analysis of financial ratios for publicly 
    traded companies and comes up with an recommendation on the long term investment potential.
    </center>
    <br/>
""",
    unsafe_allow_html=True,
)

# Stock symbol input
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        stock_symbol = st.text_input(
            "Enter Stock Symbol to begin (should be same as used on the Yahoo! Finance website):",
            placeholder="e.g., TCS.NS",
            key="stock_input",
        )
    with col2:
        col2.markdown(f"<div style='height: 28px;'></div>", unsafe_allow_html=True)
        analyze_button = st.button("Analyze", type="primary")

# Analysis section
if analyze_button and stock_symbol:
    # check if user has entered a valid stock symbol
    if not is_valid_stock_symbol(stock_symbol):
        st.markdown(
            f"""<div style='color: red;'>
            Invalid stock symbol: {stock_symbol.upper()}. Please enter valid symbol to proceed!
            </div>""",
            unsafe_allow_html=True,
        )
        st.stop()

    try:
        stock_symbol = stock_symbol.upper()
        company_name = yf.Ticker(stock_symbol).info.get("longName")
        with st.spinner(
            f"Generating financial analysis for {company_name} ({stock_symbol})..."
        ):
            analysis, metrics = generate_financial_analysis(stock_symbol)

        st.success("Analysis completed!")
        st.markdown(analysis)
        #st.markdown(metrics)  

        # Display analysis in an expandable container
        # with st.expander("View Detailed Analysis", expanded=True):
        #     # input_tokens = np.array(metrics["input_tokens"]).sum()
        #     # output_tokens = np.array(metrics["output_tokens"]).sum()
        #     # total_tokens = np.array(metrics["total_tokens"]).sum()
        #     # total_time = np.array(metrics["time"]).sum()
        #     # # st.markdown(f"**Metrics**: {metrics}")
        #     # st.markdown(
        #     #     f"**Token Count** -> Input: {input_tokens:5d} - Output: {output_tokens:5d} - Total: {total_tokens:5d} | **Time Taken**: {total_time:2f}s"
        #     # )
        #     st.markdown(analysis)

        st.session_state.analysis_generated = True

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #999;'>
        <small><b>Developed by:</b> Manish Bhobé • <b>Powered by:</b> yfinance | Agno (for agents) | Google Gemini (LLM) | Streamlit (UI) • <b>For educational purposes only!</b></small>
    </div>
    """,
    unsafe_allow_html=True,
)
