#Program No 1: Learn the Building Blocks of Logic Programming in Python
# Facts and rules using simple Python logic
# Dictionary to store facts about different categories
facts = {
    "human": ["Tony", "Loki"],   # List of humans
    "Petar": []                      # Empty list (not used in this example)
}

# Function to check whether a person is mortal
def is_mortal(name):
    # If the given name exists in the human list
    if name in facts["human"]:
        return True      # Humans are considered mortal
    return False         # Otherwise, return False
# Assign the name to be checked
name = "Tony"

# Print whether the given name is a human
print("Is", name, "a human?", name in facts["human"])

# Print whether the given name is mortal using the function
print("Is", name, "mortal?", is_mortal(name))
#test 21aug2026