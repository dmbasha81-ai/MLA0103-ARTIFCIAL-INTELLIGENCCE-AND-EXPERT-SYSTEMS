# Backward Chaining for Dengue Fever Diagnosis

# Symptoms of Dengue
facts = {
    "high_fever": True,
    "headache": True,
    "joint_pain": True,
    "skin_rash": True
}

# Rule
def backward_chaining():
    print("Goal: Check if patient has Dengue Fever\n")

    if facts.get("high_fever"):
        if facts.get("headache"):
            if facts.get("joint_pain"):
                if facts.get("skin_rash"):
                    print("Result: Patient has Dengue Fever.")
                    return

    print("Result: Patient does NOT have Dengue Fever.")

# Driver Code
backward_chaining()
