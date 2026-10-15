"""Staged pipeline: discovery → validation → remediation → report."""

from redpilot.pipeline.models import PipelineResult, Stage, StageResult, STAGE_MODULES
from redpilot.pipeline.pipeline import Pipeline

__all__ = [
    "Pipeline", "PipelineResult", "Stage", "StageResult", "STAGE_MODULES",
]
