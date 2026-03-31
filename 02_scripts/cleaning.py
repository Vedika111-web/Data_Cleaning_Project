import pandas as pd

# -----------------------------
# 1. LOAD DATASETS
# -----------------------------
airbnb = pd.read_csv("airbnb.csv")
youtube = pd.read_csv("youtube_trending.csv")

print("Airbnb Data Loaded")
print("YouTube Data Loaded")

# -----------------------------
# 2. BASIC INFO
# -----------------------------
print("\n--- Airbnb Info ---")
print(airbnb.info())

print("\n--- YouTube Info ---")
print(youtube.info())

# -----------------------------
# 3. HANDLE MISSING VALUES
# -----------------------------
airbnb = airbnb.ffill()
youtube = youtube.ffill()

print("\nMissing values handled")

# -----------------------------
# 4. REMOVE DUPLICATES
# -----------------------------
airbnb = airbnb.drop_duplicates()
youtube = youtube.drop_duplicates()

print("Duplicates removed")

# -----------------------------
# 5. SIMPLE DATA CLEANING
# -----------------------------

# Airbnb: remove price outliers (if price exists)
if 'price' in airbnb.columns:
    airbnb = airbnb[airbnb['price'] < 1000]

# YouTube: remove videos with 0 views
if 'views' in youtube.columns:
    youtube = youtube[youtube['views'] > 0]

print("Basic cleaning done")

# -----------------------------
# 6. SAVE CLEAN DATA
# -----------------------------
airbnb.to_csv("clean_airbnb.csv", index=False)
youtube.to_csv("clean_youtube.csv", index=False)

print("\n✅ Cleaned files saved successfully!")