import random

upper = 100000
def generate_data(dimensions):
    min_values = [random.randint(0, upper - 10) for _ in range(dimensions)]
    max_values = [random.randint(min_value + 1, upper) for min_value in min_values]

    # 确保每一列的最大值大于最小值
    data = [min_values, max_values]
    return data

def format_data(data):
    formatted_data = "\n".join([" ".join(map(str, row)) for row in data])
    return formatted_data

def main(filename, dimensions):
    data = generate_data(dimensions)
    formatted_data = format_data(data)

    # 将数据写入指定文件
    with open(filename, "w") as file:
        file.write(formatted_data)

if __name__ == "__main__":
    # 可以在此处指定文件名和维度数
    output_file = "../data/query.txt"
    dimensions = 64  # 可以根据需要指定列数
    main(output_file, dimensions)
