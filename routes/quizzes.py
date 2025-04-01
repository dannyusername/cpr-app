from flask import Blueprint, render_template, request, jsonify, session
import random

quizzes = Blueprint('quizzes', __name__, template_folder='templates')

# CPR Quiz questions
questions = [
    {
        "question": "What is the first step in the Cardiac Chain of Survival?",
        "correct_answer": "Recognize emergency, call EMS.",
        "other_options": [
            "Perform CPR immediately.",
            "Provide early defibrillation.",
            "Wait for advanced medical care."
        ]
    },
    {
        "question": "How do you check if someone needs CPR?",
        "correct_answer": "Check breathing and responsiveness.",
        "other_options": [
            "Check for a pulse for 30 seconds.",
            "Wait for EMS to arrive.",
            "Tap their shoulder and wait."
        ]
    },
    {
        "question": "Where should AED pads be placed on an adult?",
        "correct_answer": "Upper right chest, lower left side.",
        "other_options": [
            "Both on the chest center.",
            "One on the back, one on the chest.",
            "One on each side of the neck."
        ]
    },
    {
        "question": "What should you do if the AED advises 'no shock'?",
        "correct_answer": "Resume CPR immediately.",
        "other_options": [
            "Turn off the AED and stop.",
            "Remove pads and reposition.",
            "Wait for help to arrive."
        ]
    },
    {
        "question": "How should you care for a conscious choking adult?",
        "correct_answer": "5 back blows, 5 thrusts.",
        "other_options": [
            "Perform chest compressions.",
            "Give two rescue breaths.",
            "Check for a pulse first."
        ]
    },
    {
        "question": "What should you do if a choking person becomes unresponsive?",
        "correct_answer": "Start CPR immediately.",
        "other_options": [
            "Call EMS and wait.",
            "Perform abdominal thrusts.",
            "Try to give rescue breaths."
        ]
    },
    {
        "question": "What is the primary purpose of an AED?",
        "correct_answer": "Restore normal heart rhythm.",
        "other_options": [
            "Restart the heart.",
            "Provide oxygen to the brain.",
            "Reduce blood pressure."
        ]
    },
    {
        "question": "What precautions should you take when using an AED?",
        "correct_answer": "No contact during shock delivery.",
        "other_options": [
            "Keep the AED elevated.",
            "Ensure pads are fully dry.",
            "Avoid using it in sunlight."
        ]
    },
    {
        "question": "How do you perform hands-only CPR?",
        "correct_answer": "Continuous compressions only.",
        "other_options": [
            "30 compressions, 2 breaths.",
            "Compressions every 5 seconds.",
            "Chest compressions with AED only."
        ]
    },
    {
        "question": "What are common signals of a heart attack?",
        "correct_answer": "Chest pain, trouble breathing.",
        "other_options": [
            "Severe coughing, dry throat.",
            "Sweating without chest pain.",
            "Sharp pain in fingers or toes."
        ]
    },
    {
        "question": "What is the correct rate for chest compressions during CPR?",
        "correct_answer": "100\u2013120 compressions per minute",
        "other_options": [
            "60\u201380 compressions per minute",
            "At least 150 compressions per minute",
            "40 compressions per minute"
        ]
    },
    {
        "question": "How deep should compressions be for an adult?",
        "correct_answer": "At least 2 inches (5 cm)",
        "other_options": [
            "At least 3 inches",
            "About 1 inch",
            "Half an inch"
        ]
    },
    {
        "question": "What should you do if the chest does not rise during a rescue breath?",
        "correct_answer": "Retilt the head and give a second breath",
        "other_options": [
            "Start CPR immediately",
            "Skip the breaths and continue compressions",
            "Tap and shout again"
        ]
    },
    {
        "question": "Can an AED be used on a person with a pacemaker?",
        "correct_answer": "Yes, but avoid placing pads directly over the device",
        "other_options": [
            "No, AEDs are unsafe with pacemakers",
            "Only if the person is unconscious",
            "Only under hospital supervision"
        ]
    },
    {
        "question": "What are the four links in the Cardiac Chain of Survival?",
        "correct_answer": "Early recognition, CPR, defibrillation, advanced care",
        "other_options": [
            "Call 911, do CPR, use AED, transport patient",
            "Rescue breathing, CPR, AED, hospital care",
            "Scene safety, EMS, CPR, AED"
        ]
    },
    {
        "question": "What should you do if the person does not give consent for care?",
        "correct_answer": "Do not provide care; call 9-1-1",
        "other_options": [
            "Give care anyway if it\u2019s an emergency",
            "Wait for a bystander to help",
            "Leave the person alone"
        ]
    },
    {
        "question": "How deep should compressions be for an infant?",
        "correct_answer": "About 1\u00bd inches (4 cm)",
        "other_options": [
            "About 2\u00bd inches",
            "At least 3 inches",
            "As deep as possible"
        ]
    },
    {
        "question": "How should you open the airway for rescue breaths?",
        "correct_answer": "Head-tilt, chin-lift method",
        "other_options": [
            "Lift the shoulders",
            "Cover the mouth and nose",
            "Push the chest inward"
        ]
    },
    {
        "question": "What is the compression to breath ratio for CPR?",
        "correct_answer": "30 compressions to 2 breaths",
        "other_options": [
            "15 compressions to 1 breath",
            "10 compressions to 5 breaths",
            "Continuous breaths only"
        ]
    },
    {
        "question": "How long should each rescue breath last?",
        "correct_answer": "About 1 second",
        "other_options": [
            "3 seconds",
            "Until the person coughs",
            "About 5 seconds"
        ]
    },
    {
        "question": "What should you do before applying AED pads?",
        "correct_answer": "Remove clothing and dry the chest",
        "other_options": [
            "Apply oxygen",
            "Wait for EMS to arrive",
            "Cover the chest with a cloth"
        ]
    },
    {
        "question": "Can an AED be used on a wet person?",
        "correct_answer": "Dry them off first before applying pads",
        "other_options": [
            "Yes, water improves conductivity",
            "No, wait until EMS arrives",
            "Only if you have gloves on"
        ]
    },
    {
        "question": "How do you care for a person having a diabetic emergency?",
        "correct_answer": "Give them sugar if they are conscious",
        "other_options": [
            "Make them lie down",
            "Begin CPR immediately",
            "Apply an ice pack"
        ]
    },
    {
        "question": "How do you care for severe external bleeding?",
        "correct_answer": "Apply direct pressure with a sterile dressing",
        "other_options": [
            "Flush with water",
            "Apply ice directly",
            "Remove any embedded objects"
        ]
    },
    {
        "question": "What are the four links in the Cardiac Chain of Survival?",
        "correct_answer": "Early recognition, CPR, defibrillation, advanced care",
        "other_options": [
            "Call 911, do CPR, use AED, transport patient",
            "Rescue breathing, CPR, AED, hospital care",
            "Scene safety, EMS, CPR, AED"
        ]
    },
    {
        "question": "What is defibrillation and how does it work?",
        "correct_answer": "It delivers a shock to help restore a normal heart rhythm",
        "other_options": [
            "It keeps the airway open",
            "It forces the heart to beat faster",
            "It delivers oxygen to the brain"
        ]
    },
    {
        "question": "What are common signals of a breathing emergency?",
        "correct_answer": "Trouble breathing, wheezing, gurgling, pale or bluish skin",
        "other_options": [
            "Pain in the legs",
            "Sudden fever",
            "Unusual hunger"
        ]
    },
    {
        "question": "What should you do if a choking person is pregnant or too large for abdominal thrusts?",
        "correct_answer": "Give chest thrusts instead",
        "other_options": [
            "Do back blows only",
            "Wait for EMS",
            "Lay the person down"
        ]
    },
    {
        "question": "Can an AED be used on a person with a pacemaker?",
        "correct_answer": "Yes, but avoid placing pads directly over the device",
        "other_options": [
            "No, AEDs are unsafe with pacemakers",
            "Only if the person is unconscious",
            "Only under hospital supervision"
        ]
    },
    {
        "question": "What should you do if the chest does not rise during rescue breathing?",
        "correct_answer": "Retilt the head and try again",
        "other_options": [
            "Skip the breaths",
            "Start chest compressions",
            "Give 5 quick breaths"
        ]
    },
    {
        "question": "When is hands-only CPR appropriate?",
        "correct_answer": "When a responder cannot or chooses not to give rescue breaths",
        "other_options": [
            "Only for infants",
            "Only with an AED present",
            "When someone is breathing normally"
        ]
    },
    {
        "question": "What is the first thing you should do in any emergency situation?",
        "correct_answer": "Check the scene for safety",
        "other_options": [
            "Check for breathing",
            "Call for help immediately",
            "Begin CPR"
        ]
    },
    {
        "question": "What should you do if a person does not give consent for care?",
        "correct_answer": "Do not provide care and call 911",
        "other_options": [
            "Give care anyway",
            "Wait for someone else",
            "Leave the area"
        ]
    },
    {
        "question": "What is the purpose of the Good Samaritan Law?",
        "correct_answer": "To protect people who give care in good faith",
        "other_options": [
            "To punish those who refuse to help",
            "To require CPR certification",
            "To limit the role of first responders"
        ]
    }
]

