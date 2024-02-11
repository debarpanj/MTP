#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<float> inputs(3);
    for(int i = 1; i < 4; ++i) {
        string numerator , denominator = "1" , s;
        int flag = 0;
        s = av[i];
        for(int i = 0 ; i < s.size() ; i++)
        {
            if(s[i] == '/')
            {
                flag = 1;
                i++;
                denominator.pop_back();
            }
            if(flag == 0)
            numerator.push_back(s[i]);
            else
            denominator.push_back(s[i]);
        }
        inputs[i - 1] = stof(numerator)/stof(denominator);
    }
    //cout<<inputs[0]<<"  "<<inputs[1]<<"  "<<inputs[2]<<" ";
    vector<vector<float>> w = {{-6.0, 10.0, 5.0, 1.0}, {8.0, -7.0, 1.0, -1.0}, {4.0, 7.0, -3.0, -2.0}};
    vector<float> l2out(4);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 3; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    for(auto x: l2out) {
        cout << x << " ";
    }

    vector<vector<float>> w2 = {{-3.0, 4.0, 5.0, 9.0}, {6.0, -7.0, 1.0, 4.0}, {3.0, -3.0, -3.0, -3.0}, {3.0, -3.0, -3.0, -3.0}};
    vector<float> l3out(4);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            l3out[i] += (l2out[j] * w2[j][i]);
        }
        if(l3out[i] < 0) l3out[i] = 0;
    }
    for(auto x: l3out) {
        cout << x << " ";
    }

    vector<float> w3 = {2.0, -1.0, 1.0, 7.0};
    float out = 0;
    for(int i = 0; i < 4; ++i) {
        out += (w3[i] * l3out[i]);
    }
     cout << out << endl;
}