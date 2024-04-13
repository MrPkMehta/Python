from scipy.optimize import minimize

# Define objective function to maximize
def objective(weights):
    return -(0.08 * weights[0] + 0.10 * weights[1] + 0.12 * weights[2])

# Define constraints
constraints = (
    {"type": "eq", "fun": lambda weights: weights[0] + weights[1] + weights[2] - 1},  # Total investment
    {"type": "ineq", "fun": lambda weights: weights[0] - 0.3},  # Min investment in X
    {"type": "ineq", "fun": lambda weights: weights[1] - 0.2},  # Min investment in Y
    {"type": "ineq", "fun": lambda weights: weights[2] - 0.1},  # Min investment in Z
    {"type": "ineq", "fun": lambda weights: 0.6 - weights[0]},  # Max investment in X
    {"type": "ineq", "fun": lambda weights: 0.4 - weights[1]},  # Max investment in Y
    {"type": "ineq", "fun": lambda weights: 0.3 - weights[2]}   # Max investment in Z
)

# Initial guess for weights
initial_guess = [0.3, 0.2, 0.1]

# Optimize
result = minimize(objective, initial_guess, constraints=constraints)

# Print results
print("Optimal weights:", result.x)
print("Expected return:", -result.fun)









pip install pulp


import pulp

# Define the problem as a maximization problem
prob = pulp.LpProblem("Portfolio Optimization", pulp.LpMaximize)

# Define decision variables
w_X = pulp.LpVariable("Weight_X", lowBound=0.3, upBound=0.6)  # Weight of Asset X
w_Y = pulp.LpVariable("Weight_Y", lowBound=0.2, upBound=0.4)  # Weight of Asset Y
w_Z = pulp.LpVariable("Weight_Z", lowBound=0.1, upBound=0.3)  # Weight of Asset Z

# Define expected returns and risks for each asset
R_X = 0.08  # Example expected return for Asset X
R_Y = 0.10  # Example expected return for Asset Y
R_Z = 0.12  # Example expected return for Asset Z

# Objective function
prob += R_X * w_X + R_Y * w_Y + R_Z * w_Z, "Expected_Return"

# Constraints
prob += w_X + w_Y + w_Z == 1, "Total Investment"
prob += w_X >= 0.3, "Min Investment in X"
prob += w_Y >= 0.2, "Min Investment in Y"
prob += w_Z >= 0.1, "Min Investment in Z"

# Solve the problem
prob.solve()

# Print the results
print("Status:", pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Expected Return =", pulp.value(prob.objective))
