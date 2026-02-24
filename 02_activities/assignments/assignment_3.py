# Python Code for Data Visualization 
# DataSet used: Development Pipeline in Toronto https://open.toronto.ca/dataset/development-pipeline/
# Bar chart for displaying the pipeline by Status over time from 1995 - 2025

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset 
df = pd.read_csv(r"C:\Users\h_daw\dsi14\visualization\02_activities\assignments\Development Pipeline.csv")

# Convert date and extract year
df["Date Received"] = pd.to_datetime(df["Date Received"], errors="coerce")
df["Year"] = df["Date Received"].dt.year

# Remove rows with missing values
df_clean = df.dropna(subset=["Year", "Pipeline Status"])

# Create summary table (counts by year and status)
year_status = (
    df_clean.groupby(["Year", "Pipeline Status"])
    .size()
    .unstack(fill_value=0)
    .sort_index()
)

# Plot stacked bar chart
plt.figure(figsize=(10,6))
year_status.plot(kind="bar", stacked=True)

plt.title("Projects by Development Pipeline Status Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Projects")
plt.xticks(rotation=45, ha="right")

# Legend
plt.legend(title="Pipeline Status")
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Footer
footer_text = "Source: Development Pipeline Dataset | City of Toronto Open Data Portal"
plt.figtext(0.5, -0.02, footer_text, ha="center", fontsize=9)

plt.tight_layout()
plt.show()

# Second chart - Heatmap for displaying the pipeline by Status  and by Ward from 1995 - 2025 
# -----------------------------
# Settings you can change
# -----------------------------
TOP_N_WARDS = 10
STATUS_FILTER = None   # set to "Active" or "Built" or "Under Review" (or keep None for all)
MIN_YEAR = None        # e.g., 2010 to limit older years; keep None for all years
# -----------------------------

# Load dataset (adjust path if needed)
df = pd.read_csv(r"C:\Users\h_daw\dsi14\visualization\02_activities\assignments\Development Pipeline.csv")

# Convert date and extract year
df["Date Received"] = pd.to_datetime(df["Date Received"], errors="coerce")
df["Year"] = df["Date Received"].dt.year

# Clean required fields
df = df.dropna(subset=["Year", "Ward", "Pipeline Status"])
df["Ward"] = df["Ward"].astype(int)

# Optional: filter by status
if STATUS_FILTER is not None:
    df = df[df["Pipeline Status"] == STATUS_FILTER]

# Optional: filter by minimum year
if MIN_YEAR is not None:
    df = df[df["Year"] >= MIN_YEAR]

# Keep top N wards by number of records (to keep heatmap readable)
top_wards = df["Ward"].value_counts().head(TOP_N_WARDS).index
df = df[df["Ward"].isin(top_wards)]

# Build heatmap matrix: rows=Year, cols=Ward, values=Count of projects
heat = (
    df.groupby(["Year", "Ward"])
      .size()
      .unstack(fill_value=0)
      .sort_index()
)

# Plot heatmap (matplotlib only)
plt.figure(figsize=(12, 6))
plt.imshow(heat.values, aspect="auto")  # no manual colors specified
plt.colorbar(label="Number of Projects")

title_status = STATUS_FILTER if STATUS_FILTER is not None else "All Statuses"
plt.title(f"Development Projects Heatmap by Year and Ward ({title_status})")

plt.xlabel("Ward")
plt.ylabel("Year")

# Set axis tick labels
plt.xticks(range(len(heat.columns)), heat.columns, rotation=45, ha="right")
plt.yticks(range(len(heat.index)), heat.index)

plt.tight_layout()
plt.show()