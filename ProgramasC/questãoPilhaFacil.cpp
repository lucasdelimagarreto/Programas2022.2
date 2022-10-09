#include <stdio.h>
int main(){

    int pilha[2], aux, menuVal, valor, i = 0;
    scanf("%d", &aux);
    for (i = 0; i < aux; i++){
        
        if (i < 2){
            scanf("%d   %d", &menuVal, &valor);
            pilha[i] = valor;
        }
        else{
            scanf("\n%d", &menuVal);
            if (menuVal == 2){
                pilha[0] = pilha[1];
                pilha[1] = 0;
            }
            if (menuVal == 3)
            {
                if (pilha[0] == 0 && pilha[1] == 0)
                {
                    printf("Empty!");
                }else
                {
                    printf("%d\n", pilha[0]);
                }
            }
        }
        
    }
    return 0;
}