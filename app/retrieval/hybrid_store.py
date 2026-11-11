"""Interface for tier-scoped hybrid policy retrieval.

The Qdrant and BM25 implementation is not connected yet. Implementations must
apply the company-tier filter in the data store before ranking or returning
policy chunks.
"""

from typing import Protocol, TypedDict


class PolicyChunk(TypedDict):
    id: str
    text: str
    metadata: dict[str, str]


class HybridRetriever(Protocol):
    def retrieve(
        self,
        query: str,
        *,
        company_tier: str,
        limit: int = 5,
    ) -> list[PolicyChunk]:
        """Return policy evidence restricted to the requested company tier."""
        ...
