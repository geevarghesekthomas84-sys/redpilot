## 2025-02-23 - Adding Composite Index for Sorting Vulnerabilities
**Learning:** In SQLite databases, queries that filter by one column and sort by another (e.g. `WHERE scan_id=? ORDER BY severity_order ASC`) can be significantly slower if only the filtered column is indexed, as the engine still has to perform a sort phase on the results. Creating a composite index (in this case `(scan_id, severity_order)`) allows the database engine to retrieve the rows already in the requested order without an explicit sort step.
**Action:** When adding or updating SQLite queries in this codebase that filter by a foreign key and sort the results, always ensure that a composite index covering both the filter and the sort columns exists.

## 2025-02-23 - Batching Database Writes
**Learning:** Inserting multiple vulnerability records using an N+1 approach (looping and executing an individual insert for each finding) is a huge performance bottleneck due to excessive disk I/O and lack of batching in both SQLite and MongoDB.
**Action:** When inserting or updating multiple database records at once, always implement and utilize bulk write operations (e.g., `bulk_write` with `UpdateOne` in MongoDB, or batched operations within a single transaction in SQLite) to avoid N+1 query performance bottlenecks.
