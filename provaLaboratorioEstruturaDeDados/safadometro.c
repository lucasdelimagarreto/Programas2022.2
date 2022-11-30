#include <stdio.h>

int somatorio(int mes){

    if(mes == 0){
        return 0;
    }
    return mes + somatorio(mes -1);

}
void wesleySafadao(int dia, int mes, float anoComDoisDigitos){
    float safadeza = somatorio(mes) + (anoComDoisDigitos/100) * (50 - dia);
    float anjo = 100 - safadeza;
    printf("Anjo: %.1f", anjo);
    printf("Safadeza: %.1f", safadeza);
}
int main(void) {
    int dia,mes;
    float anoComDoisDigitos;

    printf("digite o dia do nascimento");
    scanf("%d", &dia);
    printf("digite o mes do nascimento");
    scanf("%d", &mes);
    printf("digite o ano do nascimento");
    scanf("%f", &anoComDoisDigitos);

    wesleySafadao(dia,mes,anoComDoisDigitos);

    return 0;
}