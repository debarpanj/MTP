#include<bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(7);
    for(int i = 1; i < 8; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }
     vector<int>W={1,2,3,5,5,5,1};
    //cout<<endl;

     int l2out=0;
    for(int i = 0; i < 7; ++i) {
        
        l2out+=W[i]*inputs[i];
    }
    l2out=(l2out<0)?0:l2out;
    cout<<l2out;
    return 0;
    
}
