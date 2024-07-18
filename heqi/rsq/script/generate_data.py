import random

upper = 100000
def generate_data(rows, dimensions):
    data = [[random.randint(1, upper) for _ in range(dimensions)] for _ in range(rows)]
    return data

def format_data(header, data):
    formatted_data = "\n".join([",".join(map(str, row)) for row in data])
    return f"{header}\n{formatted_data}"

def main(filename, x_rows, y_rows, dimensions, k):
    if k > y_rows:
        raise ValueError("k值不能大于y数据集的行数")

    x_data = generate_data(x_rows, dimensions)
    y_data = generate_data(y_rows, dimensions)

    # 组合并格式化数据
    header = f"{x_rows} {y_rows} {dimensions} {k}"
    data = x_data + y_data
    formatted_data = format_data(header, data)

    # 将数据写入文件
    with open(filename, "w") as file:
        file.write(formatted_data)

if __name__ == "__main__":
    # 可以在此处指定文件名，x数据集的行数，y数据集的行数，维度，和k值
    output_file = "../data/data.txt"
    x_rows = 10000
    y_rows = 10000
    dimensions = 64
    k = 100

    main(output_file, x_rows, y_rows, dimensions, k)
