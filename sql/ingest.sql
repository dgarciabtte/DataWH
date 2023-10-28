.echo on
CREATE TABLE central_park_weather AS SELECT * FROM 
read_csv('./data/central_park_weather.csv', HEADER='true', AUTO_DETECT=TRUE);
CREATE TABLE  fhv_bases AS SELECT * FROM 
read_csv('./data/fhv_bases.csv', HEADER='true', AUTO_DETECT=TRUE);
CREATE TABLE  citibike_tripdata AS SELECT * FROM 
read_csv('./data/citibike-tripdata.csv', HEADER='true', AUTO_DETECT=TRUE);
Create table fhv_tripdata as select * from
read_parquet('./data/taxi/fhv_tripdata.parquet',
Union_by_name=True, filename=True);
Create table green_tripdata as select * from
read_parquet('./data/taxi/green_tripdata.parquet',
Union_by_name=True, filename=True);
Create table yellow_tripdata as select * from
read_parquet('./data/taxi/yellow_tripdata.parquet',
Union_by_name=True, filename=True);


