# eu_database.py

def eu_database(outcome):
    if outcome.startswith("HIGH_RISK"):
        return {
            "registration_required": True,
            "legal_basis": "Article 51",
            "responsible_party": "Provider or authorised representative",
            "timing": "Before placing on the EU market"
        }

    return {
        "registration_required": False
    }
