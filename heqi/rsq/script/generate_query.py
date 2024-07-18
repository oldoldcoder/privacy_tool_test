import random

def read_data_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    header = lines[0].strip().split()
    x_rows = int(header[0])
    y_rows = int(header[1])

    # 读取 x 数据集和 y 数据集
    data = [line.strip() for line in lines[1:x_rows + y_rows + 1]]

    # 提取 y 数据集
    y_data = data[x_rows:x_rows + y_rows]

    return y_data

def write_query_file(y_data, output_filename):
    # 从 y 数据集中随机选择一行
    random_line = random.choice(y_data)
    random_line = random_line.replace(",", " ")
    with open(output_filename, "w") as file:
        file.write(random_line)

def main(input_filename, output_filename):
    y_data = read_data_file(input_filename)
    write_query_file(y_data, output_filename)

if __name__ == "__main__":
    input_file = "../data/data.txt"  # 输入文件名
    output_file = "../data/query.txt"  # 输出文件名

    main(input_file, output_file)
