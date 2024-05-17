import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Φόρτωση δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Εξαγωγή κειμένου
texts = df['text']  # Προσαρμόζεις ανάλογα με τη στήλη

# Μετατροπή κειμένου σε αριθμητικά χαρακτηριστικά
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(texts)



num_clusters = 5  # Επιλέγεις τον κατάλληλο αριθμό συστάδων
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(X)

# Προσθήκη στηλών συστάδας στα αρχικά δεδομένα
df['cluster'] = kmeans.labels_

# Εμφάνιση των πιο συχνών λέξεων ή θεμάτων για κάθε συστάδα
for i in range(num_clusters):
    cluster_texts = df[df['cluster'] == i]['text']
    print(f"Cluster {i}:")
    print(cluster_texts.value_counts().head(10))  # Ή χρήση άλλης μεθοδολογίας για εύρεση κορυφαίων λέξεων

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
reduced_features = pca.fit_transform(X.toarray())

plt.scatter(reduced_features[:,0], reduced_features[:,1], c=df['cluster'])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Visualization of Tweet Clusters')
plt.show()
