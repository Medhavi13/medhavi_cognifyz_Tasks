import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


file_path = 'C:\\Users\\medhavi\\Downloads\\Dataset .csv'
dataset = pd.read_csv(file_path)


dataset.fillna('', inplace=True)

dataset['combined_features'] = dataset['Cuisines'] + ' ' + dataset['Price range'].astype(str)

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['combined_features'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(user_cuisine_preference, user_price_range, top_n=10):
    user_combined_features = f"{user_cuisine_preference} {user_price_range}"
    user_tfidf = tfidf_vectorizer.transform([user_combined_features])
    user_cosine_sim = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    
    top_indices = user_cosine_sim.argsort()[-top_n:][::-1]
    return dataset.iloc[top_indices][['Restaurant Name', 'Cuisines', 'Price range', 'Aggregate rating']]

user_cuisine_preference = 'Japanese'
user_price_range = 3

recommendations = get_recommendations(user_cuisine_preference, user_price_range)
print(recommendations)
