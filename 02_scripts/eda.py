import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned datasets
airbnb = pd.read_csv("../01_data/clean_airbnb.csv")
youtube = pd.read_csv("../01_data/clean_youtube.csv")

print("Datasets loaded successfully")

# ----------------------------
# 1. BASIC INFO
# ----------------------------
print("\nAirbnb Info:")
print(airbnb.info())

print("\nYouTube Info:")
print(youtube.info())

# ----------------------------
# 2. AIRBNB ANALYSIS
# ----------------------------

# Top 5 expensive locations
top_locations = airbnb.groupby("neighbourhood_group")["price"].mean().sort_values(ascending=False)

print("\nTop Locations by Price:")
print(top_locations.head())

# Plot Airbnb prices
top_locations.head().plot(kind='bar', title="Top Airbnb Locations by Price")
plt.show()

# ----------------------------
# 3. YOUTUBE ANALYSIS
# ----------------------------

# Top 5 most viewed videos
top_views = youtube.sort_values(by="views", ascending=False).head(5)

print("\nTop 5 Most Viewed Videos:")
print(top_views[["title", "views"]])

# Plot views vs likes
plt.scatter(youtube["views"], youtube["likes"])
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Views vs Likes")

plt.savefig("../03_outputs/views_vs_likes.png")
plt.show()