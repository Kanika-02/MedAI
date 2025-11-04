def get_diagnosis(symptom):
    symptom = symptom.lower()

    # Simple rule-based demo logic
    if "fever" in symptom and "cough" in symptom:
        return "It could be a common cold or flu. Stay hydrated, rest, and consider paracetamol if fever persists."
    elif "headache" in symptom:
        return "It might be a tension headache or dehydration. Try drinking water and resting your eyes."
    elif "stomach pain" in symptom or "diarrhea" in symptom:
        return "You may have indigestion. Avoid spicy food and stay hydrated."
    elif "sore throat" in symptom:
        return "Gargle with warm salt water and drink warm fluids. It may be a throat infection."
    else:
        return "I'm not sure about that. Please consult a doctor for a proper diagnosis."
