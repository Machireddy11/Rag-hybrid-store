from fastapi import FastAPI, HTTPException, status

from app.config import settings
from app.models.schemas import AuditRequest, AuditResponse

app = FastAPI(
    title="Commercial Claims - AI Audit API",
    version="1.0.0",
    description=(
        "API scaffold for auditing commercial expense claims against policy. "
        "A policy evaluation workflow must be configured before audits are available."
    ),
)


@app.get("/healthz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, str]:
    return {"status": "healthy", "service": settings.service_name}


@app.get("/readyz", status_code=status.HTTP_200_OK)
async def readiness_check() -> dict[str, str]:
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Audit workflow is not configured.",
    )


@app.post(
    "/v1/audit/claim",
    response_model=AuditResponse,
    status_code=status.HTTP_200_OK,
)
async def audit_commercial_claim(request: AuditRequest) -> AuditResponse:
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Audit workflow is not configured. No claim has been evaluated.",
    )
