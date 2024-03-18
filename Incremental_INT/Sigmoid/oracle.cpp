#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<cfloat>
#include <iomanip>
using namespace std;

int main(int ac, char* av[]) {
    
    vector<double> inputs(7);
    for(int i = 1; i < 8; ++i) {
        inputs[i - 1] = stod(string(av[i]));
    }

    //cout<<exp(1)<<endl;
    //std::cout << std::fixed << std::setprecision(10);

     auto sigmoid=[&](double x)->double
     {
          //if(exp(-x)==HUGE_VAL)return 1.0/DBL_MAX;
          //cout<<exp(-x)<<endl;
        //   if(exp(-x)==0)
        //   {
        //       //cout<<"Hi"<<endl;
        //       return (double)0.9999999999;
        //   }
          //if(x==0)cout<<"hi"<<endl;
          
          double temp=1.00+exp(-x);
          //cout<<temp<<endl;;
          double y=1.00/temp;
          // double a=1.0;
          // double y=a/(double)(a+exp(-x));
          //cout<<y<<endl;
          // if(y==1)
          // {
          //   //cout<<"hi"<<endl;
          //   return (double)0.999999;
          // }
          // if(y==0)return (double)0.00000001;
          return y;
     };
     auto Sigmoid=[&](double x)->double
     {
         double temp=exp(x)+1;
         return temp/(temp+1);
     };
    vector<vector<double>> W= {
    {-0.26927736,  0.4474085,   -0.6313309,  -0.23548515,  0.28327122,  0.18054737, -0.7850956},
    { 0.40271512,  0.593842,   -0.48198894, -0.34208864, -0.33478367,  0.2008145,   0.33520782},
    { 0.25987637,  0.0748964,    0.08253773,  0.304837,    0.34815702,  0.00122899,  0.06936391},
    { 0.5486546,  -0.31519368,  -0.4794696,   0.46808526, -0.6001533,   0.4800906,   0.23571008},
    {-0.6680718,  -0.06248595,   0.30081135, -0.46983615, -0.19020042,  0.4570041,  -0.2823602},
    { 0.01759708, -0.04382259,  -0.07980937, -0.17746899, -0.30356637, -0.23139721, -0.21972698},
    {-0.0791545,  -0.01202262,   0.48967943,  0.39217058,  0.572214,    0.07319394, -0.278908}
};
   vector<double>B={-0.012214,0.12345678,0.23242210,-0.11230691,-0.88321415,0.551432123,-0.75767};
     double l2out=0;
     int k=0;
    for(int i = 0; i < 7; ++i) {
        
        l2out+=W[k][i]*inputs[i];
    }
    l2out+=B[k];
    cout<<l2out<<endl;
    
    l2out=sigmoid(l2out);
    cout<<l2out;
    return 0;
    
}
