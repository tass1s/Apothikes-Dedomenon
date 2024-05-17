import pandas as pd
import matplotlib.pyplot as plt

# Φόρτωση δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Μετατροπή της στήλης created_at σε datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Δημιουργία νέας στήλης για την ώρα
df['hour'] = df['created_at'].dt.hour

# Δημιουργία ιστογράμματος
plt.figure(figsize=(10,6))
df['hour'].plot(kind='hist', bins=24, range=(0, 23), alpha=0.7)
plt.title('Frequency of Tweets per Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Tweets')
plt.xticks(range(24))  # Προσθήκη ετικετών για κάθε ώρα της ημέρας
plt.grid(True)
plt.show()
