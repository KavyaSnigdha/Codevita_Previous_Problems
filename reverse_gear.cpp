#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
 int n;
 cin>>n;
 for(int i=0;i<n;i++){
  int f,b,t,d,cnt=0,x;
  cin>>f>>b>>t>>d;
  while(1){
   if(b<d){
    x=((f+b)*t);
    cnt=cnt+x;
    d=d-(b-f);
   }
   else{
    x=(d*t);
    cnt=cnt+x;
    break;
   }
   
  }
  cout<<cnt<<endl;
 }
 return 0;
}
