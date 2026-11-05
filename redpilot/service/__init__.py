"""RedPilot service layer — the typed, UI-free facade shared by CLI, API, and MCP."""

from redpilot.service.events import Event, EventBus
from redpilot.service.models import (
    AgentPlanStep, AgentResult, Finding, ScanResult, ScanSummary,
    ScopeState, ToolStatus,
)
from redpilot.service.service import RedPilotService, ScopeError, InputError, MODULE_MAP

__all__ = [
    "RedPilotService", "ScopeError", "InputError", "MODULE_MAP",
    "Event", "EventBus",
    "Finding", "ScanResult", "AgentPlanStep", "AgentResult",
    "ScanSummary", "ToolStatus", "ScopeState",
]
