#include <istream>
#include <bits/stdc++.h>
using namespace std;

int diferenca(int numero1, int numero2){
    if (numero1 > numero2){
        return numero1 - numero2;
    }
    else{
        return numero2 - numero1;
    }
}
int main(){
    int tamanho, numero;
    cin >> tamanho;
    cin >> numero;
    int array[tamanho];
    for (size_t i = 0; i < tamanho; i++){
        cin >> array[i];
    }
    sort(array, array + tamanho);
    int pares = 0;
    for (size_t i = 0; i < tamanho - 1; i++){
        for (size_t j = i + 1; j < tamanho; j++){
            int tmp = diferenca(array[i], array[j]);
            if (tmp < numero){
                continue;
            }
            else if (tmp == numero){
                ++pares;
            }
            else{
                break;
            }
        }
    }
    cout << pares << "\n";
    return 0;
}