@quizzes.route('/')
def index():
    """Main quiz page"""
    return render_template('quizzes.html')

@quizzes.route('/get_questions', methods=['POST'])
def get_questions():
    """API endpoint to get quiz questions"""
    data = request.get_json()
    num_questions = data.get('num_questions', 5)
    
    # Select random questions
    selected_questions = random.sample(questions, min(num_questions, len(questions)))
    
    # Prepare questions for the frontend with answer options randomized
    prepared_questions = []
    for q in selected_questions:
        all_options = q["other_options"] + [q["correct_answer"]]
        random.shuffle(all_options)
        
        # Find which index contains the correct answer
        correct_index = all_options.index(q["correct_answer"])
        
        prepared_questions.append({
            "question": q["question"],
            "options": all_options,
            "correct_index": correct_index
        })
    
    # Store in session for validation
    session['quiz_questions'] = prepared_questions
    
    return jsonify({"questions": prepared_questions})

@quizzes.route('/check_answers', methods=['POST'])
def check_answers():
    """API endpoint to check quiz answers"""
    data = request.get_json()
    user_answers = data.get('answers', [])
    questions = session.get('quiz_questions', [])
    
    if len(user_answers) != len(questions):
        return jsonify({"error": "Answer count doesn't match question count"}), 400
    
    results = []
    score = 0
    
    for i, (q, ans) in enumerate(zip(questions, user_answers)):
        is_correct = ans == q['correct_index']
        if is_correct:
            score += 1
        
        results.append({
            "question_index": i,
            "is_correct": is_correct,
            "correct_answer": q['options'][q['correct_index']]
        })
    
    feedback = ""
    if score == len(questions):
        feedback = "Excellent work!"
    elif score > len(questions) // 2:
        feedback = "Good effort, keep practicing!"
    else:
        feedback = "Try again!"
        
    return jsonify({
        "score": score,
        "total": len(questions),
        "results": results,
        "feedback": feedback
    })
