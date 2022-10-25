#include <iostream>
#include <deque>
#include <algorithm>
#include <math.h>
using namespace std;
int main(){
    int aux, regular = 0;
    cin >> aux;
    deque<int> k;
    while (aux--)
    {
        string z;
        cin >> z;

        if (z == "back")
        {
            if (!k.empty())
            {
                if (regular % 2 == 0)
                {
                    cout << k.back() << "\n";
                    k.pop_back();
                }
                else
                {
                    cout << k.front() << "\n";
                    k.pop_front();
                }
                
            }
            else
            {
                cout << "No job for Ada?\n";
            }
            
        }
        else if (z == "front")
        {
            if (!k.empty())
            {
                if (regular % 2 == 0)
                {
                    cout << k.front() << "\n";
                    k.pop_front();
                }
                else
                {
                    cout << k.back() << "\n";
                    k.pop_back();
                }
                
            }
            else
            {
                cout << "No job for Ada?\n";
            }
            
        }
        else if (z == "push_back")
        {
            int auxL;
            cin >> auxL;
            if (regular % 2 == 0)
            {
                k.push_front(auxL);
            }
            else
            {
                k.push_back(auxL);
            }
            
        }
        else if (z == "toFront")
        {
            int auxL;
            cin >> auxL;
            if (regular % 2 == 0)
            {
                k.push_front(auxL);
            }
            else
            {
                k.push_front(auxL);
            }
            
        }
        else
        {
            regular++;
        }
        
    }
    return 0;
}