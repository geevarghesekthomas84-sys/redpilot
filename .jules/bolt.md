## 2025-02-23 - Adding Composite Index for Sorting Vulnerabilities
**Learning:** In SQLite databases, queries that filter by one column and sort by another (e.g. `WHERE scan_id=? ORDER BY severity_order ASC`) can be significantly slower if only the filtered column is indexed, as the engine still has to perform a sort phase on the results. Creating a composite index (in this case `(scan_id, severity_order)`) allows the database engine to retrieve the rows already in the requested order without an explicit sort step.
**Action:** When adding or updating SQLite queries in this codebase that filter by a foreign key and sort the results, always ensure that a composite index covering both the filter and the sort columns exists.

## 2025-02-23 - Database Bulk Upsert for Vulnerabilities
**Learning:** Bulk writing database writes when updating multiple records to avoid N+1 query performance bottlenecks. Iterating through results and executing individual updates can cause a large performance hit.
**Action:** Use bulk writes (`bulk_write` in MongoDB or batched implicit transactions in SQLite) when inserting/updating multiple records.
