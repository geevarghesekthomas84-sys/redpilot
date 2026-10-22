## 2025-02-23 - Adding Composite Index for Sorting Vulnerabilities
**Learning:** In SQLite databases, queries that filter by one column and sort by another (e.g. `WHERE scan_id=? ORDER BY severity_order ASC`) can be significantly slower if only the filtered column is indexed, as the engine still has to perform a sort phase on the results. Creating a composite index (in this case `(scan_id, severity_order)`) allows the database engine to retrieve the rows already in the requested order without an explicit sort step.
**Action:** When adding or updating SQLite queries in this codebase that filter by a foreign key and sort the results, always ensure that a composite index covering both the filter and the sort columns exists.

## 2025-02-23 - Batching Database Writes
**Learning:** In the core engine and service modules, vulnerabilities were being iterated over and inserted one by one (`await db.upsert_vulnerability`), which resulted in N+1 database operations and thread context switches. This is especially slow for SQLite as it causes sequential `fsync` operations on disk.
**Action:** When inserting or updating multiple records in the database, always use bulk write operations (e.g., `bulk_write` in MongoDB, or batched operations executed in a single transaction in SQLite) to reduce the number of context switches and disk I/O.
