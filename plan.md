1. **Optimize `upsert_vulnerabilities` in `redpilot/database/sqlite.py`:**
   - Currently, it iteratively iterates over findings to execute `SELECT` to check for existence, and then executes `INSERT` or `UPDATE` conditionally.
   - Replace this with a single `con.executemany` executing `INSERT INTO ... ON CONFLICT DO UPDATE ...`. This bulk write avoids N+1 queries.
   - Utilize `json_set(excluded.data, '$.created_at', vulnerabilities.created_at)` to maintain the original `created_at` timestamp.
   - This aligns with the learning from `.jules/bolt.md` (Batch Database Write Operations).

2. **Complete pre-commit steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

3. **Submit the PR:**
   - Submit the PR with the performance metrics documented.
