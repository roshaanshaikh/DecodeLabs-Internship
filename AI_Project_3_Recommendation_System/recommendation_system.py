# DecodeLabs Artificial Intelligence Project 3
# AI Recommendation Logic - Tech Stack Recommender

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset: Career roles with required skills
roles = {
    "Data Scientist": "python sql machine learning data analysis statistics",
    "DevOps Engineer": "aws docker kubernetes cloud automation linux",
    "Backend Developer": "java python sql api database backend development",
    "Cloud Architect": "aws cloud architecture networking automation",
    "AI Engineer": "python machine learning deep learning ai algorithms"
}

# Take minimum three user skills as input
user_input = input("Enter your three skills separated by commas: ")

user_profile = user_input.replace(",", " ")

# Combine user input with role descriptions
documents = list(roles.values()) + [user_profile]

# TF-IDF Vector Mapping
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

# Calculate cosine similarity
similarity_scores = cosine_similarity(vectors[-1], vectors[:-1])[0]

# Rank recommendations
ranking = sorted(
    zip(roles.keys(), similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Recommended Career Paths:")
for role, score in ranking[:3]:
    print(role, "-", round(score * 100, 2), "% match")
