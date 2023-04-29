/*Ejercicio 3: Un laboratorio  abastece a 30 farmacias de  la provincia. Dicho laboratorio  comercializa 80 medicamentos (1..80)  de 
los que se debe registrar: Código de medicamento, nombre y precio unitario. Se  ingresan  las  ventas  realizadas  ordenada  por  farmacia.  
Por  cada  venta  a  una  farmacia  se  ingresa:  código  de medicamento y cantidad de  unidades,  
finalizando con código de medicamento igual a 0 (cero).
Codificar un programa en C, que utilizando funciones permita: 
a) Calcular y mostrar total de unidades vendidas de cada uno de los medicamentos. 
b) Escribir el/los códigos/s del/los medicamento/s por el que se recaudó mayor importe. 
c) Indicar la cantidad de unidades vendidas para un código de medicamento ingresado por teclado. 
d) Dado el nombre de un medicamento indicar el importe total recaudado y la cantidad de unidades vendidas. 
e) Indicar la cantidad de unidades vendida a cada farmacia y el importe total que pagó cada una.*/

/*Exercise 3: A laboratory supplies 30 pharmacies in the province. Said laboratory sells 80 medicines (1..80) of
those to be registered: medication code, name and unit price. Sales made ordered by pharmacy are entered.
For each sale to a pharmacy, enter: medication code and number of units,
ending with medication code equal to 0 (zero).
Code a program in C, that using functions allows:
a) Calculate and display the total units sold of each of the medications.
b) Write the code(s) of the medication(s) for which the highest amount was collected.
c) Indicate the number of units sold for a drug code entered by keyboard.
d) Given the name of a drug, indicate the total amount collected and the number of units sold.
e) Indicate the number of units sold to each pharmacy and the total amount paid by each one.*/

#include <stdio.h>
#include <string.h>

typedef struct{
    char nomb[40];
    float prec, imp;
    int acum;
}medicamento;

typedef struct{
    int cantidad;
    float importe;
}farmacia; 

void porfarmacia(farmacia a[30][80], int n, int m){
    int tot=0;
    float imp=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            tot+=a[i][j].cantidad;
            imp+=a[i][j].importe;
        }
        printf("Farmacia %d\n");
        printf("Cantidad de undidades vendidas %d\n", tot);
        printf("Importe total que pago %.2f\n", imp);
        tot=0;
        imp=0;
    }
}

void nombremedicamento(medicamento *b, int n){
    int i=0;
    char nombre[40];
    printf("Ingrese el nombre del medicamento a buscar:\n");
    gets(nombre);
    while((i<n) && (strcmp(b[i].nomb, nombre) != 0)){
        i++;
    }
    if(i<n){
        printf("Importe total recaudado: %.2f\n", b[i].imp);
        printf("Cantidad de unidades vendidas: %d\n", b[i].acum);
    } else{
        printf("El medicamento no se encuentra registrado.\n");
    }
}

void indicar(medicamento *b){
    int codigo;
    printf("Ingrese el codigo del medicamento a buscar:\n");
    scanf("%d", &codigo);
    printf("Cantidad de unidades vendidas: %d\n", b[codigo-1].acum);
}

void escribir(medicamento *b, int n){
    int max=0;
    for(int i=0; i<n; i++){
        if(b[i].imp > max)
            max=b[i].imp;
    }
    for(int j=0; j<n; j++){
        if(b[j].imp == max)
        printf("Codigo de medicamento con mayor importe: %d\n", j+1);
    }
}

void mostrar(medicamento *b, int n){
    for(int i=0; i<n; i++){
        printf("Cantidad de unidades vendidas: %d", b[i].acum);
    }
}

void ventas(farmacia a[30][80], medicamento *b, int n){
    int cod, cant;
    for(int i=0; i<n; i++){
    printf("Farmacia %d\n", i+1);
    printf("Ingrese el código de medicamento:\n");
    scanf("%d", &cod);
    while(cod!=0){
        printf("Ingrese la cantidad de unidades vendidas:\n");
        scanf("%d", &cant);
        a[i][cod-1].cantidad+=cant;
        a[i][cod-1].importe+=cant*b[cod-1].prec;
        b[cod-1].acum+=cant;
        b[cod-1].imp+=b[cod-1].acum*b[cod-1].prec;
        printf("Ingrese el código de medicamento:\n");
        scanf("%d", &cod);
        }
    }
}

void cereo(farmacia a[30][80]){
    for(int i=0; i<30 ; i++){
        for(int j=0; j<80; j++){
            a[i][j].cantidad=0;
            a[i][j].importe=0;
        }
    }
}

void carga(medicamento *b, int n){
    for(int i=0; i<n; i++){
        printf("Medicamento: %d\n", i+1);
        printf("Ingrese el nombre del medicamento:\n");
        gets(b[i].nomb);
        printf("Ingrese el precio unitario:\n");
        scanf("%f", &b[i].prec);
        b[i].imp=0;
        b[i].acum=0;
    }
}

int main(){
    farmacia a[30][80];
    medicamento b[80];
    carga(b,80);
    cereo(a);
    ventas(a,b,80);
    mostrar(b,80);
    escribir(b,80);
    indicar(b);
    nombremedicamento(b, 80);
    porfarmacia(a,30,80);
}