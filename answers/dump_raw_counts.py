## dgarciab@andrew.edu.co
## web pague consulted for code support: https://duckdb.org/docs

import duckdb

connection = duckdb.connect(database='/Users/dgarciabtte/Documents/PcVILIV_Local/DEV/DataWareHouse1/main.db')
cursor = connection.cursor()


cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'")
## read the tables in the database 
table_names = []
for table in cursor.fetchall():
    table_names.append(table[0])
i=0
total_rows=0
for table in table_names:
    cursor.execute(f'SELECT COUNT(*) FROM {table_names[i]}')
    results = cursor.fetchone()[0]
    print(table_names[i]+ ": " + str(results))
    total_rows= total_rows+ results   
    i=i+1

print("Total_number_of_rows_all_tables:  "+ str(total_rows))

connection.close()

