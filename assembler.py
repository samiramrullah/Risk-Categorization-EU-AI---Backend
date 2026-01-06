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
        "applicable_obligations": [],
        "required_controls": [],
        "not_required": []
    }

    # ─────────────────────────
    # UNACCEPTABLE RISK
    # ─────────────────────────
    if outcome == "UNACCEPTABLE":
        assessment["applicable_obligations"] = [
            "System must not be placed on the market or put into service"
        ]
        assessment["required_controls"] = [
            "Immediate discontinuation",
            "Removal from market",
            "Governance prohibition decision"
        ]
        assessment["not_required"] = [
            "Conformity assessment",
            "CE marking",
            "EU AI database registration",
            "Post-market monitoring"
        ]
        return assessment

    # ─────────────────────────
    # HIGH-RISK AI
    # ─────────────────────────
    if outcome.startswith("HIGH_RISK"):
        assessment["applicable_obligations"] = [
            "Risk management system",
            "Data governance and bias mitigation",
            "Technical documentation",
            "Logging and traceability",
            "Human oversight",
            "Accuracy, robustness and cybersecurity",
            "Post-market monitoring and incident reporting"
        ]

        assessment["required_controls"] = [
            "Formal AI risk assessment",
            "Bias and fairness testing",
            "Human-in-the-loop approval",
            "Override and fallback mechanisms",
            "Audit logging",
            "Change management procedures"
        ]

        assessment["additional_requirements"] = [
            "Conformity assessment required before placing on the market",
            "Registration in the EU AI database (Article 51)",
            "CE marking required"
        ]

        return assessment

    # ─────────────────────────
    # TRANSPARENCY OBLIGATIONS (ARTICLE 52)
    # ─────────────────────────
    if outcome.startswith("TRANSPARENCY"):
        assessment["applicable_obligations"] = [
            "Inform individuals that they are interacting with an AI system",
            "Disclose AI-generated or manipulated content where applicable",
            "Disclose use of emotion recognition or biometric categorisation"
        ]

        assessment["required_controls"] = [
            "Clear user-facing AI disclosures",
            "Content labelling or watermarking",
            "User documentation explaining AI use"
        ]

        assessment["not_required"] = [
            "Conformity assessment",
            "CE marking",
            "EU AI database registration",
            "Post-market monitoring"
        ]

        return assessment

    # ─────────────────────────
    # MINIMAL RISK
    # ─────────────────────────
    if outcome == "MINIMAL":
        assessment["applicable_obligations"] = [
            "No mandatory obligations under the EU AI Act"
        ]

        assessment["required_controls"] = [
            "Voluntary codes of conduct",
            "Ethical AI best practices"
        ]

        assessment["not_required"] = [
            "Conformity assessment",
            "CE marking",
            "EU AI database registration",
            "Post-market monitoring"
        ]

        return assessment
