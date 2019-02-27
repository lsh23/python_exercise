#include <bits/stdc++.h>
using namespace std;

int i;

vector<int> v;

int y(){
  int sum = 0;
  for(i=0;i<v.size();i++){
    if(v[i]<30) sum +=10;
    else{
      sum+=(v[i]/30 + 1)*10;
    }
  }
    return sum;
}

int m(){
  int sum = 0;
  for(i=0;i<v.size();i++){
    if(v[i]<60) sum +=15;
    else{
      sum+=(v[i]/60 + 1)*15;
    }
  }
  return sum;
}


int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;

  cin >> n;
  v.resize(n);
  for(i=0;i<n;i++){
    cin >> v[i];
  }

  int _y,_m;

  _y = y();
  _m = m();

  if(_y>_m)
    cout << "M " <<_m;
  else if(_y<_m)
    cout << "Y " <<_y;
  else
    cout << "Y M "<<_y;


  return 0;

}
