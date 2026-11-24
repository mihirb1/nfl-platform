import duckdb

con = duckdb.connect("nfl.duckdb")
con.sql("""
    create or replace table plays as
    select * from 'data/play_by_play_2025.parquet'
""")

print(con.sql("select count(*) from plays"))