import random
upper = 100000
def generate_horizontal_data(num_dimensions):
    data = []
    for _ in range(num_dimensions):
        min_value = random.randint(1, upper - 10)
        max_value = min_value + random.randint(min_value, upper)
        data.append((min_value, max_value))

    lines = []
    for min_val, max_val in data:
        line = f"{min_val} {max_val}"
        lines.append(line)

    return lines
if __name__ == "__main__":
    # Specify the number of dimensions
    num_dimensions = 64

    # Generate the horizontal data
    data = generate_horizontal_data(num_dimensions)

    # Save the generated data to a file
    file_name = "../data/range.txt"
    with open(file_name, 'w') as f:
        for line in data:
            f.write(line + '\n')

