///Plagio do GitHub
#include<bits/stdc++.h>

using namespace std;

#pragma GCC optimize("Ofast,no-stack-protector")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")

/// Typedef
typedef long long ll;
typedef unsigned long long ull;

#define sc1(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)

#define pf1(a) printf("%lld\n",a)
#define pf2(a,b) printf("%lld %lld\n",a,b)

#define vpnt(ans) for(ll i = 0; i < ans.size(); i++) cout << ans[i] << (i + 1 < ans.size() ? ' ' : '\n');
#define apnt(arr, num) for(ll i = 0; i < num; i++) cout << arr[i] << (i + 1 < num ? ' ' : '\n');

#define mx 200005
#define mod 1000000007
#define PI acos(-1.0)
#define eps 1e-7

#define size1 1505

#define no cout << "NO" << endl
#define yes cout << "YES" << endl
#define mem(name, value) memset(name, value, sizeof(name))

#define pb push_back
#define ff first
#define ss second
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define case cout << "Case " << t++ << ": ";

typedef vector <ll> vll;
typedef set <ll> sll;
typedef queue <ll> qll;
typedef map <ll, ll> mll;
typedef pair <ll, ll> pll;
typedef vector <pair <ll , ll> > vpll;

inline bool cmp(pll a,pll b){ if(a.ff == b.ff)return a.ss < b.ss; return a.ff > b.ff; }

deque <int> qu;

int main() {

    //freopen("/opt/Coding/clion code/input.txt", "r", stdin);
    //freopen("/opt/Coding/clion code/output.txt", "w", stdout);

    int n, m, num, tc, t = 1;

    scanf("%d", &num);

    char str[100];
    int cnt = 0, temp = 0;
    while(num--) {
        scanf("%s", str);

        if(str[0] == 'b') {
            if(qu.empty()) {
                printf("No job for Ada?\n");
            }
            else {
                if(cnt & 1) {
                    cout << qu.front() << '\n';
                    qu.pop_front();
                }
                else {
                    cout << qu.back() << '\n';
                    qu.pop_back();
                }
            }
        }
        else if(str[0] == 'f') {
            if(qu.empty()) {
                printf("No job for Ada?\n");
            }
            else {
                if(cnt & 1) {
                    cout << qu.back() << '\n';
                    qu.pop_back();
                }
                else {
                    cout << qu.front() << '\n';
                    qu.pop_front();
                }
            }
        }
        else if(str[0] =='r') cnt++;
        else if(str[0] == 'p') {
            scanf("%d", &temp);
            if(cnt & 1) qu.push_front(temp);
            else qu.push_back(temp);
        }
        else if(str[0] == 't') {
            scanf("%d", &temp);
            if(cnt & 1) qu.push_back(temp);
            else qu.push_front(temp);
        }
    }
}