## 2025-02-23 - Adding Composite Index for Sorting Vulnerabilities
**Learning:** In SQLite databases, queries that filter by one column and sort by another (e.g. `WHERE scan_id=? ORDER BY severity_order ASC`) can be significantly slower if only the filtered column is indexed, as the engine still has to perform a sort phase on the results. Creating a composite index (in this case `(scan_id, severity_order)`) allows the database engine to retrieve the rows already in the requested order without an explicit sort step.
**Action:** When adding or updating SQLite queries in this codebase that filter by a foreign key and sort the results, always ensure that a composite index covering both the filter and the sort columns exists.

## 2025-02-23 - Batching Database Upserts for Vulnerabilities
**Learning:** Inserting or updating single database records in a loop (e.g. `upsert_vulnerability` called repeatedly) can create significant N+1 query overhead and excessive disk I/O. Both MongoDB (`bulk_write` with `UpdateOne`) and SQLite (looping within a single thread operation followed by a single `commit`) support efficient batched operations.
**Action:** When saving multiple vulnerabilities (or other records) to the database, always use bulk or batched methods (like `upsert_vulnerabilities`) instead of calling single-record insertion methods in a loop.
