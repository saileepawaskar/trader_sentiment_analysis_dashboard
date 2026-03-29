from data_preprocessing import load_and_clean_data
import pandas as pd

print("=== YOUR FILES ===")
df = load_and_clean_data("./data")[2]
print(f"Shape: {df.shape}")
print("\nFirst 3 rows:")
print(df[['account', 'entry_price', 'exit_price', 'pnl', 'sentiment_category']].head(3))
print("\nSentiment distribution:")
print(df['sentiment_category'].value_counts())