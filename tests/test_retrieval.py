from inspect import signature

from app.retrieval.hybrid_store import HybridRetriever


def test_retriever_requires_company_tier_filter() -> None:
    company_tier = signature(HybridRetriever.retrieve).parameters["company_tier"]

    assert company_tier.default is company_tier.empty
    assert company_tier.kind is company_tier.KEYWORD_ONLY
