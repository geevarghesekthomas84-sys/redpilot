## 2025-02-23 - Adding Composite Index for Sorting Vulnerabilities
**Learning:** In SQLite databases, queries that filter by one column and sort by another (e.g. `WHERE scan_id=? ORDER BY severity_order ASC`) can be significantly slower if only the filtered column is indexed, as the engine still has to perform a sort phase on the results. Creating a composite index (in this case `(scan_id, severity_order)`) allows the database engine to retrieve the rows already in the requested order without an explicit sort step.
**Action:** When adding or updating SQLite queries in this codebase that filter by a foreign key and sort the results, always ensure that a composite index covering both the filter and the sort columns exists.

## 2025-02-23 - Batch inserting vulnerabilities
**Learning:** Inserting multiple items into a database iteratively (e.g. `await db.upsert_vulnerability(...)` inside a loop) causes severe N+1 database queries overhead. For SQLite, it incurs repeated explicit locking/transactions overhead, and for MongoDB it results in numerous round-trips over the network.
**Action:** When inserting or updating multiple database records, always use bulk write operations (e.g., `upsert_vulnerabilities` leveraging `bulk_write` in MongoDB or single-transaction batched operations in SQLite) to avoid N+1 query performance bottlenecks and excessive disk I/O.
