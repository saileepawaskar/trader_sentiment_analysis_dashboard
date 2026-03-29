import pandas as pd
import numpy as np
from pathlib import Path
import os

def load_and_clean_data(data_path="./data"):
    """Load and clean trader + fear/greed data with flexible paths"""
    data_path = Path(data_path)
    
    # Load trader data
    trader_file = data_path / "trader_data.csv"
    if not trader_file.exists():
        raise FileNotFoundError(f"❌ {trader_file} not found!")
    
    trader_df = pd.read_csv(trader_file)
    
    # Load Fear & Greed (sample data if missing)
    fg_file = data_path / "fear_greed.csv"
    if fg_file.exists():
        fg_df = pd.read_csv(fg_file)
    else:
        # Generate sample Fear & Greed data
        dates = pd.date_range('2024-01-01', periods=len(trader_df), freq='D')
        fg_df = pd.DataFrame({
            'timestamp': dates,
            'fear_greed_index': np.random.randint(20, 80, len(dates))
        })
    
    # Merge and clean
    df = trader_df.merge(fg_df, on='timestamp', how='left')
    df['sentiment_category'] = pd.cut(df['fear_greed_index'], 
                                    bins=[0, 25, 45, 55, 75, 100],
                                    labels=['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed'])
    
    # Calculate PnL and size
    df['pnl'] = df['exit_price'] * df['position_size'] - df['entry_price'] * df['position_size']
    df['size_usd'] = df['position_size'] * df['entry_price']
    
    return trader_df, fg_df, df