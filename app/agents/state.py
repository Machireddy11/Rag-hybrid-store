"""Typed data passed between claim-audit workflow nodes."""

from typing import NotRequired, TypedDict

from app.models.schemas import AuditResponse
from app.retrieval.hybrid_store import PolicyChunk


class AgentState(TypedDict):
    claim_query: str
    expense_amount: float
    company_tier: str
    retrieved_context: NotRequired[str | None]
    retrieved_docs: NotRequired[list[PolicyChunk] | None]
    final_audit: NotRequired[AuditResponse | None]
