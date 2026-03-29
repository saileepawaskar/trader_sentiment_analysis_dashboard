import pandas as pd
import numpy as np
import scipy.stats as stats
from pathlib import Path
from sklearn.preprocessing import StandardScaler

def ensure_outputs_folder(outputs_path="./outputs"):
    """Create outputs folder if missing"""
    Path(outputs_path).mkdir(parents=True, exist_ok=True)

def calculate_metrics(df):
    """Calculate sentiment performance metrics"""
    metrics = df.groupby('sentiment_category').agg({
        'pnl': ['mean', 'count', lambda x: (x > 0).mean()],
        'size_usd': 'sum'
    }).round(4)
    
    metrics.columns = ['Avg PnL', 'Trade Count', 'Win Rate', 'Total Volume']
    metrics['Win Rate %'] = metrics['Win Rate'] * 100
    metrics = metrics[['Win Rate %', 'Avg PnL', 'Trade Count', 'Total Volume']]
    return metrics.sort_values('Win Rate %', ascending=False)

def top_traders_analysis(df):
    """Top traders by total PnL"""
    top_traders = df.groupby('account').agg({
        'pnl': 'sum',
        'size_usd': 'sum',
        'pnl': 'count'
    }).round(2)
    top_traders.columns = ['Total PnL', 'Total Volume', 'Trade Count']
    top_traders['Win Rate'] = df.groupby('account')['pnl'].apply(lambda x: (x > 0).mean() * 100)
    return top_traders.sort_values('Total PnL', ascending=False)

def statistical_tests(df):
    """Statistical significance tests"""
    # ANOVA test
    groups = [group['pnl'].values for name, group in df.groupby('sentiment_category')]
    anova_f, anova_p = stats.f_oneway(*groups)
    
    # Correlation matrix
    corr_data = df[['pnl', 'size_usd', 'fear_greed_index']].dropna()
    correlation_matrix = corr_data.corr()
    
    return {
        'anova_f': anova_f,
        'anova_p': anova_p,
        'correlation_matrix': correlation_matrix
    }

def save_outputs(df, metrics, top_traders, stats, outputs_path="./outputs"):
    """Save all outputs with flexible paths"""
    outputs_path = Path(outputs_path)
    ensure_outputs_folder(outputs_path)
    
    # Save files
    metrics.to_csv(outputs_path / 'performance_table.csv')
    top_traders.to_csv(outputs_path / 'top_traders.csv')
    stats['correlation_matrix'].to_csv(outputs_path / 'correlation_matrix.csv')
    df.to_csv(outputs_path / 'full_analysis_data.csv', index=False)
    
    print(f"✅ Saved to {outputs_path}")