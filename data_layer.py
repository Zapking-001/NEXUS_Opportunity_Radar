import yfinance as yf                                                                                                                                                                                                               # type: ignore
import pandas as pd                                                                                                                                                                                                                # type: ignore
import numpy as np                                                                                                                                                                                                                # type: ignore

def fetch_market_anomaly(ticker_symbol):
    """
    Extracts NSE data and performs statistical anomaly detection.
    """
    ticker = f"{ticker_symbol}.NS"
    print(f"[SYSTEM] Scanning {ticker} for anomalies...")
    
    # Fetch 6 months of data
    stock = yf.Ticker(ticker)
    df = stock.history(period="6mo")
    
    if df.empty:
        return {"error": "Invalid ticker or no data found."}

    # 1. 20-Day Simple Moving Average (SMA)
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    
    # 2. Volume Z-Score (Mathematical signal for unusual interest)
    # Formula: (Current Volume - Avg Volume) / Std Dev Volume
    df['Vol_Mean'] = df['Volume'].rolling(window=20).mean()
    df['Vol_STD'] = df['Volume'].rolling(window=20).std()
    df['Vol_ZScore'] = (df['Volume'] - df['Vol_Mean']) / df['Vol_STD']
    
    # Isolate the latest session
    latest = df.iloc[-1]
    
    return {
        "ticker": ticker_symbol,
        "price": round(latest['Close'], 2),
        "sma_20": round(latest['SMA_20'], 2),
        "vol_zscore": round(latest['Vol_ZScore'], 2),
        "status": "Potential Breakout" if latest['Vol_ZScore'] > 2 else "Normal Activity",
        "trend": "Bullish" if latest['Close'] > latest['SMA_20'] else "Bearish"
    }

if __name__ == "__main__":
    # Quick test for Reliance
    print(fetch_market_anomaly("RELIANCE"))

