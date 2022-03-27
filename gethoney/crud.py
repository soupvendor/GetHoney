import sqlite3

conn = sqlite3.connect("../data/gethoney.db", check_same_thread=False)
curr = conn.cursor()
