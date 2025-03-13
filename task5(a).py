# -------------->Function<-----------------
# Question no 1
def get_expected_cost(beds, baths):
    base_cost = 80000
    cost_per_bedroom = 30000
    cost_per_bathroom = 10000
    
    expected_cost = base_cost + (beds * cost_per_bedroom) + (baths * cost_per_bathroom)
    
    return expected_cost

# Example usage:
print(get_expected_cost(1, 1))  # Output: 120000
print(get_expected_cost(2, 1))  # Output: 150000

# Question no 2
def get_expected_cost(beds, baths):
    base_cost = 80000
    cost_per_bedroom = 30000
    cost_per_bathroom = 10000
    
    expected_cost = base_cost + (beds * cost_per_bedroom) + (baths * cost_per_bathroom)
    
    return expected_cost

option_1 = get_expected_cost(2, 3)
option_2 = get_expected_cost(3, 2)
option_3 = get_expected_cost(3, 3)
option_4 = get_expected_cost(3, 4)

print("Option 1 cost:", option_1)  # Expected cost for 2 beds, 3 baths
print("Option 2 cost:", option_2)  # Expected cost for 3 beds, 2 baths
print("Option 3 cost:", option_3)  # Expected cost for 3 beds, 3 baths
print("Option 4 cost:", option_4)  # Expected cost for 3 beds, 4 baths

# Quesstion no 3
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft_to_paint = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft_to_paint / sqft_per_gallon
    total_cost = gallons_needed * cost_per_gallon
    return total_cost

sqft_walls = 400
sqft_ceiling = 200
sqft_per_gallon = 350
cost_per_gallon = 25.00

cost = get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
print("Total cost to paint the room:", cost)

# Question  no 4
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft_to_paint = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft_to_paint / sqft_per_gallon
    total_cost = gallons_needed * cost_per_gallon
    return total_cost

sqft_walls = 432
sqft_ceiling = 144
sqft_per_gallon = 400
cost_per_gallon = 15.00

cost = get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
print("Total cost to paint the room:", cost)

# Question no 5
import math

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft_to_paint = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft_to_paint / sqft_per_gallon
    actual_gallons = math.ceil(gallons_needed)
    total_cost = actual_gallons * cost_per_gallon
    return total_cost

sqft_walls = 432
sqft_ceiling = 144
sqft_per_gallon = 400
cost_per_gallon = 15.00

cost = get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
print("Total cost to paint the room:", cost)