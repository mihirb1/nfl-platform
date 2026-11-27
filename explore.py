import duckdb

# buffalo's total yards and change from previous game
# return game_id, total_yds and change
# first game's change should be null
# should be in order of game_id

con = duckdb.connect("nfl.duckdb")
con.sql("""
    with game_totals as (
        select game_id, SUM(yards_gained) AS total_yds
        from plays
        where posteam = 'BUF' and play_type in ('run', 'pass')
        group by posteam, game_id
    )
    select game_id, total_yds, lag(total_yds) over (order by game_id) - total_yds as change
    from game_totals
    order by game_id
""").show()


