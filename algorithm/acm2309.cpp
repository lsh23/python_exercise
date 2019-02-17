#include<iostream>
#include<algorithm>

using namespace std;

int nans[9];

int main(void)
{
    int i;
    for(i=0 ; i<9 ; i++){
      scanf("%d", &nans[i]);
    }
    int a,b,c,d,e,f,g;
    a= 0;
    b = a + 1;
    c = b + 1;
    d = c + 1;
    e = d + 1;
    f = e + 1;
    g = f + 1;
    int flag = 0;
    for(a = 0 ; a < 3 ; a ++){
      for(b = a+1; b < 4 ; b ++){
        for(c = b+1 ; c <5 ; c++){
          for(d = c+1; d < 6; d ++){
            for(e = d+1; e <7; e ++){
              for(f = e+1; f<8; f++){
                for(g = f+1; g<9; g++){
                  if(nans[a]+nans[b]+nans[c]+nans[d]+nans[e]+nans[f]+nans[g]==100){
                    flag=1;
                    break;
                  }
                }
                if(flag == 1)
                  break;
              }
              if(flag == 1)
                break;
            }
            if(flag == 1)
              break;
          }
          if(flag == 1)
            break;
        }
        if(flag == 1)
          break;
      }
      if(flag == 1)
        break;
    }

    int out[7] = {nans[a],nans[b],nans[c],nans[d],nans[e],nans[f],nans[g]};
    sort(out,out+7);
    for(int i = 0 ; i < 7; i++){
      cout << out[i] << "\n";
    }

    return 0;
}
