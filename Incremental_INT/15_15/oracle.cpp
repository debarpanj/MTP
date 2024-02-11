#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(15);
    for(int i = 1; i < 16; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }
      srand(100);
    //vector<vector<int>> w = {{6, 10, 6, 2, 1, 4, 0, 6, 3, 1}, {8, 7, 5, 3, 7, 4, 9, 10, 2, 0}, {10, 8, 5, 0, 4, 6, 0, 10, 3, 10}, {10, 7, 10, 3, 7, 9, 7, 8, 2, 10}, {7, 10, 4, 1, 0, 10, 4, 9, 7, 6}, {8, 6, 2, 2, 7, 6, 6, 5, 5, 7}, {4, 4, 4, 3, 6, 9, 10, 2, 4, 1}, {0, 10, 9, 4, 0, 10, 1, 2, 6, 9}, {7, 1, 4, 9, 3, 9, 2, 10, 3, 7}, {6, 8, 9, 8, 9, 4, 5, 9, 5, 9}};
    vector<vector<int>> w(15, vector<int>(15));
    for(int i = 0; i < 15; ++i) {
        for(int j = 0; j < 15; ++j) {
            w[i][j] = rand() % 11;  // Random weight between 0 and 10 (inclusive)
            //cout<<w[i][j]<<" ";
        }
        //cout<<endl;
    }
    cout<<endl;

    vector<int> l2out(15,0);
    for(int i = 0; i < 15; ++i) {
        for(int j = 0; j < 15; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    for(auto x: l2out) {
        cout << x << " ";
    }
    cout << endl;
    // srand(21);
    // //vector<vector<int>> w2 = {{8, 3, 8, 7, 5, 7, 4, 7, 7, 8}, {5, 1, 10, 7, 8, 0, 6, 10, 8, 9}, {4, 2, 4, 3, 10, 3, 5, 2, 10, 8}, {10, 5, 0, 5, 10, 6, 10, 3, 0, 7}, {10, 5, 6, 9, 10, 4, 9, 5, 3, 7}, {2, 8, 7, 4, 9, 4, 5, 1, 7, 4}, {10, 6, 8, 8, 0, 7, 3, 9, 0, 1}, {5, 8, 4, 0, 6, 4, 2, 2, 9, 6}, {7, 9, 1, 3, 3, 8, 8, 8, 9, 4}, {0, 8, 8, 8, 4, 6, 4, 7, 4, 2}};
    // vector<vector<int>> w2(15, vector<int>(15));
    // for(int i = 0; i < 15; ++i) {
    //     for(int j = 0; j < 15; ++j) {
    //         w2[i][j] = rand() % 11;  // Random weight between 0 and 10 (inclusive)
    //         cout<<w2[i][j]<< " ";
    //     }
    //     cout<<endl;
    // }
    // cout<<endl;
    // vector<int> l3out(15,0);
    // for(int i = 0; i < 15; ++i) {
    //     for(int j = 0; j < 15; ++j) {
    //         l3out[i] += (l2out[j] * w2[j][i]);
    //     }
    //     if(l2out[i] < 0) l2out[i] = 0;
    // }
    // for(auto x: l3out) {
    //     cout << x << " ";
    // }
    // cout<<endl;

    // vector<int> w3(15);
    // srand(53);
    // for(int i=0;i<15;i++)
    // {
    //    w3[i]= rand() % 11; 
    //    cout<<w3[i]<<" ";

    // }
    // cout<<endl;
    // int out = 0;
    // for(int i = 0; i < 15; ++i) {
    //     out += (w3[i] * l3out[i]);
    // }
    // cout << out << endl;
}