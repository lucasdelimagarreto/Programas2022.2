#include <bits/stdc++.h>
using namespace std;

int main(){

    bool verificador = false;
    int contador;
    cin >> contador;
    string menu;
    deque<int> q;
    while (contador--){
        
        cin >> menu;
        if (menu == "toFront"){
            int valor;
            cin >> valor;
            if (!verificador){
                q.push_front(valor);
            }
            else{
                q.push_back(valor);
            }
        }
        else if (menu == "front"){
            if (!verificador){
                if (q.empty()){
                    cout << "No Job for Ada?\n";
                }
                else{
                    cout << q.front() << endl;
                    q.pop_front();
                }
            }else{
                if (q.empty()){
                    cout << "No Job for Ada?\n";
                }
                else{
                    cout << q.back() << endl;
                    q.pop_back();
                }
            }
        }
        else if (menu == "back"){
            if (verificador){
                if (q.empty()){
                    cout << "No Job for Ada?\n";
                }
                else{
                    cout << q.front() << endl;
                    q.pop_front();
                }
            }
            else{
                if (q.empty()){
                    cout << "No Job for Ada?\n";
                }
                else{
                    cout << q.back() << endl;
                    q.pop_back();
                }
            }
        }
        else if (menu == "reverse"){
            verificador =! verificador;
        }
        else if (menu == "push_back"){
            int valor;
            cin >> valor;
            if (verificador){
                q.push_front(valor);
            }
            else{
                q.push_back(valor);
            }
        }
    }
}