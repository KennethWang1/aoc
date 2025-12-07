#include <bits/stdc++.h>

using namespace std;

#define f first
#define s second

int main()
{
    cin.sync_with_stdio(0); cin.tie();
    string str;
    int start;
    int sum = 1;
    vector<string> arr;
    while (cin>>str){
        arr.push_back(str);
        if(str == "X"){
            break;
        }
    }
    
    for(int i = 0; i < arr[0].size(); i++){
        if(arr[0][i] == 'S'){
            start = i;
            break;
        }
    }
    
    queue<pair<int,int>> q;
    q.push({0,start});
    
    while(!q.empty()){
        pair<int,int> p = q.front();
        q.pop();
        
        if(arr[p.f][p.s] == '^'){
            q.push({p.f,p.s+1});
            q.push({p.f,p.s-1});
            sum ++;
            arr[p.f][p.s] = '#';
        }else if(arr[p.f][p.s] == '#'){
            continue;
        }else{
            //q.push({p.f+1,p.s});
            for(int i = p.f; i < arr.size(); i++){
                if(arr[i][p.s] == '^'){
                    //cout<<i<<" "<<p.s<<endl;
                    q.push({i,p.s});
                    break;
                }
            }
            cout<<p.f<<" "<<p.s<<endl;
        }
    }
    
    cout<<(sum);

    return 0;
}
