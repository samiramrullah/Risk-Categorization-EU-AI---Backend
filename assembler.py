# assembler.py

from annex_iii import annex_iii_justification
from conformity import conformity_route
from eu_database import eu_database

BASE_OUTCOMES = {

    "UNACCEPTABLE": {
        "risk_category": "Unacceptable Risk",
        "legal_basis": ["Article 5"],
        "obligations": ["System must not be placed on the market"]
    },

    "MINIMAL": {
        "risk_category": "Minimal Risk",
        "legal_basis": ["Article 69"],
        "obligations": ["Voluntary codes of conduct"]
    },

    "TRANSPARENCY_CHATBOT": {
        "risk_category": "Transparency Obligations",
        "legal_basis": ["Article 52"],
        "obligations": ["Inform users they are interacting with AI"]
    },

    "TRANSPARENCY_GENERATIVE": {
        "risk_category": "Transparency Obligations",
        "legal_basis": ["Article 52"],
        "obligations": ["Disclose AI-generated content"]
    },

    "TRANSPARENCY_BIOMETRIC": {
        "risk_category": "Transparency Obligations",
        "legal_basis": ["Article 52"],
        "obligations": ["Disclose biometric or emotion recognition"]
    },

    "HIGH_RISK_ANNEX_III": {
        "risk_category": "High-Risk AI System",
        "legal_basis": ["Article 6", "Annex III"]
    },

    "HIGH_RISK_SAFETY_COMPONENT": {
        "risk_category": "High-Risk AI System",
        "legal_basis": ["Article 6", "Annex III"]
    }
}

def build_assessment(outcome, gpai=None):
    base = BASE_OUTCOMES[outcome]

    assessment = {
        "risk_category": base["risk_category"],
        "legal_basis": base["legal_basis"],
        "obligations": base.get("obligations", [])
    }

    annex = annex_iii_justification(outcome)
    if annex:
        assessment["annex_iii_justification"] = annex

    assessment["conformity_assessment"] = conformity_route(outcome)
    assessment["eu_database_registration"] = eu_database(outcome)

    if outcome.startswith("HIGH_RISK"):
        assessment["post_market_monitoring"] = [
            "Performance monitoring",
            "Incident reporting",
            "Change impact assessment"
        ]

    if gpai:
        assessment["gpai_additional_obligations"] = gpai

    return assessment
