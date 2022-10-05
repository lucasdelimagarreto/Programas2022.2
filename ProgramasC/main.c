#include <stdio.h>
#include <stdlib.h>

int main (){

    int vet[10], aux;

    for (int i = 0; i < 10; i++){

        printf("digite um numero pro vetor: ");
        scanf("%d", &vet[i]);
    }

    for (int i = 0; i < 10; i++){

        for (int j = i; j < 10; j++){
            
            if (vet[i] > vet[j]){

                aux = vet[i];
                vet[i] = vet[j];
                vet[j] = aux;
            }
            
        }
        
    }
    
    for (int i = 0; i < 10; i++){

        printf("%d \n", vet[i]);
        
    }

    return 0;
}