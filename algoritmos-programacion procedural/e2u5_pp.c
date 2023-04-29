/*Ejercicio 2: La Federación Argentina de boxeo (FAB) mantiene información de los boxeadores federados: DNI, categoría y el peso 
(47..90) en kilogramos. Las categorías están codificadas por letras: ‘A’: Peso crucero, ...., ‘ H’: Peso minimosca. La 
cantidad de participantes se ingresa por teclado.   Escribir un programa en C que permita:  
a) Cargar los datos en una estructura adecuada. (Validar el ingreso, suponiendo que código de categoría varía entre 
‘A’ y ‘H‘)  
b) Para  una  categoría  determinada,  mostrar  los  DNI  de  los  boxeadores  que  tienen  el  peso  máximo.  Generar  una 
estructura auxiliar.  
c) Realizar un listado que muestre, para cada Peso cuantos participantes existen. Generar una estructura auxiliar.*/

/*Exercice 2: The Argentine Boxing Federation (FAB) maintains information on federated boxers: DNI, category and weight
(47..90) in kilograms. The categories are coded by letters: 'A': Cruiserweight, ...., 'H': Light Flyweight. The
number of participants is entered by keyboard. Write a C program that allows:
a) Load the data in a suitable structure. (Validate the entry, assuming that the category code varies between
'A' and 'H')
b) For a certain category, show the DNI of the boxers who have the maximum weight. generate a
auxiliary structure.
c) Make a list that shows, for each Weight, how many participants there are. Generate an auxiliary structure.*/

#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>

const char c[8][1]={'A','B','C','D','E','F','G','H'};

typedef struct{
    char *dni;
    char categ;
    float peso;    
}box;

void switchhh(char categ, int *b){
    switch(categ){
        case 'A': b[0]++; break;
        case 'B': b[1]++; break;
        case 'C': b[2]++; break;
        case 'D': b[3]++; break;
        case 'E': b[4]++; break;
        case 'F': b[5]++; break;
        case 'G': b[6]++; break;
        case 'H': b[7]++; break;
    }
}

void carga(box *&a, int &cant, int i, int *b){
    char *aux, categ;
    printf("Ingrese la cantidad de boxeadores:\n");
    scanf("%d",&cant);
    a=(box*)malloc(sizeof(box)*cant);
    while(i<cant){
        aux=(char*)malloc(sizeof(char)*8+1);
        printf("Boxeador: %d\n",i+1);
        printf("Ingrese la categoria: \n");
        scanf("%c",&categ);
        fflush(stdin);
        if((categ>='A') && (categ<='H')){
            switchhh(categ,b);
            a[i].categ=categ;
            printf("Ingrese el dni: \n");
            scanf("%s",&aux);
            a[i].dni=(char*)malloc(sizeof(char)*strlen(aux)+1);
            strcpy(a[i].dni,aux);
            free(aux);
            printf("Ingrese el peso: \n");
            scanf("%f",&a[i].peso);
            fflush(stdin);
            i++;
        }else{
            printf("Categoria incorrecta. Reingrese.\n");
        }
    }
}

float maximo(box *a,int i,int cant, float max){
    if(i==cant) return max;
    else{
         if(a[i].peso>max) return maximo(a,i+1,cant,a[i].peso);
         else return maximo(a,i+1,cant,max);
    }
}

void pesomaximo(box *a, int cant){
    int j=0;
    char c, *dni[cant];
    printf("Ingrese la categoria a buscar:\n");
    scanf("%c",&c);
    for(int i=0; i<cant; i++){
        if ((a[i].categ == c) && a[i].peso == maximo(a,0,cant,0)){
            dni[j]=(char*)malloc(sizeof(char)*8+1);
            strcpy(dni[j],a[i].dni);
            j++;
        }
    }
    for(int k=0; k<j; k++){
        printf("%s",dni[k]);
    }
    free(dni);
}

void cantidad(int *b, int i, int N){
    if(i==N) return;
    else{
        printf("Categoria: %c\n",c[i]);
        printf("Cantidad de participantes: %d\n.",b[i]);
        cantidad(b,i+1,N);
    }
}

int main(){
    box *a;
    int cant, *b;
    b=(int*)malloc(sizeof(int)*8);
    for(int i=0; i<8;i++){
        b[i]=0;
    }
    carga(a,cant,0,b);
    pesomaximo(a,cant);
    cantidad(b,0,8);
}