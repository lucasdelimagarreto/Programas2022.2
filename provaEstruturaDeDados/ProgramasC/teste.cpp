#include <stdio.h>
#include <conio.h>

int valorMin(int listaPresentes[],int numOperacoes){
    int aux = 0;
    for (size_t i = 0; i < numOperacoes; i++){
        if (listaPresentes[i] >= aux){
            aux = listaPresentes[i];
        }
    }
    return aux;
}

int main(){

    int numOperacoes; 
    scanf("%d", &numOperacoes);
    int listaPresentes[numOperacoes];
    
    for (size_t i = 0; i < numOperacoes; i++){
        char menuNome[10];
        
        
    }
    return 0;
}