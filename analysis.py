import pandas as pd
import numpy as np
import os
from scipy import stats

def ensure_outputs_folder():
    """Auto-create outputs folder"""
    os.makedirs('outputs', exist_ok=True)

def calculate_metrics(df):
    """Performance metrics by sentiment (NO account needed)"""
    metrics = df.groupby('sentiment_category').agg({
        'pnl': ['count', 'mean', 'median', 'std', lambda x: (x > 0).mean()],
        'size_usd': 'mean',
        'leverage': 'mean'
    }).round(4)
    metrics.columns = ['Trade Count', 'Avg PnL', 'Median PnL', 'PnL Std', 
                      'Win Rate', 'Avg Size USD', 'Avg Leverage']
    return metrics.sort_values('Win Rate', ascending=False)

def top_traders_analysis(df, n=10):
    """Top traders OR fallback to trade clusters if no account column"""
    if 'account' in df.columns:
        # Normal case
        trader_summary = df.groupby('account').agg({
            'pnl': ['count', 'sum', 'mean', lambda x: (x > 0).mean()],
            'size_usd': 'sum'
        }).round(4)
        trader_summary.columns = ['Trades', 'Total PnL', 'Avg PnL', 'Win Rate', 'Total Volume']
        return trader_summary.sort_values('Total PnL', ascending=False).head(n)
    else:
        # FALLBACK: Create fake trader IDs for demo
        print("⚠️ No 'account' column - using trade clusters")
        df['account'] = ['Trader_' + str(i//1000) for i in range(len(df))]
        trader_summary = df.groupby('account').agg({
            'pnl': ['count', 'sum', 'mean', lambda x: (x > 0).mean()],
            'size_usd': 'sum'
        }).round(4)
        trader_summary.columns = ['Trades', 'Total PnL', 'Avg PnL', 'Win Rate', 'Total Volume']
        return trader_summary.sort_values('Total PnL', ascending=False).head(n)

def statistical_tests(df):
    """Statistical tests (NO account needed)"""
    groups = [group['pnl'].dropna() for name, group in df.groupby('sentiment_category')]
    f_stat, p_value = stats.f_oneway(*[g for g in groups if len(g) > 5])
    
    corr_cols = ['pnl', 'size_usd', 'leverage']
    if 'value' in df.columns:
        corr_cols.append('value')
    
    corr_matrix = df[corr_cols].corr().round(3)
    
    return {
        'anova_f': f_stat,
        'anova_p': p_value,
        'correlation_matrix': corr_matrix
    }

def save_outputs(df, metrics, top_traders, stats):
    """Save all outputs"""
    ensure_outputs_folder()
    metrics.to_csv('outputs/performance_table.csv')
    top_traders.to_csv('outputs/top_traders.csv')
    stats['correlation_matrix'].to_csv('outputs/correlation_matrix.csv')
    df.to_csv('outputs/full_analysis_data.csv', index=False)
    print("✅ All outputs saved!")