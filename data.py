import pandas as pd
import matplotlib.pyplot as mat  
import seaborn as sns

#providing the url of my data which I want to show case
url = r"C:\Users\ASUS\Downloads\netflix_titles (1).csv"
df = pd.read_csv(url)

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

# Data Cleaning:
# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)
df_cleaned = df.dropna() #remove the missing value

# Filter: 
# Show only movies released after 2015
filtered_movies = df_cleaned[(df_cleaned['type'] == 'Movie') & (df_cleaned['release_year'] > 2015)]
print("\nMovies released after 2015:")
print(filtered_movies[['title', 'release_year']])


# Grouping:
#  Count the number of titles by type (Movies/TV Shows)
type_counts = df['type'].value_counts()
print("\nCount of Titles by Type:")
print(type_counts)


# Aggregation: 
# Number of titles by release year
titles_by_year = df.groupby('release_year').size()
print("\nNumber of Titles by Release Year:")
print(titles_by_year)

# Visualizations

# 1. Bar Plot: Count of Movies and TV Shows
type_counts.plot(kind='bar', color=['blue', 'orange'], title='Count of Movies and TV Shows')
mat.xlabel('Type')
mat.ylabel('Count')
mat.show()

# 2. Line Plot: Number of Titles by Release Year
mat.figure(figsize=(10, 6))
titles_by_year.plot(kind='line', marker='o', color='green', title='Number of Titles by Release Year')
mat.xlabel('Year')
mat.ylabel('Number of Titles')
mat.grid()
mat.show()

# 3. Top 10 Countries with Most Titles
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
mat.title('Top 10 Countries by Number of Titles')
mat.xlabel('Number of Titles')
mat.ylabel('Country')
mat.show()
