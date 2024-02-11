#include<bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<double> inputs(7);
    for(int i = 1; i < 8; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }
     vector<double>W={1.21,2.12,3.42,5.25,5.87,5.16,1.39};
    //cout<<endl;

     double l2out=0;
    for(int i = 0; i < 7; ++i) {
        
        l2out+=W[i]*inputs[i];
    }
    l2out=(l2out<0)?0:l2out;
    cout<<l2out;
    return 0;
    
}
