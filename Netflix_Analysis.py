import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
print(df)
df.head()
df.columns
df.info()
plt.figure(figsize=(12,6))

#Calculating sum of null values from each coloumn
print(df.isnull().sum())
plt.bar(df.columns,df.isnull().sum(),color = 'red',label='Null Values Sum')
plt.xlabel("Columns")
plt.ylabel("Null Values")
plt.title("Sum of all Null Values for each Column")
plt.xticks(rotation=75)
plt.tight_layout()
plt.legend()
plt.savefig("bar_chart.png")
plt.show()

#removing the useless column
df.drop(columns='description', inplace=True)

#removing all the null values holding rows for cleaning of data
df.dropna(inplace=True)

#now suming and checking all the the non null rows
print(df.isnull().sum())
plt.plot(df.columns,df.isnull().sum(),color = 'red',label='Null Values Sum')
plt.xlabel("Columns")
plt.ylabel("Null Values")
plt.title("Sum of all Null Values for each Column")
plt.xticks(rotation=75)
plt.tight_layout()
plt.legend()
plt.savefig("line_chart.png")
plt.show()

#How many shows are Movies vs. TV Shows?
print(df['type'].value_counts())
type_counts = df['type'].value_counts()

plt.pie( type_counts.values,labels= type_counts.index,autopct = '%1.1f%%', colors=['red','blue'])
plt.title("Movies vs. TV Shows")
plt.grid()
plt.savefig("pie_chart.png")
plt.show()

#There are more Movies than TV Shows on Netflix.





#What’s the most common rating (PG, R, TV-14)?
plt.figure(figsize=(12,6))
print(df['rating'].value_counts())
type_count2= df['rating'].value_counts()
plt.bar(type_count2.index,type_count2.values,color='blue',label='Number')
plt.xlabel("Ratings")
plt.ylabel("Numbers")
plt.title("Most common rating (PG, R, TV-14)")
plt.legend()
plt.savefig("bar_chart2.png")
plt.show()

#TV-MA is the most common content rating.




#Which year had the highest number of releases?
print(df['release_year'].value_counts().head(10))
print(df['release_year'].value_counts().sort_index(ascending=True))
type_count3 = df['release_year'].value_counts().head(10)
plt.plot(type_count3.index,type_count3.values,color='green',label='Number')
plt.xlabel("Release year")
plt.ylabel("Numbers")
plt.title("Highest number of releases")
plt.legend()
plt.savefig("line_chart2.png")
plt.show()

#Highest number of releases were in 2019



#Top 10 countries producing Netflix content
print(df["country"].value_counts().head())
type_count4= df["country"].value_counts().head(10)
plt.figure(figsize=(12,6))
plt.bar(type_count4.index,type_count4.values,color='purple',label='Number')
plt.xlabel("Countries")
plt.ylabel("Numbers")
plt.title("Top 10 countries producing Netflix content")
plt.legend()
plt.savefig("bar_chart3.png")
plt.show()



#Average duration of movies
movies = df[df['type'] == 'Movie']
movies['duration_mins'] = movies['duration'].str.replace(' min','',regex=False).astype(int)
print(movies['duration_mins'].mean())
plt.figure(figsize=(8,5))
plt.hist(movies['duration_mins'],bins=5,color='yellow',edgecolor='black')
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.title("Distribution of Movie Durations")
plt.savefig("hist_chart.png")
plt.show()
