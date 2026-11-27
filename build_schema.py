import duckdb

con = duckdb.connect("nfl.duckdb")
con.sql("""
    create or replace table dim_team (team_id varchar primary key);
    insert into dim_team (team_id)
        select distinct posteam
        from plays
        where posteam is not null;

    select count(*) from dim_team;
""").show()




