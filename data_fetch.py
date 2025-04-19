import pymysql
import pandas as pd

# Set up a connection to your SQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',  # Your DB password
    database='game_Analytics'
)

# Function to fetch data from a table
def fetch_data_from_sql(query):
    return pd.read_sql(query, connection)

# Fetch Rankings Data
def get_rankings_data():
    query = "SELECT * FROM competitor_rankings"  # Replace with the correct table name
    return fetch_data_from_sql(query)

# Fetch Competitors Data
def get_competitors_data():
    query = "SELECT * FROM competitors"  # Replace with the correct table name
    return fetch_data_from_sql(query)

# Fetch Complexes Data
def get_complexes_data():
    query = "SELECT * FROM complexes"  # Replace with the correct table name
    return fetch_data_from_sql(query)

# Fetch Venues Data
def get_venues_data():
    query = "SELECT * FROM venues"  # Replace with the correct table name
    return fetch_data_from_sql(query)

# Fetch Category Data
def get_category_data():
    query = "SELECT * FROM categories"  # Replace with the correct table name
    return fetch_data_from_sql(query)

# Fetch Competitions Data
def get_competitions_data():
    query = "SELECT * FROM competitions"  # Replace with the correct table name
    return fetch_data_from_sql(query)