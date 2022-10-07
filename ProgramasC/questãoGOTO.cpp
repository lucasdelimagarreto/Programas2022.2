#include <locale.h>
#include <iostream>
using namespace std;

int main(){
    setlocale(LC_ALL, "Portuguese");
    printf("Utilização do GO TO.\n");
    
    int aux = 5;

    LOOP: do
    {
        if (aux == 15){
            aux += 1;
            goto LOOP;
        }
        cout << "valor de aux: " << aux << endl;
        aux += 1;
        
    } while (aux < 10);
    
    system("pause");
    return 0;
}