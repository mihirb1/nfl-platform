import duckdb

# buffalo's total yards and change from previous game
# return game_id, total_yds and change
# first game's change should be null
# should be in order of game_id

con = duckdb.connect("nfl.duckdb")
con.sql("""
    describe plays
""").show()


