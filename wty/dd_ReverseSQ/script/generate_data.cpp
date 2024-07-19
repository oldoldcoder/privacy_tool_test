#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <ctime>
#include <sstream>
#include <cstring>
#include <mutex>
using namespace std;


void createData() {
    // 定义生成数据文件的路径
    const char* fileString1 = "C:\\Users\\uu\\Desktop\\privacy_tool_test\\wty\\dd_ReverseSQ\\data\\data1.txt";
    ofstream outfile(fileString1);

    if (!outfile.is_open()) {
        cerr << "Error opening file for writing: " << fileString1 << endl;
        return;
    } else {
        cout << "File opened successfully: " << fileString1 << endl;
    }

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);

    for (int i = 0; i < 100; ++i) { // 写入数据
        for (int j = 0; j < 100; ++j) {
            if (j != 0) {
                outfile << " ";
            }
            outfile << dis(gen);
        }
        outfile << "\n";
    }

    

    outfile.close();
    cout << "Data written successfully to: " << fileString1 << endl;
}

void createData2() {
    // 定义生成数据文件的路径
    const char* fileString1 = "C:\\Users\\uu\\Desktop\\privacy_tool_test\\wty\\dd_ReverseSQ\\data\\data2.txt";
    ofstream outfile(fileString1);

    if (!outfile.is_open()) {
        cerr << "Error opening file for writing: " << fileString1 << endl;
        return;
    } else {
        cout << "File opened successfully: " << fileString1 << endl;
    }

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);

    for (int i = 0; i < 100; ++i) { // 写入数据
        for (int j = 0; j < 100; ++j) {
            if (j != 0) {
                outfile << " ";
            }
            outfile << dis(gen);
        }
        outfile << "\n";
    }

    

    outfile.close();
    cout << "Data written successfully to: " << fileString1 << endl;
}

int main() {
    createData();
    createData2();
    return 0;
}
