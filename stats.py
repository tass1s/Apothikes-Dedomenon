import pandas as pd

# Φόρτωση του DataFrame
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Περιγραφική Στατιστική
descriptive_stats = df[['favorite_count', 'retweet_count', 'reply_count', 'quote_count']].describe()
print(descriptive_stats)

# Υπολογισμός Συσχέτισης
correlation_matrix = df[['favorite_count', 'retweet_count', 'reply_count', 'quote_count']].corr()
print(correlation_matrix)
