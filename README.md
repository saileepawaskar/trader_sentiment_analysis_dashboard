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
├── analysis.py              # 📈 Metrics & stats
├── data/                    # 📊 YOUR CSVs HERE
│   ├── *.csv                # CSV files
├── outputs/                 # 💾 Auto-generated reports
├── requirements.txt         # 📦 Dependencies
└── README.md                # 📖 This file
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