"""RedPilot — AI-orchestrated offensive security automation."""

import os as _os


def _apply_env_compat() -> None:
    """Back-compat: mirror legacy ``SPAF_*`` env vars onto ``REDPILOT_*``.

    RedPilot was formerly ``spaf``; deployments and .env files may still set
    ``SPAF_*``. For any ``SPAF_<NAME>`` with no ``REDPILOT_<NAME>`` already set,
    copy the value across so old configs keep working. Called at import and again
    after the CLI loads a .env file.
    """
    for key, val in list(_os.environ.items()):
        if key.startswith("SPAF_"):
            new = "REDPILOT_" + key[len("SPAF_"):]
            _os.environ.setdefault(new, val)


_apply_env_compat()
