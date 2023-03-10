/*Ejercicio 5: Construir un programa en lenguaje C que a través de funciones recursivas resuelva los siguientes ítems: 
a) Cargar un arreglo de enteros, de N componentes. 
b) Generar un subarreglo con las componentes del arreglo cargado, cuyo valor es mayor o igual al Promedio. 
c) Indicar cuantas componentes del subarreglo son mayores al promedio y cuantas iguales a éste.  
d) Ingresar un número y decir si se encuentra en el subarreglo. 
e) Realice el ítem anterior si el arreglo original estuviera ordenado ascendentemente.*/

/*Exercise 5: Build a program in C language that through recursive functions solves the following items:
a) Load an array of integers, of N components.
b) Generate a subarray with the components of the loaded array, whose value is greater than or equal to Average.
c) Indicate how many components of the subarray are greater than the average and how many are equal to it.
d) Enter a number and say if it is in the subarray.
e) Do the previous item if the original array was ordered ascending.*/

#include <stdio.h>
#include <stdlib.h>
#define N 10

void busquedaorigen(int *a, int num, int inf, int sup, int med){
    med=(inf+sup)/2;
    if((inf<=sup) && (a[med]!=num)){
        if(num<a[med]) busquedaorigen(a,num,inf,med-1,med); 
        else busquedaorigen(a,num,med+1,sup,med); 
    } 
    if(a[med] == num){
        printf("El numero se encuentra en el arreglo.\n");
        return;
    }else{
    	printf("El numero no se encuentra en el arreglo.\n");
    	return;
	}
}

void busquedasub(int *b, int num, int i){
    if(i>N){
    	printf("El elemento no se encuentra en el arreglo.\n");
    	return;
	}
    if(b[i]==num){
        printf("El elemento se encuentra en el arreglo.\n");
        return;
    } else busquedasub(b,num,i+1);
}

void cuantas(int b[], int c, int i, int c1, int c2, float prom){
    if(i<c){
        if(b[i]>(prom/N)) c1++;
        if(b[i]==(prom/N)) c2++;
        cuantas(b,i+1,c1,c2,prom);
    }else{
        printf("Componentes mayores al promedio: %d.\n", c1);
        printf("Componentes iguales al promedio: %d.\n", c2);
        return;
    }
}

void subarreglo(int *a, int *b, int i, float prom, int &cont){
    if(i==N) return;
    else{
        if(a[i]>=(prom/N)){
            b[i]=a[i];
            cont++;
        }
        subarreglo(a,b,i+1,prom);
    }
}

void promedio(int *a, int i, float &prom){
    if(i<N){
        prom+=a[i];
        promedio(a,i+1,prom);
    }else return;
}

void carga(int *a, int i){
    if(i==N) return;
    else{
        a[i]=1+rand()%50;
        carga(a,i+1);
    }
}

int main(){
    int a[N],b[N],num,inf=0,sup=N-1,med, cont=0;
    float prom;
    carga(a,0);
    promedio(a,0,prom);
    subarreglo(a,b,0,prom,cont);
    cuantas(b,cont,0,0,0,prom);
    printf("Ingrese el numero a buscar:\n");
    scanf("%d", &num);
    busquedasub(b,num,0);
    busquedaorigen(a,num,inf,sup,med);
}