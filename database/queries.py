class Creator:
	def country_table_creator(self,conn):
		cur = conn.cursor()
		cur.execute('''CREATE TABLE countries
               (date text, trans text, symbol text, qty real, price real)''')

	def country_add(self):
		cur.execute("INSERT INTO countries VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

