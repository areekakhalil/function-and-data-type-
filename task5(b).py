# ----------Data type----------
# Question no 1

positive_float = 3.7
negative_float = -3.7
positive_int = int(positive_float)
negative_int = int(negative_float)

print("Positive float:", positive_float)
print("Converted to integer:", positive_int)

print("Negative float:", negative_float)
print("Converted to integer:", negative_int)

# Question no 2
print(3 * True)        
print(-3.1 * True)     

print(3 * False)       
print(-3.1 * False)    

print("abc" * True)    
print(type("abc" * False))  
print(len("abc" * False))    

# Question no 3
def get_expected_cost(beds, baths, has_basement):
    base_cost = 80000
    cost_per_bedroom = 30000
    cost_per_bathroom = 10000
    basement_cost = 40000 if has_basement else 0
    
    value = base_cost + (beds * cost_per_bedroom) + (baths * cost_per_bathroom) + basement_cost
    return value

# Example usage:
print(get_expected_cost(1, 1, False))  # Output: 120000
print(get_expected_cost(2, 1, True))   # Output: 190000

# Question no 4
print(False + False)      # Expected output: 0
print(True + False)       # Expected output: 1
print(False + True)       # Expected output: 1
print(True + True)        # Expected output: 2
print(False + True + True + True)  # Expected output: 3

# Question no 5
def cost_of_project(engraving, solid_gold):
    if solid_gold:
        base_cost = 100
        cost_per_unit = 10
    else:
        base_cost = 50
        cost_per_unit = 7
    
    engraving_cost = len(engraving) * cost_per_unit
    total_cost = base_cost + engraving_cost
    return total_cost

# Calculate the cost of engraving "Charlie+Denver" on a solid gold ring
project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

# Calculate the cost of engraving "08/10/2000" on a gold plated ring
project_two = cost_of_project("08/10/2000", False)
print(project_two)