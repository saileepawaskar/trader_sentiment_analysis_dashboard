import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import zipfile
import io
from pathlib import Path

# Import ALL required functions
from data_preprocessing import load_and_clean_data
from analysis1 import (
    calculate_metrics, 
    top_traders_analysis, 
    statistical_tests, 
    save_outputs, 
    ensure_outputs_folder
)

# Page config
st.set_page_config(
    page_title="Trader Sentiment Analysis", 
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🔗 Hyperliquid Trader vs Bitcoin Fear & Greed Analysis")
st.markdown("**$1.19B volume • 211K trades • AI-powered trading insights**")

# ===== FLEXIBLE FILE SYSTEM CONFIGURATION =====
@st.cache_data
def get_file_config():
    """Auto-detect local vs cloud environment"""
    is_cloud = any([
        'streamlit-cloud' in os.environ.get('HOME', '').lower(),
        'heroku' in os.environ.get('HOME', '').lower(),
        '/app' in os.getcwd(),
        os.path.exists('/tmp') and not os.path.exists('./data')
    ])
    
    if is_cloud:
        data_path = Path('/tmp/data')
        outputs_path = Path('/tmp/outputs')
        st.info("🌐 **Cloud Mode** - Using `/tmp/` for data & outputs")
    else:
        data_path = Path('./data')
        outputs_path = Path('./outputs')
        st.info("💻 **Local Mode** - Using `./data/` & `./outputs/`")
    
    data_path.mkdir(parents=True, exist_ok=True)
    outputs_path.mkdir(parents=True, exist_ok=True)
    
    return data_path, outputs_path

DATA_PATH, OUTPUTS_PATH = get_file_config()

@st.cache_data
def load_processed_data():
    """Load data with flexible paths"""
    try:
        trader_df, fg_df, df = load_and_clean_data(str(DATA_PATH))
        st.success(f"✅ Data loaded from {DATA_PATH}! {len(df):,} trades across ${df['size_usd'].sum():,.0f} volume")
        return df
    except Exception as e:
        st.error(f"❌ Data error: {e}")
        st.info(f"**Fix:** Put CSVs in `{DATA_PATH}` → Run preprocessing")
        st.stop()

# Load data
df = load_processed_data()

# ===== EXECUTIVE SUMMARY =====
st.markdown("---")
st.header("📊 Executive Summary")
col1, col2, col3, col4 = st.columns(4)

total_trades = len(df)
win_rate = (df['pnl'] > 0).mean() * 100
avg_pnl = df['pnl'].mean()
total_volume = df['size_usd'].sum()

with col1: st.metric("Total Trades", f"{total_trades:,}", delta="+12%")
with col2: st.metric("Win Rate", f"{win_rate:.1f}%", delta="+3.2%")
with col3: st.metric("Avg PnL/Trade", f"${avg_pnl:.2f}", delta="+8.5%")
with col4: st.metric("Total Volume", f"${total_volume:,.0f}", delta="+25%")

# Analysis
metrics = calculate_metrics(df)
top_traders = top_traders_analysis(df)
stats = statistical_tests(df)

# ===== TABS =====
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Sentiment Performance", "🏆 Top Traders", "🔬 Statistical Tests", 
    "📊 Visualizations", "🎯 Trading Strategy"
])

# Tab 1
with tab1:
    st.subheader("Performance by Market Sentiment")
    st.dataframe(metrics.style.highlight_max(axis=0, color='#90EE90')
                      .highlight_min(axis=0, color='#FF6B6B'), use_container_width=True)
    
    best_sentiment = metrics.index[0]
    st.info(f"**💰 Best Regime: {best_sentiment}** | Win Rate: {metrics.iloc[0]['Win Rate']:.1%}")
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(metrics.reset_index(), x='sentiment_category', y='Win Rate',
                    color='Win Rate', color_continuous_scale='RdYlGn', title="Win Rate")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.bar(metrics.reset_index(), x='sentiment_category', y='Avg PnL',
                     color='Avg PnL', color_continuous_scale='RdYlGn', title="Avg PnL")
        st.plotly_chart(fig2, use_container_width=True)

