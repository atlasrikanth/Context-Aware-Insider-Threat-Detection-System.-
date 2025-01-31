import pandas as pd
from datetime import datetime
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['insider_threat']
collection = db['user_activity']

# Simulate user activity data
data = {
    "user_id": [1, 1, 2, 2, 3, 3],
    "activity": ["login", "file_access", "login", "email", "login", "file_access"],
    "timestamp": [datetime(2023, 10, 1, 9, 0), datetime(2023, 10, 1, 9, 5),
                  datetime(2023, 10, 1, 9, 10), datetime(2023, 10, 1, 9, 15),
                  datetime(2023, 10, 1, 9, 20), datetime(2023, 10, 1, 9, 25)]
}

df = pd.DataFrame(data)

# Insert data into MongoDB
collection.insert_many(df.to_dict('records'))
print("Data inserted into MongoDB.")