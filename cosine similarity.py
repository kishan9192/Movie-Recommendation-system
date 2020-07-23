from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

text = ["London Paris London", "Paris Paris London"]

# sklearn find count of words in text
# There's a class in SKlearn called count vectorizer

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)

print(count_matrix.toarray())
 
# Now for finding out the similarity
# sklearn cosine_similarity of two vectors

# it's a function not a class. SO we don't need an object
from sklearn.metrics.pairwise import cosine_similarity

similarity_scores = cosine_similarity(count_matrix)

print(similarity_scores)