/*Ejercicio 3: Se registra la información de las operaciones realizadas por un cajero durante un fin de semana. De cada operación 
se conoce: numero de operación, importe y tipo de operación (1: cobro; 2: pago). Utilizando funciones óptimas realice lo siguiente: 
a) Genere una lista con la información de las operaciones. 
b) Indique cual es el/los numero/s de mayor importe cobrado. (usar una función recursiva) 
c) Con la información de la lista genere un archivo con los datos de los pagos realizados. 
d) Eliminar la lista generada. 
e) Indicar en el principal el importe promedio de los pagos realizados. 
f) Eliminar del archivo los pagos menores a $500.*/

/*Exercise 3: The information of the operations carried out by a cashier during a weekend is recorded. of each operation
is known: operation number, amount and type of operation (1: collection; 2: payment). Using optimal functions do the following:
a) Generate a list with the information of the operations.
b) Indicate which is the number(s) with the highest amount collected. (to use a recursive function)
c) With the information from the list, generate a file with the data of the payments made.
d) Delete the generated list.
e) Indicate in the principal the average amount of the payments made.
f) Eliminate payments under $500 from the file.*/
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <windows.h>

typedef struct{
    int nro,tipo;
    float imp;
}operaciones;

struct nodo{
    operaciones op;
    struct nodo *sig;
};

typedef struct nodo *puntero;

void carga(puntero &cab){
    int nro;
    printf("Ingrese el numero de operacion, finalice con 0.\n");
    scanf("%d",&nro);
    while(nro!=0){
        puntero nuevo=(puntero)malloc(sizeof(struct nodo));
        nuevo->sig=cab;
        cab=nuevo;
        printf("Ingrese el tipo de operacion.\n");
        scanf("%d",&nuevo->op.tipo);
        printf("Ingrese el importe.\n");
        scanf("%f",&nuevo->op.imp);
        printf("Operacion registrada.\n");
        nuevo->op.nro=nro;
        Sleep(500);
        system("cls");
        printf("Ingrese el numero de operacion, finalice con 0.\n");
        scanf("%d",&nro);
    }
}

static void mayor(puntero cab, float &m){
    if(cab==NULL) return;
    else{
        if((cab->op.imp>m) && (cab->op.tipo==1)) m=cab->op.imp;
        mayor(cab->sig,m);
    }
}

static void cuentamayores(puntero cab, float m, int &c){
    if(cab!=NULL){
        if((cab->op.imp==m) && (cab->op.tipo==1)) c++;
        cuentamayores(cab->sig,m,c);
    } else return;
}

static void cargamayores(puntero cab, float m, int i, int *a){
    if(cab==NULL) return;
    else{
        if(cab->op.imp == m){
            a[i]=cab->op.nro;
            cargamayores(cab->sig,m,i+1,a);
        }
        cargamayores(cab->sig,m,i,a);
    }
}

static void muestramayores(int *a, int i, int N){
    if(i<N){
        printf("Numero de operacion con mayor importe: %d.\n",a[i]);
        muestramayores(a,i+1,N);
    }
}

void mayores(puntero cab){
    float max=0;
    int cant=0,*a;
    mayor(cab,max);
    cuentamayores(cab,max,cant);
    a=(int*)malloc(sizeof(int)*cant);    
    cargamayores(cab,max,0,a);
    muestramayores(a,0,cant);
}

void generar(puntero x, FILE *archi){
    operaciones a;
    while(x!=NULL){
        a.imp=x->op.imp;
        a.nro=x->op.nro;
        a.tipo=x->op.tipo;
        fwrite(&a,sizeof(a),1,archi);
        x=x->sig;
    }
}

void liberarlista(puntero &x){
    puntero aux;
    while(x!=NULL){
        aux=x;
        x=x->sig;
        free(aux);
    }
}

float promedio(FILE *archi){
    operaciones a;
    int cont=0;
    float cant=0;
    rewind(archi);
    while((fread(&a,sizeof(a),1,archi)) && (a.tipo==2)){
        cant+=a.imp;
        cont++;
    }
    return(cant/cont);
}

void marcar(FILE *archi){
    int i=0;
    operaciones a;
    fseek(archi,0,SEEK_SET);
    while((i==0) && (fread(&a,sizeof(a),1,archi))){
        if(a.imp<500) i=1;
        if(i==1){
            fseek(archi,-sizeof(a),SEEK_CUR);
            a.imp=-1;
            fwrite(&a,sizeof(a),1,archi);
        }
        i=0;
    }  
}

void eliminar(FILE *archi, FILE *aux){
    operaciones a;
    marcar(archi);
    fseek(archi,0,SEEK_SET);
    while(fread(&a,sizeof(a),1,archi)){
        if(a.imp!=-1){
            fwrite(&a,sizeof(a),1,aux);
        }
    }
}

int main(){
    FILE *archi, *aux;
    puntero cab=NULL;
    carga(cab);
    system("pause");
    system("cls");
    mayores(cab);
    system("pause");
    system("cls");
    if((archi=fopen("operaciones.dat","wb+"))==NULL){
        printf("Error.\n");
    }else{
        generar(cab,archi);
        liberarlista(cab);
        printf("El importe promedio es: %.2f",promedio(archi));
        system("cls");
        aux=fopen("auxiliar.dat","wb+");
        eliminar(archi,aux);
        fclose(archi);
        fclose(aux);
        remove("operaciones.dat");
        rename("auxiliar.dat","operaciones.dat");
    }
} 