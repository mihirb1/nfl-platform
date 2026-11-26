import duckdb

con = duckdb.connect("nfl.duckdb")
con.sql("""
    select posteam, game_id, play_id, yards_gained, 
        row_number() over (order by yards_gained desc) as rn, 
        rank() over (order by yards_gained desc) as rnk,
        dense_rank() over (order by yards_gained desc) as dense_rnk
    from plays
    where (play_type = 'run' or play_type = 'pass') and posteam = 'ARI'
    order by posteam, rn
    limit 15
""").show()


