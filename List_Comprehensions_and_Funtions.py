# Example 1: Squaring numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 2: Filtering even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# Example 3: Creating a list of tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
name_age_pairs = [(name, age) for name, age in zip(names, ages)]
print(name_age_pairs)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 28)]


def solve_quadratic_equation(a, b, c):
    """Solves a quadratic equation of the form ax^2 + bx + c = 0."""
    delta = (b**2) - 4*(a*c)

    if delta < 0:
        return "No real roots"
    elif delta == 0:
        x = (-b + delta**0.5) / (2*a)
        return f"One real root: x = {x}"
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return f"Two real roots: x1 = {x1}, x2 = {x2}"


print(solve_quadratic_equation(1, -5, 6))
