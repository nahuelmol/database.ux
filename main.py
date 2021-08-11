import os

from interface import start
from database.conn import make_conn

def connect_DB():
	result = make_conn()

	if result:
		return "database connected"

if __name__ == "__main__":
	print(connect_DB())
