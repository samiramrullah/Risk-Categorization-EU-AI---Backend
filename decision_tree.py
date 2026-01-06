# decision_tree.py

QUESTIONS = {

    # ─────────────────────────────────────
    # PHASE 0 — GPAI OVERLAY (NOT RISK)
    # ─────────────────────────────────────
    "Q0": {
        "text": "Is the system based on or does it integrate a General-Purpose AI (GPAI) model?",
        "yes": "Q0A",
        "no": "Q1"
    },
    "Q0A": {
        "text": "Does the GPAI model present systemic risk (very large compute, broad downstream impact)?",
        "yes": "GPAI_SYSTEMIC",
        "no": "GPAI_NON_SYSTEMIC"
    },

    # ─────────────────────────────────────
    # PHASE 1 — UNACCEPTABLE RISK (ART. 5)
    # ─────────────────────────────────────
    "Q1": {
        "text": "Does the system perform social scoring by public authorities?",
        "yes": "UNACCEPTABLE",
        "no": "Q2"
    },
    "Q2": {
        "text": "Does the system manipulate behaviour in a way likely to cause harm?",
        "yes": "UNACCEPTABLE",
        "no": "Q3"
    },
    "Q3": {
        "text": "Does the system exploit vulnerabilities of specific groups?",
        "yes": "UNACCEPTABLE",
        "no": "Q4"
    },
    "Q4": {
        "text": "Does the system use real-time remote biometric identification in public spaces for law enforcement?",
        "yes": "UNACCEPTABLE",
        "no": "Q5"
    },

    # ─────────────────────────────────────
    # PHASE 2 — HIGH RISK (ART. 6 + ANNEX III)
    # ─────────────────────────────────────
    "Q5": {
        "text": "Is the system used in employment, education, credit, healthcare, law enforcement, migration, or essential services?",
        "yes": "Q6",
        "no": "Q8"
    },
    "Q6": {
        "text": "Does the system make or significantly influence decisions affecting individuals’ rights or opportunities?",
        "yes": "HIGH_RISK_ANNEX_III",
        "no": "Q7"
    },
    "Q7": {
        "text": "Is the system a safety component of a product subject to EU harmonisation legislation?",
        "yes": "HIGH_RISK_SAFETY_COMPONENT",
        "no": "Q8"
    },

    # ─────────────────────────────────────
    # PHASE 3 — TRANSPARENCY (ART. 52)
    # ─────────────────────────────────────
    "Q8": {
        "text": "Does the system interact directly with humans?",
        "yes": "TRANSPARENCY_CHATBOT",
        "no": "Q9"
    },
    "Q9": {
        "text": "Does the system generate or manipulate content that may appear authentic?",
        "yes": "TRANSPARENCY_GENERATIVE",
        "no": "Q10"
    },
    "Q10": {
        "text": "Does the system perform emotion recognition or biometric categorisation?",
        "yes": "TRANSPARENCY_BIOMETRIC",
        "no": "MINIMAL"
    }
}
