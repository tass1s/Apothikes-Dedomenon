import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Φόρτωση δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Εξαγωγή κειμένου και ανάλυση συναισθήματος
df['sentiment'] = df['text'].apply(lambda tweet: TextBlob(tweet).sentiment)

# Προσθήκη στήλης πολικότητας και υποκειμενικότητας
df['polarity'] = df['sentiment'].apply(lambda x: x.polarity)
df['subjectivity'] = df['sentiment'].apply(lambda x: x.subjectivity)

# Εμφάνιση των πρώτων αποτελεσμάτων
print(df[['text', 'polarity', 'subjectivity']].head())



# Οπτικοποίηση πολικότητας
plt.figure(figsize=(10, 5))
plt.hist(df['polarity'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Tweet Polarity')
plt.xlabel('Polarity')
plt.ylabel('Frequency')
plt.show()

# Οπτικοποίηση υποκειμενικότητας (προαιρετικό)
plt.figure(figsize=(10, 5))
plt.hist(df['subjectivity'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Tweet Subjectivity')
plt.xlabel('Subjectivity')
plt.ylabel('Frequency')
plt.show()
