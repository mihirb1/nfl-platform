## Day 2 (Nov 23-24, one session past midnight)
Done: NFL project setup (venv, requirements.txt, .gitignore, GitHub), loaded
2025 plays into DuckDB (48,771 rows, idempotent with CREATE OR REPLACE),
explored columns, checked game_id + play_id uniqueness.

Learned: Parquet is columnar. A DuckDB file holds tables. play_id is unique
within a game but has gaps (not a running count). Text values need single
quotes in SQL.

Struggled / avoided: window functions and LeetCode. Felt low after the
Databricks rejection, but did the work anyway. Deleted Polymarket.

Confidence: 3/5. Next: LeetCode starts, then star schema design.