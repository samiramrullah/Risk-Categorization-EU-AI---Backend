# annex_iii.py

ANNEX_III = {
    "HIGH_RISK_ANNEX_III": {
        "section": "Annex III, Point 4(a)",
        "title": "Employment, workers management",
        "justification": (
            "The AI system is used in employment or career-related contexts and "
            "makes or significantly influences decisions affecting individuals’ "
            "access to employment or professional advancement."
        )
    },
    "HIGH_RISK_SAFETY_COMPONENT": {
        "section": "Annex III, Point 2",
        "title": "Safety components of regulated products",
        "justification": (
            "The AI system functions as a safety component of a product subject "
            "to EU harmonisation legislation, where failure may cause physical harm."
        )
    }
}

def annex_iii_justification(key):
    return ANNEX_III.get(key)
