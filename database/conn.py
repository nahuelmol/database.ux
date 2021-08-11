import sqlite3

def make_conn():
	conn = sqlite3.connect('example.db')
	return conn