#Program No 4: Parse a Family Tree and Infer Relationships
parents = {
    "Amit": ["Raj", "Sunita"],
    "Neha": ["Raj", "Sunita"],
    "Rohan": ["Amit", "Priya"]
}

def parent(child, person):
    return person in parents.get(child, [])

def sibling(person1, person2):
    p1 = set(parents.get(person1, []))
    p2 = set(parents.get(person2, []))
    return person1 != person2 and len(p1.intersection(p2)) > 0

def grandparent(child, person):
    for p in parents.get(child, []):
        if person in parents.get(p, []):
            return True
    return False

print("Are Amit and Neha siblings?", sibling("Amit", "Neha"))
print("Is Raj grandparent of Rohan?", grandparent("Rohan", "Raj"))
print("Is Amit parent of Rohan?", parent("Rohan", "Amit"))
