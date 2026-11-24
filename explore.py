import duckdb

con = duckdb.connect("nfl.duckdb")
con.sql("""
    SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'plays'
""").show()
