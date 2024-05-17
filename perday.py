import pandas as pd
import matplotlib.pyplot as plt

# Φόρτωση των δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Μετατροπή της στήλης 'created_at' σε datetime format
df['created_at'] = pd.to_datetime(df['created_at'])

# Φιλτράρισμα δεδομένων μεταξύ 2016 και 2018
df = df[(df['created_at'] >= '2016-01-01') & (df['created_at'] <= '2018-12-31')]

# Υπολογισμός αριθμού tweets ανά μήνα
df['month'] = df['created_at'].dt.to_period('M')
tweets_per_month = df.groupby('month').size()

# Οπτικοποίηση
plt.figure(figsize=(14, 7))
tweets_per_month.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Δραστηριότητα Tweets ανά Μήνα (2016-2018)')
plt.xlabel('Μήνας')
plt.ylabel('Πλήθος Tweets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
