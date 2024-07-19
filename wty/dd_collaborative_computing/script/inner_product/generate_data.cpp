#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <ctime>
#include <sstream>
#include <cstring>
#include <mutex>
using namespace std;

// 往文件中写入1万条数据，每个数据都是1-1000的随机数
void createData() {
    // 定义生成数据文件的路径
    const char* fileString = "C:\\Users\\uu\\Desktop\\privacy_tool_test\\wty\\dd_collaborative_computing\\data\\data.txt";
    ofstream outfile(fileString);

    if (!outfile.is_open()) {
        cerr << "Error opening file for writing: " << fileString << endl;
        return;
    } else {
        cout << "File opened successfully: " << fileString << endl;
    }

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);

    for (int i = 0; i < 2; ++i) { // 写入数据
        for (int j = 0; j < 1000000; ++j) {
            if (j != 0) {
                outfile << " ";
            }
            outfile << dis(gen);
        }
        outfile << "\n";
    }

    outfile.close();
    cout << "Data written successfully to: " << fileString << endl;
}

int main() {
    createData();
    return 0;
}
