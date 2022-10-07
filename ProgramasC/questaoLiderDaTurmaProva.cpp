#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
#define AUX = 2;
using namespace std;

int main(){
    setlocale(LC_ALL, "Portuguese");

    int quantAlunos = 10, turma[quantAlunos];

    for (size_t i = 0; i < quantAlunos; i++){
        turma[i] = i;
    }
    
    
    
    
    
    
    
    
    /*for (size_t i = 0; i < quantAlunos; i++){
        cout << "aluno: " << turma[i] + 1 << endl;
    }*/
    return 0;
}