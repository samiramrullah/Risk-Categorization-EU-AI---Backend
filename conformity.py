# conformity.py

def conformity_route(outcome):
    if outcome == "HIGH_RISK_SAFETY_COMPONENT":
        return {
            "route": "Third-party conformity assessment (Notified Body)",
            "legal_basis": "Article 43(1)",
            "ce_marking": True
        }

    if outcome == "HIGH_RISK_ANNEX_III":
        return {
            "route": "Internal conformity assessment",
            "legal_basis": "Article 43(2)",
            "ce_marking": True
        }

    return {
        "route": "Not applicable",
        "ce_marking": False
    }
