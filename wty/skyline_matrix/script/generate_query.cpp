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
    const char* fileString1 = "C:\\Users\\uu\\Desktop\\privacy_tool_test\\wty\\skyline_matrix\\query.txt";
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

    vector<pair<int, int>> pairs;
    for (int i = 0; i < 6; ++i) {
        // 保证a < b
        int a = dis(gen);
        int b = dis(gen);
        while (a == b) {
            a = dis(gen);
        }
        if (a > b) {
            swap(a, b);
        }
        pairs.push_back({a, b});
    }

    for (int j = 0; j < 6; ++j) {
        outfile << pairs[j].first << " " << pairs[j].second << " " << endl;
    }

    for (int j = 0; j < 6; ++j) {
        uniform_int_distribution<> dis(pairs[j].first, pairs[j].second);
        int a = dis(gen);
        outfile << a << " ";
    }
    

    outfile.close();
    cout << "Data written successfully to: " << fileString1 << endl;
}

int main() {
    createData();
    return 0;
}