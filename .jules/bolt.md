## 2025-02-23 - Adding Composite Index for Sorting Vulnerabilities
**Learning:** In SQLite databases, queries that filter by one column and sort by another (e.g. `WHERE scan_id=? ORDER BY severity_order ASC`) can be significantly slower if only the filtered column is indexed, as the engine still has to perform a sort phase on the results. Creating a composite index (in this case `(scan_id, severity_order)`) allows the database engine to retrieve the rows already in the requested order without an explicit sort step.
**Action:** When adding or updating SQLite queries in this codebase that filter by a foreign key and sort the results, always ensure that a composite index covering both the filter and the sort columns exists.

## 2025-02-23 - Batch Database Write Operations to prevent N+1 queries
**Learning:** Writing multiple database records iteratively using a for-loop (N+1 query problem) incurs significant database I/O latency, particularly when scaling to large payloads. The codebase's original `upsert_vulnerability` method exhibited this bottleneck in both MongoDB and SQLite backends when processing many scan findings.
**Action:** When inserting or updating multiple database records simultaneously in this codebase, always leverage batch mechanisms: use PyMongo's `bulk_write` with `UpdateOne` for MongoDB, and batch operations within a single transaction in Python's `sqlite3` driver (`con.commit()` only at the end).

## 2025-02-12 - [SQLite Batch Upserts Performance Bottleneck]
**Learning:** Avoid N+1 query loop when writing batch records to SQLite databases. The earlier approach utilized iterative `SELECT` statements followed by `UPDATE` or `INSERT`, leading to significant performance degradation over large workloads.
**Action:** Use `executemany` with `INSERT ... ON CONFLICT DO UPDATE` to dramatically reduce query volume and resolve N+1 queries. We can also use SQLite's native JSON operations like `json_set` to merge or preserve old data (like `created_at`) elegantly.
