import pandas as pd
import numpy as np
import sqlite3

# Load dataset
df = pd.read_csv("sales_data.csv")

# ---------------- Q1 ----------------
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# ---------------- Q2 ----------------
df["revenue"] = np.round(
    df["quantity"] * df["unit_price"] * (1 - df["discount_pct"] / 100),
    2
)

print("\nRevenue Stats:")
print("Min:", np.min(df["revenue"]))
print("Max:", np.max(df["revenue"]))
print("Mean:", np.mean(df["revenue"]))

# ---------------- Q3 ----------------
filtered = df[
    (df["status"] == "Completed") &
    (df["category"] == "Electronics")
]

top3 = filtered.sort_values(by="revenue", ascending=False).head(3)
print("\nTop 3 Orders:\n", top3[["order_id", "revenue"]])

# ---------------- Q4 ----------------
grouped = df.groupby("category").agg({
    "revenue": "sum",
    "discount_pct": "mean",
    "order_id": "count"
}).rename(columns={"order_id": "num_orders"})

print("\nCategory Summary:\n", grouped.sort_values(by="revenue", ascending=False))

# ---------------- Q5 ----------------
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month_name()

monthly = df.groupby("month")["revenue"].sum()
print("\nMonthly Revenue:\n", monthly)
print("\nBest Month:", monthly.idxmax())

# ---------------- Q6 ----------------
percentiles = np.percentile(df["unit_price"], [25, 50, 75])
print("\nPercentiles:", percentiles)

p75 = np.percentile(df["revenue"], 75)

df["order_tier"] = np.where(df["revenue"] > p75, "High Value", "Standard")

# ---------------- Q7 ----------------
pivot = pd.pivot_table(
    df,
    values="revenue",
    index="category",
    columns="status",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:\n", pivot)

# ---------------- Q8 ----------------
conn = sqlite3.connect("sales.db")
df.to_sql("orders", conn, if_exists="replace", index=False)

print("\nSQL Revenue per Category:")
print(pd.read_sql("SELECT category, SUM(revenue) FROM orders GROUP BY category", conn))

print("\nCancelled Orders:")
print(pd.read_sql("SELECT * FROM orders WHERE status='Cancelled'", conn))

conn.close()
