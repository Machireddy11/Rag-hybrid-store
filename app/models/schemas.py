from pydantic import BaseModel, ConfigDict, Field


class AuditRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    claim_query: str = Field(
        min_length=1,
        max_length=4000,
        examples=["Commercial Gold meal expense limit for a NYC client dinner"],
    )
    expense_amount: float = Field(gt=0, allow_inf_nan=False, examples=[135.00])
    company_tier: str = Field(min_length=1, max_length=100, examples=["Commercial_Gold"])


class AuditResponse(BaseModel):
    is_compliant: bool
    max_allowed_amount: float
    policy_clause: str
    requires_manual_review: bool
    reasoning: str
