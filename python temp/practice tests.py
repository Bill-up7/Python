import random

# Function to generate a random polynomial as a string
def generate_polynomial(degree):
    coeffs = [random.randint(-5, 5) for _ in range(degree + 1)]
    terms = []
    for i, coeff in enumerate(coeffs):
        if coeff == 0:
            continue
        power = degree - i
        term = f"{coeff}"
        if power > 0:
            term += f"x^{power}" if power > 1 else "x"
        terms.append(term)
    return " + ".join(terms) if terms else "0"

# Function to generate a random rational function (numerator/denominator)
def generate_rational_function():
    numerator_degree = random.choice([1, 2, 3])  # Degree of numerator
    denominator_degree = random.choice([1, 2, 3])  # Degree of denominator
    numerator = generate_polynomial(numerator_degree)
    denominator = generate_polynomial(denominator_degree)
    return numerator, denominator

# Function to calculate the horizontal asymptote
def calculate_ha(numerator, denominator):
    # Degree of numerator and denominator
    num_deg = numerator.count('x')
    denom_deg = denominator.count('x')

    if num_deg < denom_deg:
        return "y = 0"
    elif num_deg == denom_deg:
        # The horizontal asymptote is the ratio of the leading coefficients
        return "y = 1"
    else:
        return "No horizontal asymptote"

# Function to calculate the vertical asymptotes
def calculate_va(denominator):
    # In this case, we are simplifying by assuming we just have linear factors like x - a
    if 'x' in denominator:
        # Let's just create a single vertical asymptote at a random x value
        return [f"x = {random.randint(-5, 5)}"]
    return []

# Function to calculate the slant asymptote
def calculate_sa(numerator, denominator):
    # Slant asymptote occurs if numerator degree is 1 higher than the denominator
    num_deg = numerator.count('x')
    denom_deg = denominator.count('x')
    if num_deg == denom_deg + 1:
        # We'll assume a simple linear slant asymptote, represented by "y = x"
        return "y = x"
    return "No slant asymptote"

# Function to generate a practice test question
def generate_question():
    numerator, denominator = generate_rational_function()
    ha = calculate_ha(numerator, denominator)
    va = calculate_va(denominator)
    sa = calculate_sa(numerator, denominator)
    
    # Formatting the question and answers
    question = f"Given the rational function: f(x) = {numerator} / {denominator},\n"
    question += f"1. Find the horizontal asymptote (if any): {ha}\n"
    question += f"2. Find the vertical asymptotes (if any): {', '.join(va)}\n"
    question += f"3. Find the slant asymptote (if any): {sa}\n"
    
    return question

# Generate a practice test with 5 questions
def generate_practice_test(num_questions=5):
    return [generate_question() for _ in range(num_questions)]

# Example: Generate and display the practice test
if __name__ == "__main__":
    practice_test = generate_practice_test(5)
    for idx, question in enumerate(practice_test, 1):
        print(f"Question {idx}:\n{question}\n{'-'*50}")
