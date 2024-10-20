import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt
import seaborn as sn

# Giving Title
st.title("Covid 19 Data Analysis 📊")

st.write(" ")
st.write(" ")

st.header("A) Data Preprocessing")
st.write(" ")

# First five rows
st.subheader("1. Visualizing the first five rows of the dataset")
df=pd.read_csv('country_wise_latest.xls')
st.write(df.head())
st.write(" ")
#####################################################


# Last five rows
st.subheader("2. Visualizing the last five rows of the dataset")
st.write(df.tail())
st.write(" ")
#####################################################################

# Shape of the dataset
st.subheader("3. Shape of the dataset")
st.write(df.shape)
st.write(" ")
#####################################################################

# Numerical columns of the dataset
st.subheader("4. Numerical Columns of the dataset")
st.write(df.select_dtypes(include=['int64','float64']))
st.write(" ")
#####################################################################

# Categorical columns of the dataset
st.subheader("5. Categorical Columns of the dataset")
st.write(df.select_dtypes(include=['object']))
st.write(" ")
#####################################################################

# Missing values of the dataset
st.subheader("6. Missing values of the dataset")
st.write(df.isnull().sum())
st.write(" ")
#####################################################################

# Duplicated values of the dataset
st.subheader("7. Duplicated values of the dataset")
st.write(df.duplicated().sum())
st.write(" ")
#####################################################################

# Unique values of the dataset
st.subheader("8.  Unique values of the dataset")
st.write(df.nunique())
st.write(" ")
#####################################################################

# Showing extra statistical measures of the dataset
st.subheader("9.  Showing extra statistical measures of the dataset")
st.write(df.describe())
st.write(" ")
#####################################################################

st.write("--------------------------------------------------------------------")

st.write(" ")

st.header("B) Exploratory Data Analysis || EDA 📈📉")

st.write(" ")

# Part 1
st.subheader("1) Which Countries had the highest number of confirmed cases?")
high_confirm_cases=df.nlargest(10, 'Confirmed')

# Plot
ax=px.bar(high_confirm_cases,
      x='Country/Region',
      y='Confirmed',
     
      color='Country/Region')
st.plotly_chart(ax)

# Alternative 
st.error("Alternative Solution")

case=df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(20).reset_index()

plt.figure(figsize=(16,7))
sn.barplot(x='Country/Region', y='Confirmed', data=case, palette="magma")
plt.xlabel('Countries ', fontsize=18)
plt.ylabel('Number of Confirmed Cases', fontsize=18)
plt.xticks(rotation=45)
st.pyplot(plt)

st.write("-----------------------------------------------------------")
#####################################################################

# Part 2
st.subheader("2) Distribution of Confirmed cases across different WHO regions?")

# Plot
ax=px.pie(df, 
      values='Confirmed',
      names='WHO Region',
     
      color_discrete_sequence=px.colors.sequential.Viridis_r)
st.plotly_chart(ax)

# Alternative
st.error("Alternative Solution")
case_who=df.groupby('WHO Region')['Confirmed'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 4))
sn.barplot(y='WHO Region', x='Confirmed', data=case_who, palette="crest")
plt.xlabel('Number of Confirmed Cases', fontsize=14)
plt.ylabel('WHO Region', fontsize=14)
plt.xlim(0, case_who['Confirmed'].max() + 10000)  # Adding some padding to the x-axis
st.pyplot(plt)


st.write("-----------------------------------------------------------")
#####################################################################

# Part 3
st.subheader("3) What were the trends in new cases, new deaths and new recoveries in each country?")

# Plot
ax=px.scatter(df,
          x='New cases',
          y='New deaths',
          size='New recovered',
          color='Country/Region'
          )
st.plotly_chart(ax)

st.write("-----------------------------------------------------------")
#####################################################################

# Part 4
st.subheader("4) What was the 1-week percentage increase in confirmed cases for each country?")

# Plot
ax=px.choropleth(df,
             locations='Country/Region',
             locationmode='country names',
             color='1 week % increase',
             hover_name='Country/Region',
             color_continuous_scale=px.colors.sequential.Magenta)
st.plotly_chart(ax)

# Alternative
st.error("Alternative Solution")
week_case=df.groupby('Country/Region')['1 week % increase'].sum().sort_values(ascending=False).reset_index().head(20)

plt.figure(figsize=(14,6))

plt.plot('Country/Region', '1 week % increase', data=week_case, color='tab:orange')
plt.plot('Country/Region', '1 week % increase', data=week_case, marker="o", color="red")

plt.grid()
plt.legend(["1 week % increase"], loc ="upper right")
plt.xticks(rotation = 45, fontweight = 'bold')
st.pyplot(plt)


st.write("-----------------------------------------------------------")
#####################################################################


# Part 5
st.subheader("5) How do death rates per 100 confirmed cases vary by WHO Region?")

# Plot
ax=px.box(df,
      x='WHO Region',
      y='Deaths / 100 Cases',
       color='WHO Region'
      )
st.plotly_chart(ax)

# Alternative
st.error("Alternative Solution")
death_case=df.groupby('WHO Region')['Deaths / 100 Cases'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 4))
sn.barplot(x='WHO Region', y='Deaths / 100 Cases', data=death_case, palette="viridis")
plt.ylabel('Number of Confirmed Cases')
plt.xlabel('WHO Region')
plt.xticks(rotation=45)
plt.show()
st.pyplot(plt)


st.write("-----------------------------------------------------------")
#####################################################################

# Part 6
st.subheader("6) What was the mortality rate (deaths per 100 confirmed cases) for each country?")

# Plot
ax=px.choropleth(df,
             locations='Country/Region',
            color='Deaths / 100 Cases',
             hover_name='Country/Region',
             locationmode='country names',
            
             color_continuous_scale=px.colors.sequential.Reds)
st.plotly_chart(ax)

# Alternative
st.error("Alternative Solution")
death_case_m=df.groupby('Country/Region')['Deaths / 100 Cases'].sum().sort_values(ascending=False).reset_index().head(20)

plt.figure(figsize=(16,6))
plt.fill_between('Country/Region', 'Deaths / 100 Cases', data=death_case_m,color='red', alpha=0.5,
                  edgecolor='black', linewidth=2)

plt.legend(["Deaths / 100 Cases"], loc ="upper right")
plt.xticks(rotation = 45, fontweight = 'bold')
st.pyplot(plt)

st.write("-----------------------------------------------------------")
#####################################################################

# Part 7
st.subheader("7) How many countries are in each WHO Region?")
who_region_count=df['WHO Region'].value_counts().reset_index()
# Plot
ax=px.bar(who_region_count,
      x='WHO Region',
      y='index',
     
      color='WHO Region')
st.plotly_chart(ax)

st.write("-----------------------------------------------------------")
#####################################################################

# Part 8
st.subheader("8) Treemap of COVID-19 confirmed cases by WHO Region and country")

# Plot
ax=px.treemap(df,
          path=['WHO Region', 'Country/Region'],
          values='Confirmed',
          
          height=800)
st.plotly_chart(ax)

st.write("-----------------------------------------------------------")
#####################################################################
