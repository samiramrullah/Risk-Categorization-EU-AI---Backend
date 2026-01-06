# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from decision_tree import QUESTIONS
from assembler import build_assessment
from gpai import GPAI
from glossary import GLOSSARY


app = Flask(__name__)
CORS(app)

@app.route("/start", methods=["POST"])
def start():
    return jsonify({
        "question_id": "Q0",
        "question": QUESTIONS["Q0"]["text"],
        "allowed_answers": ["yes", "no"]
    })

@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()
    qid = data["question_id"]
    answer = data["answer"]
    gpai_state = data.get("gpai")

    if answer == "not_sure":
        return jsonify({
            "status": "REQUIRES_HUMAN_REVIEW",
            "reason": "Insufficient certainty to classify under EU AI Act"
        })

    outcome = QUESTIONS[qid][answer]

    # if outcome.startswith("GPAI"):
    #     return jsonify({
    #         "next_question": "Q1",
    #         "gpai_state": GPAI[outcome]
    #     })
    if outcome.startswith("GPAI"):
     next_qid = "Q1"
     return jsonify({
        "question_id": next_qid,
        "question": QUESTIONS[next_qid]["text"],
        "allowed_answers": ["yes", "no", "not_sure"],
        "gpai_state": GPAI[outcome]
    })


    if outcome in QUESTIONS:
        return jsonify({
            "question_id": outcome,
            "question": QUESTIONS[outcome]["text"],
            "allowed_answers": ["yes", "no"],
            "gpai_state": gpai_state
        })

    return jsonify({
        "assessment_complete": True,
        "final_assessment": build_assessment(outcome, gpai_state)
    })

@app.route("/glossary", methods=["GET"])
def get_full_glossary():
    """
    Returns the full EU AI Act glossary
    """
    return jsonify({
        "source": "EU AI Act",
        "count": len(GLOSSARY),
        "terms": GLOSSARY
    })
if __name__ == "__main__":
    app.run()
