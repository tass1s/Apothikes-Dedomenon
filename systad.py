import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA


# Φόρτωση των δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Προετοιμασία δεδομένων: Εξαγωγή κειμένου και καθαρισμός
df['text_clean'] = df['text'].str.replace('[^\w\s]', '').str.lower()  # αφαίρεση σημείων στίξης και μετατροπή σε πεζά

# Εξαγωγή χαρακτηριστικών με TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['text_clean'])

# Εφαρμογή K-means
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(tfidf_matrix)
labels = kmeans.labels_

# Προσάρτηση των ετικετών συστάδας στο DataFrame
df['cluster'] = labels

# Οπτικοποίηση των αποτελεσμάτων
fig, ax = plt.subplots()
scatter = ax.scatter(df.index, labels, c=labels, cmap='viridis', alpha=0.6)
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)
plt.title('Tweets Clustering')
plt.xlabel('Tweet Index')
plt.ylabel('Cluster')
plt.show()



# Ανάλυση των πιο συχνών λέξεων σε κάθε συστάδα
def most_common_words(text_list):
    words = ' '.join(text_list).split()
    return Counter(words).most_common(10)

# Ομαδοποίηση των tweets ανά συστάδα και εξαγωγή των πιο συχνών λέξεων
cluster_common_words = df.groupby('cluster')['text_clean'].apply(lambda texts: most_common_words(texts))
print(cluster_common_words)




# Εφαρμογή t-SNE για μείωση των διαστάσεων
tsne = TSNE(n_components=2, perplexity=30, n_iter=300)
tsne_features = tsne.fit_transform(tfidf_matrix.toarray())

# Οπτικοποίηση με t-SNE
plt.figure(figsize=(10, 8))
plt.scatter(tsne_features[:, 0], tsne_features[:, 1], c=df['cluster'], cmap='viridis', alpha=0.5)
plt.colorbar(label='Cluster')
plt.title('t-SNE of Tweets')
plt.xlabel('t-SNE Feature 1')
plt.ylabel('t-SNE Feature 2')
plt.show()

