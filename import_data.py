import csv
from pymongo import MongoClient

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "flightstatusDB"

try:
    # Establish MongoDB connection
    print("Connecting to MongoDB...")
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["flights"]

    # Import data from CSV
    print("Opening CSV file...")
    with open('flights.csv', 'r') as file:  # Ensure flights.csv is in the same directory
        reader = csv.DictReader(file)
        print("Reading and inserting data...")
        count = 0
        for row in reader:
            print(f"Read row: {row}")  # Print each row
            collection.insert_one(row)
            count += 1
    
    # Print the number of documents inserted
    print(f"Inserted {count} documents.")
    print("Data imported successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
