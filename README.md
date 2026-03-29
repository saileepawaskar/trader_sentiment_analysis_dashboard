# Trader Sentiment Analysis Dashboard

🔗 **Hyperliquid Trader vs Bitcoin Fear & Greed Analysis**  
**$1.19B volume -  211K trades -  AI-powered trading insights**


## 🎯 **What It Does**
Professional dashboard analyzing **211K Hyperliquid trades** against **Bitcoin Fear & Greed Index**:

- 📊 **Win Rate by Sentiment** (Greed: 48% vs Fear: 32%)
- 🏆 **Top 10 Traders** ($2.3M PnL leader)
- 🔬 **Statistical Tests** (ANOVA p<0.001 - sentiment matters!)
- 🎯 **Trading Strategy** (LONG in Greed, SHORT in Fear)
- 💾 **Export CSVs** (Full 1.19B volume dataset)

## 🚀 **Quick Start (2 minutes)**

```bash
# 1. Clone & Install
git clone <your-repo>
cd trader-sentiment-dashboard
pip install -r requirements.txt

# 2. Add your data
# Put CSVs in data/ folder:
#   data/trader_data.csv
#   data/fear_greed.csv

# 3. Run
streamlit run app.py
```

**Opens:** `http://localhost:8501`

## 📁 **Folder Structure**
```
trader-sentiment-dashboard/
├── app.py                   # 🎮 Main dashboard
├── data_preprocessing.py    # 🔧 Data loading & cleaning
├── analysis.py             # 📈 Metrics & stats
├── data/                   # 📊 YOUR CSVs HERE
│   ├── trader_data.csv     # Account, PnL, size_usd, timestamp
│   └── fear_greed.csv      # Timestamp, fear_greed_index (0-100)
├── outputs/                # 💾 Auto-generated reports
├── requirements.txt        # 📦 Dependencies
└── README.md              # 📖 This file
```

## 📈 **Expected Data Format**

**trader_data.csv:**
```csv
account,timestamp,pnl,size_usd,leverage
0xabc123,2024-01-01 10:30:00,150.50,50000,5x
0xdef456,2024-01-01 11:15:00,-75.20,25000,3x
```

**fear_greed.csv:**
```csv
timestamp,fear_greed_index
2024-01-01,72
2024-01-02,45
```

## 🎛️ **Dashboard Features**

| Tab | What You Get |
|-----|--------------|
| **📈 Sentiment** | Win rates + PnL by Fear/Greed |
| **🏆 Top Traders** | #1 trader: $2.3M PnL analysis |
| **🔬 Stats** | ANOVA p-value + correlations |
| **📊 Charts** | Interactive Plotly visuals |
| **🎯 Strategy** | LONG Greed, SHORT Fear rules |

**Downloads:**
- 4 CSVs (performance, traders, correlations, full data)
- One-click ZIP package

## 🛠️ **Requirements**

```bash
pip install streamlit==1.38.0 pandas==2.2.2 plotly==5.24.0 numpy scipy
```

**Full `requirements.txt`:**
```txt
streamlit==1.38.0
pandas==2.2.2
plotly==5.24.0
numpy==2.1.1
scipy==1.14.1
```

## 🔍 **Troubleshooting**

| Error | Fix |
|--------|-----|
| `data/trader_data.csv not found` | Put CSVs in `data/` folder |
| `ModuleNotFoundError` | Ensure `data_preprocessing.py` & `analysis.py` exist |
| Slow loading | Use upload feature in app |
| No outputs | Click **GENERATE REPORTS** first |

## 💾 **Outputs Generated**
```
outputs/
├── 1_sentiment_performance.csv
├── 2_top_traders.csv
├── 3_correlations.csv
└── 4_full_dataset.csv (211K trades)
```

## 📱 **Usage Workflow**
```
1. 🗂️ Add CSVs to data/
2. ▶️ streamlit run app.py
3. 📊 Explore 5 tabs
4. 🔄 GENERATE REPORTS
5. 💾 ZIP ALL FILES → 📧 Share!
```

## 🤝 **Support**
- **Issues?** Check Troubleshooting table
- **Customize?** Edit `analysis.py` functions
- **Data questions?** Adjust `merge_and_clean()` in `data_preprocessing.py`

## 📊 **Sample Metrics**
```
Total Trades: 211,472
Win Rate: 42.3%
Avg PnL: $18.47
Total Volume: $1.19B
Best Sentiment: Greed (48.2% win rate)
```

***

*🏆 Built for quantitative traders -  Hyperliquid + Bitcoin Fear/Greed analysis*  
*Last updated: March 2026*