import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################
#print(df[df.title == "Avatar"].values)

##Step 1: Read CSV File
df = pd.read_csv("movie_dataset.csv")
df.head()

df.columns
##Step 2: Select Features
features = ["keywords", "cast", "genres", "director"]

# iterate over all the features in features array, and 
# replace the nans with empty string

for i in features:
    df[i] = df[i].fillna('')


##Step 3: Create a column in DF which combines all selected features
# Using a try and except block to get the row that's producing the error
def combined_features(row):
    try:
        return row["keywords"] +" "+row["cast"]+" "+row["genres"]+" "+row["director"] 
    except:
        print("Error", row)
        
df["combined_features"] = df.apply(combined_features, axis = 1)

print ("Combined features:", df["combined_features"].head())


##Step 4: Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)
print(cosine_sim)

movie_user_likes = "Avatar"

## Step 6: Get index of this movie from its title
movie_index = get_index_from_title(movie_user_likes)


## Step 7: Get a list of similar movies in descending order of similarity score
similar_movies = list(enumerate(cosine_sim[movie_index]))

sorted_similar_movies = sorted(similar_movies, key = lambda x: x[1], reverse = True)
## Step 8: Print titles of first 50 movies

# passing the 0th element of tuple
i = 0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i += 1
    if i>50:
        break
