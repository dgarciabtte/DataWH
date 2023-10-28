import duckdb

connection = duckdb.connect(database='/Users/dgarciabtte/Documents/PcVILIV_Local/DEV/DataWareHouse1/main.db')
cursor = connection.cursor()

# Query the DuckDB system catalog to fetch table names
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main'")

# Fetch all the table names
table_names = cursor.fetchall()

# Print the table names
for table_name in table_names:
    print(table_name[0])

# Close the connection
connection.close()

##tables = [ 'central_park_weather', 'fhv_bases', 'fhv_tripdata', 'green_tripdata', 'yellow_tripdata']

##with open('/Users/dgarciabtte/Documents/PcVILIV_Local/DEV/DataWareHouse1/answers/raw_counts.txt', 'w') as f:
    ##for table in tables:
     ##   cursor.execute(f'SELECT COUNT(*) FROM {table}')
     ##   row_count = cursor.fetchone()[0]
     ##   f.write(f'{table} {row_count}\n')


duckdb.sql("SELECT 42").show()
