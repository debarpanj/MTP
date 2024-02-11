#include<bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(7);
    for(int i = 1; i < 8; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }
    vector<vector<int>>W1={{6,10,6,2,1,4,0},{0,3,8,1,1,9,6},{1,10,7,7,7,4,2},{1,3,5,7,9,2,4},{2,4,6,8,10,1,3},{0,1,2,3,4,5,6},{1,2,3,5,5,5,1}};
    vector<int>l1out(7,0);
    vector<int>W={10,1,4,5,6,7,0};
    //cout<<endl;
    for(int j=0;j<7;j++)
    {
        for(int i=0;i<7;i++)
        {
            l1out[j]+=(inputs[i]*W1[j][i]);
        }
        l1out[j]=(l1out[j]<0)?0:l1out[j];
    }

     int l2out=0;
    for(int i = 0; i < 7; ++i) {
        
        l2out+=W[i]*l1out[i];
    }
    l2out=(l2out<0)?0:l2out;
    cout<<l2out;
    return 0;
    
}
