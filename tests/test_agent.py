import pytest

from app.agents.graph import build_agent_graph


def test_graph_fails_closed_until_workflow_is_implemented() -> None:
    with pytest.raises(RuntimeError, match="no claims can be evaluated"):
        build_agent_graph()
