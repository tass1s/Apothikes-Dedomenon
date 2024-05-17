import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Φόρτωση του JSON αρχείου
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Εξαγωγή hashtags
df['hashtags'] = df['entities'].apply(lambda x: [tag['text'] for tag in x['hashtags']])

# Εξετάζουμε τα πρώτα στοιχεία για να δούμε τη δομή
print(df['hashtags'].head())


# Δημιουργία λίστας με όλα τα hashtags
all_hashtags = sum(df['hashtags'].tolist(), [])

# Μέτρηση συχνοτήτων
hashtag_counts = Counter(all_hashtags)

# Εκτύπωση των 10 πιο δημοφιλών hashtags
print(hashtag_counts.most_common(10))



# Οπτικοποίηση των top 10 hashtags
top_hashtags = hashtag_counts.most_common(10)
hashtags, counts = zip(*top_hashtags)

plt.figure(figsize=(10,5))
plt.bar(hashtags, counts)
plt.xlabel('Hashtags')
plt.ylabel('Frequency')
plt.title('Top 10 Hashtags')
plt.xticks(rotation=45)
plt.show()
