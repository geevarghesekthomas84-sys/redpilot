"""
Database backend selection.

RedPilot stores scans and findings in MongoDB by default, but can fall back to a
zero-setup local SQLite file for offline use. Choose the backend with the
``REDPILOT_DB_BACKEND`` environment variable:

    REDPILOT_DB_BACKEND=mongo    (default) — MongoDB via Motor
    REDPILOT_DB_BACKEND=sqlite             — local SQLite file (REDPILOT_SQLITE_PATH)

Import the shared instance as ``from redpilot.database import db``.
"""

import os

_backend = os.getenv("REDPILOT_DB_BACKEND", "mongo").strip().lower()

if _backend in ("sqlite", "sqlite3", "local", "file"):
    from redpilot.database.sqlite import db  # noqa: F401
else:
    from redpilot.database.mongo import db  # noqa: F401

__all__ = ["db"]
