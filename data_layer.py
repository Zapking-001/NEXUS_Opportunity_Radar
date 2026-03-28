import yfinance as yf
import pandas as pd
import numpy as np

def get_nse_data(ticker: str, period: str = "1mo") -> str:
    """
    Fetches historical data for a given NSE ticker and calculates the Volume Z-Score.
    """
    try:
        # Ensure correct NSE suffix
        if not ticker.endswith('.NS') and not ticker.endswith('.BO'):
            ticker += '.NS'
            
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        
        if hist.empty:
            return f"Error: No data found for ticker {ticker}."
        
        # Calculate 20-day moving average and standard deviation for volume
        hist['Vol_SMA_20'] = hist['Volume'].rolling(window=20, min_periods=1).mean()
        hist['Vol_Std_20'] = hist['Volume'].rolling(window=20, min_periods=1).std()
        
        # Calculate Volume Z-Score (Replace 0s with NaN to avoid division by zero)
        hist['Vol_Std_20'] = hist['Vol_Std_20'].replace(0, np.nan) 
        hist['Volume_Z_Score'] = (hist['Volume'] - hist['Vol_SMA_20']) / hist['Vol_Std_20']
        hist['Volume_Z_Score'] = hist['Volume_Z_Score'].fillna(0)
        
        latest = hist.iloc[-1]
        
        report = f"""
        Market Data Report for {ticker} (Latest Trading Session):
        - Close Price: ₹{latest['Close']:.2f}
        - Trading Volume: {int(latest['Volume'])}
        - 20-Day Avg Volume: {latest['Vol_SMA_20']:.2f}
        - Volume Z-Score: {latest['Volume_Z_Score']:.2f}
        
        Recent Trend (Last 5 Days Close Prices):
        {hist['Close'].tail(5).to_dict()}
        """
        return report
    except Exception as e:
        return f"Error fetching data: {str(e)}"