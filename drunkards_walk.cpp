#include<bits/stdc++.h>
using namespace std;
#define si(a) scanf("%d",&a)
int main()
{
 int n;
 si(n);
 while(n--){
  int fm,bm,t,fbs,bbs,cnt=0,ans=0,fl=0;
  char b;
  scanf(" %c",&b);
  si(fm);si(bm);si(t);si(fbs);si(bbs);
  if(b=='F' && fbs<=fm){
   printf("%d F\n",fbs*t);
   continue;
  }
  if(b=='B' && bbs<=bm){
   printf("%d B\n",bbs*t);
   continue;
  }
  if(fm>bm){
   while(1){
    if(fm>=fbs && cnt==0 && b=='F'){
     ans+=(fbs*t);
     printf("%d F\n",ans);
     break;
    }
    else if(fm>=fbs && cnt>0 && b=='F'){
     ans+=(fbs*t);
     printf("%d F\n",ans);
     break;
    }
    else if(fm>=fbs+bm && b=='B'){
     ans+=(bm*t)+((fbs+bm)*t);
     printf("%d F\n",ans);
     break;
    }
    
    else{
     ans+=((fm+bm)*t);
     fbs=fbs-(fm-bm);
    }
    cnt++;
    if(cnt>1000){
     fl=1;
     break;
    }
   }
  }
  else{
   while(1){
    if(bm>=bbs && cnt==0 && b=='B'){
     ans+=(bbs*t);
     printf("%d B\n",ans);
     break;
    }
    else if(bm>=bbs && cnt>0 && b=='B'){
     ans+=(bbs*t);
     printf("%d B\n",ans);
     break;
    }
    else if(bm>=bbs+fm && b=='F'){
     ans+=(fm*t)+((bbs+fm)*t);
     printf("%d B\n",ans);
     break;
    }
    else{
     ans+=((fm+bm)*t);
     bbs=bbs-(bm-fm);
    }
    cnt++;
    if(cnt>1000){
     fl=1;
     break;
    }
   }
  }
  if(fl)printf("Hurray\n");
 }
 return 0;
}
