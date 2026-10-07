#!/usr/bin/env python
# coding: utf-8

# # Lecture 2 — Class Exercise
# # Bar Charts: World Happiness Report 2023
# 
# ---
# 
# > **Your task:** Create **2 polished bar charts** using the World Happiness Report dataset.  
# > **Push to:** `week02/lecture02_exercise.ipynb` in **your own GitHub repo** before the end of class.
# 
# ---
# 
# ### Rules to keep in mind 💡
# 1. Every bar chart **must have a zero baseline** — no exceptions
# 2. Every chart **must have an insight title**, not a topic title
# 3. Aim for **professional quality** — clean background, readable font, no clutter
# 4. Horizontal bars for long category names
# 
# ---
# 

# ## Setup — Run this cell first
# 

# In[1]:


import pandas as pd
import numpy as np

# World Happiness Report 2023 — representative data
# Source: https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2023

df = pd.read_csv(r'C:\Users\user\Documents\GitHub\data-viz-class-material-w2026\data\world_happiness_2023.csv')
df.columns = ['Country','Region','Happiness_Score','GDP','Social_Support',
              'Life_Expectancy','Freedom','Generosity','Corruption']


print(f"Dataset: {len(df)} countries, {len(df.columns)} columns")
print(df.head())


# In[2]:


import plotly.express as px
import plotly.graph_objects as go

# Explore the dataset before you start
print("Regions in dataset:")
print(df['Region'].value_counts())
print("\nScore range:", df['Happiness_Score'].min(), "–", df['Happiness_Score'].max())
print("\nBottom 10 countries:")
print(df.nsmallest(10, 'Happiness_Score')[['Country','Region','Happiness_Score']])


# ---
# ## Task 1 — Regional Comparison Bar Chart
# 
# **What to build:** A horizontal bar chart showing the **average happiness score by region**, sorted from highest to lowest.
# 
# **Requirements:**
# - Horizontal orientation (category names are long)
# - Sorted by score, descending (so the happiest region is at the top)
# - Zero baseline on x-axis
# - At least one design choice that goes beyond the Plotly default (colour, annotation, labels, etc.)
# - An insight title that answers: *which region stands out and why does it matter?*
# 
# **Hint:** Use `df.groupby('Region')['Happiness_Score'].mean()` to compute the averages.
# 

# In[4]:


# Task 1: Regional comparison bar chart
# -------------------------------------

# Step 1: Compute average happiness score by region
region_avg = (df.groupby('Region')['Happiness_Score']
              .mean()
              .reset_index()
              .sort_values('Happiness_Score'))  # sort for horizontal bar

print(region_avg)

# Step 2: Build your chart

fig = px.bar(
    data_frame=region_avg.sort_values('Happiness_Score'),       # Rule 2: sort
    x='Region', y='Happiness_Score',
    orientation='h',                  # Rule 3: horizontal
    title='Top 10 Happiest Countries 2023',
    height=500
      
)
fig.show()


# ---
# ## Task 2 — Bottom vs. Top: A Contrast Story
# 
# **What to build:** A bar chart that highlights the **gap between the happiest and least happy countries**, focusing on a specific insight.
# 
# **Requirements:**
# - Show the **top 8 AND bottom 8 countries** together (16 bars total)
# - Use **colour** to distinguish the two groups (not Plotly's default rainbow)
# - Add a **visual separator or annotation** that emphasises the gap
# - Insight title that tells the story of the gap
# 
# **Hint:** Use `pd.concat([df.nlargest(8,'Happiness_Score'), df.nsmallest(8,'Happiness_Score')])` to get both groups.
# 
# **Stretch goal:** Add a vertical reference line showing the global average.
# 

# In[ ]:


# Task 2: Top 8 vs. Bottom 8 contrast
# ------------------------------------

# Step 1: Get top and bottom countries
top8 = df.nlargest(8, 'Happiness_Score').copy()
top8['Group'] = 'Top 8'
bottom8 = df.nsmallest(8, 'Happiness_Score').copy()
bottom8['Group'] = 'Bottom 8'

combined = pd.concat([bottom8, top8]).sort_values('Happiness_Score')
global_avg = df['Happiness_Score'].mean()
print(f"Global average: {global_avg:.2f}")

# Step 2: Build your chart
# YOUR CODE HERE


# ---
# ## Done? Stretch Goal
# 
# If you finish both tasks with time to spare, try this:
# 
# **Task 3 (stretch):** Build a **grouped bar chart** comparing 2 sub-factors (e.g. `GDP_per_capita` and `Freedom`) across the 5 most populated regions. Use colour meaningfully and write an insight title.
# 
# Regions to include: `'Western Europe'`, `'Latin America'`, `'East Asia'`, `'Sub-Saharan Africa'`, `'South Asia'`
# 

# In[ ]:


# Stretch goal — grouped bar chart
# YOUR CODE HERE

