import random

def generate_data(num_entries,dim):
    data = []
    keywords = ['a', 'b', 'c']

    for i in range(num_entries):
        line = f"{i}:"
        for _ in range(dim):
            keyword = ''.join(random.choice(keywords) for _ in range(random.randint(1, 4)))
            line += f"{keyword},"
        data.append(line.rstrip(','))

    return data

def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')


if __name__ == "__main__":
    # Generate 200 lines of data as requested
    data = generate_data(1000000, dim=6)

    # Write the generated data to a file
    write_data_to_file(data, '../data/data.txt')