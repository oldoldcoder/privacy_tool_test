import random
upper = 100000
def generate_data(rows, dimensions):
    data = [[random.randint(0, upper) for _ in range(dimensions)] for _ in range(rows)]
    return data

def format_data(rows, dimensions, data):
    header = f"{rows} {dimensions}"
    formatted_data = "\n".join([",".join(map(str, row)) for row in data])
    return f"{header}\n{formatted_data}"

def main():
    # 您可以在此处指定行数和维度
    rows = 10000
    dimensions = 3

    data = generate_data(rows, dimensions)
    formatted_data = format_data(rows, dimensions, data)

    # 将数据写入文件
    with open("../data/data.txt", "w") as file:
        file.write(formatted_data)

if __name__ == "__main__":
    main()
