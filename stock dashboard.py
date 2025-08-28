import yfinance as yf
import streamlit as st
import plotly.graph_objs as go
from datetime import date

# --- Page Setup ---
st.set_page_config(layout="wide")
st.title("📈 Stock Analysis Dashboard")

# --- Sidebar Inputs ---
st.sidebar.header("Stock Options")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL, TSLA):", "AAPL")

start_date = st.sidebar.date_input("Start Date", date(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", date.today())

ma1 = st.sidebar.slider("Short MA (days)", min_value=5, max_value=50, value=20)
ma2 = st.sidebar.slider("Long MA (days)", min_value=10, max_value=200, value=50)

# --- Data Loading ---
@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, auto_adjust=False)
    df["MA1"] = df["Adj Close"].rolling(window=ma1).mean()
    df["MA2"] = df["Adj Close"].rolling(window=ma2).mean()
    return df

try:
    df = load_data(ticker, start_date, end_date)

    st.subheader(f"{ticker} Stock Price")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Adj Close"], name="Adj Close", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x=df.index, y=df["MA1"], name=f"{ma1}-day MA", line=dict(color="orange")))
    fig.add_trace(go.Scatter(x=df.index, y=df["MA2"], name=f"{ma2}-day MA", line=dict(color="green")))
    fig.update_layout(title=f"{ticker} Price with Moving Averages", xaxis_title="Date", yaxis_title="Price (USD)", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    # --- Volume Chart ---
    st.subheader(f"{ticker} Trading Volume")
    vol_fig = go.Figure()
    vol_fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name="Volume", marker_color="purple"))
    vol_fig.update_layout(xaxis_title="Date", yaxis_title="Volume", template="plotly_white")
    st.plotly_chart(vol_fig, use_container_width=True)

except Exception as e:
    st.error(f"Error fetching data for {ticker}: {e}")
