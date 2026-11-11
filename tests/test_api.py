from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "commercial-claims-agent",
    }


def test_readiness_reports_missing_workflow() -> None:
    response = client.get("/readyz")

    assert response.status_code == 503
    assert response.json()["detail"] == "Audit workflow is not configured."


def test_audit_does_not_return_a_mock_decision() -> None:
    response = client.post(
        "/v1/audit/claim",
        json={
            "claim_query": "Client dinner",
            "expense_amount": 135.0,
            "company_tier": "Commercial_Gold",
        },
    )

    assert response.status_code == 503
    assert "No claim has been evaluated." in response.json()["detail"]


def test_audit_rejects_non_positive_amount() -> None:
    response = client.post(
        "/v1/audit/claim",
        json={
            "claim_query": "Client dinner",
            "expense_amount": 0,
            "company_tier": "Commercial_Gold",
        },
    )

    assert response.status_code == 422
