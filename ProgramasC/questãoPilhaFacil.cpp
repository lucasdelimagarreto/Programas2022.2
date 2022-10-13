#include <bits/stdc++.h>
using namespace std;
int main(){
    int aux, valor;
    scanf("%d\n", &aux);
    queue<int> lista;
    while(aux--){
        scanf("%d", &valor);
        if (valor == 1){
            scanf("%d", &valor);
            lista.push(valor);
        }
        else if(valor == 2){
            if (lista.front() != NULL){
                lista.pop();
            }
        }
        else {
            if (lista.empty()){
                printf("Empty!\n");
            }
            else{
                printf("%d\n", lista.front());
            }
        }
    }
    return 0;
}