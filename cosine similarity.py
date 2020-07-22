from sklearn.feature_extraction.text import CountVectorizer


text = ["London Paris London", "Paris Paris London"]

# sklearn find count of words in text
# There's a class in SKlearn called count vectorizer

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)

print(count_matrix)
