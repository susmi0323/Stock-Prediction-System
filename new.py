import sqlite3 as sq
import pandas as pd

db = sq.connect('stocks.db')

query = "SELECT DISTINCT(Country) FROM tkrinfo;"
country = pd.read_sql_query(query, db)

print(country)