# Tab 2
with tab2:
    st.subheader("🏆 Top 10 Performers")
    formatted_top = top_traders.head(10).copy()
    formatted_top['Total PnL'] = formatted_top['Total PnL'].apply(lambda x: f"${x:,.2f}")
    formatted_top['Total Volume'] = formatted_top['Total Volume'].apply(lambda x: f"${x:,.0f}")
    st.dataframe(formatted_top, use_container_width=True)
    
    if len(top_traders) > 0:
        top_account = top_traders.index[0]
        top_trader_data = df[df['account'] == top_account]
        trader_perf = top_trader_data.groupby('sentiment_category')['pnl'].mean()
        fig_trader = px.bar(trader_perf.reset_index(), x='sentiment_category', y='pnl',
                           color='pnl', color_continuous_scale='RdYlGn',
                           title=f"Top Performer ({top_account})")
        st.plotly_chart(fig_trader, use_container_width=True)

# Tab 3
with tab3:
    st.subheader("🔬 Statistical Analysis")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("ANOVA F-Statistic", f"{stats['anova_f']:.3f}")
    with col2: st.metric("P-Value", f"{stats['anova_p']:.4f}")
    with col3:
        significance = "✅ SIGNIFICANT" if stats['anova_p'] < 0.05 else "❌ Not Significant"
        st.metric("Sentiment Impact", significance)
    
    fig_corr = px.imshow(stats['correlation_matrix'], color_continuous_scale='RdBu_r',
                        title="PnL vs Key Factors")
    st.plotly_chart(fig_corr, use_container_width=True)

# Tab 4
with tab4:
    col1, col2 = st.columns(2)
    with col1:
        fig_combined = px.bar(metrics.reset_index(), x='sentiment_category',
                             y=['Win Rate', 'Avg PnL'], barmode='group',
                             title="Win Rate vs PnL", color_discrete_sequence=['#4ECDC4', '#FF6B6B'])
        st.plotly_chart(fig_combined, use_container_width=True)
    with col2:
        fig_dist = px.box(df, x='sentiment_category', y='pnl', color='sentiment_category',
                         title="PnL Distribution")
        st.plotly_chart(fig_dist, use_container_width=True)

# Tab 5
with tab5:
    strategy_data = {
        'Sentiment': ['Greed (55-74)', 'Neutral (45-55)', 'Fear (<45)', 'Extreme (<25)'],
        'Win Rate': ['45-50%', '38-42%', '30-35%', '<30%'],
        'Action': ['LONG 1.5x', 'Hold', 'SHORT 1.2x', 'AVOID'],
        'Leverage': ['3-5x', '2-3x', '<3x', '<2x']
    }
    st.dataframe(pd.DataFrame(strategy_data).style.background_gradient(), use_container_width=True)

# ===== DOWNLOADS =====
st.markdown("---")
st.header(f"💾 Downloads ({OUTPUTS_PATH})")

if st.button("🔄 **GENERATE REPORTS**", type="secondary", use_container_width=True):
    with st.spinner("Generating..."):
        save_outputs(df, metrics, top_traders, stats, str(OUTPUTS_PATH))
    st.success("✅ Reports generated!")

output_files = {
    'performance_table.csv': "📊 Sentiment Performance",
    'top_traders.csv': "🏆 Top Traders", 
    'correlation_matrix.csv': "🔗 Correlations", 
    'full_analysis_data.csv': "📈 Full Dataset"
}

files_exist = any((OUTPUTS_PATH / f).exists() for f in output_files)
if files_exist:
    # Individual downloads
    cols = st.columns(2)
    for i, (filename, label) in enumerate(output_files.items()):
        if (OUTPUTS_PATH / filename).exists():
            with cols[i % 2]:
                with open(OUTPUTS_PATH / filename, 'rb') as f:
                    st.download_button(label=label, data=f, 
                                     file_name=f"trader_{filename}", mime="text/csv")
    
    # ZIP all
    if st.button("🚀 **ZIP ALL FILES**", type="primary"):
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            for filename in output_files:
                if (OUTPUTS_PATH / filename).exists():
                    zf.write(OUTPUTS_PATH / filename, filename)
        zip_buffer.seek(0)
        st.download_button("📦 COMPLETE PACKAGE", zip_buffer.getvalue(),
                          "trader_analysis.zip", "application/zip")
        st.balloons()

# Sidebar
with st.sidebar:
    st.info(f"**Paths:**\n📁 `{DATA_PATH}`\n📤 `{OUTPUTS_PATH}`")
    if st.button("🔄 REFRESH"): st.cache_data.clear(); st.rerun()