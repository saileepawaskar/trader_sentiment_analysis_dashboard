import streamlit as st
import pandas as pd  # ← THIS WAS MISSING!

def render_kpi_metrics(df):
    """Render KPI cards in sidebar"""
    col1, col2, col3, col4 = st.columns(4)
    
    total_trades = len(df)
    win_rate = (df['pnl'] > 0).mean() * 100
    avg_pnl = df['pnl'].mean()
    total_volume = df['size_usd'].sum()
    
    with col1: st.metric("Total Trades", f"{total_trades:,}")
    with col2: st.metric("Win Rate", f"{win_rate:.1f}%")
    with col3: st.metric("Avg PnL", f"${avg_pnl:.4f}")
    with col4: st.metric("Total Volume", f"${total_volume:,.0f}")

def trading_strategy_table(best_sentiment):
    """Generate strategy table"""
    strategy_data = {
        'Sentiment': ['Greed', 'Neutral', 'Fear', 'Extreme Fear'],
        'Win Rate': ['High', 'Medium', 'Low', 'Very Low'],
        'Action': ['LONG (1.5x size)', 'Hold', 'SHORT (1.2x)', 'AVOID'],
        'Leverage': ['3-5x', '2-3x', '<3x', '<2x']
    }
    return pd.DataFrame(strategy_data)