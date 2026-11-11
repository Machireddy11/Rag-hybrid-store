"""LangGraph workflow entry point.

The graph is intentionally unavailable until retrieval and policy evaluation
are implemented; callers must not treat a placeholder as an audit result.
"""

from app.agents.state import AgentState


def build_agent_graph() -> None:
    raise RuntimeError(
        "The claim-audit graph is not implemented; no claims can be evaluated."
    )
