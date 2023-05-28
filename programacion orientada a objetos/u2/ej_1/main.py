from clase import Email
import csv
import re

def verificar(fila:list[Email])->bool:
    patron=r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
    if re.match(patron,fila):
        print("\nDireccion valida.")
        return True
    else: 
        print("\nDireccion invalida.")

def test():
    #datos correctos
    email1=Email("juan", "gmail", "com", "12345")
    print("\nCaso correcto:", email1.retornarMail())
    #datos incorrectos
    email2=Email("", "gmail", "com", "12345")
    print("\nCaso incorrecto:", email2.retornarMail())

    assert email1.verificarContraseña("12345")  #debería ser True
    assert not email1.verificarContraseña("54321")  #debería ser False
    email1.modificarContraseña("54321")

    #datos correctos
    c=Email("","","","")
    email3=c.crearCuenta("pedro@gmail.com")
    print("\nCaso correcto:", email3.retornarMail())
    #datos incorrectos
    c=Email("","","","")
    email4=c.crearCuenta("pedro@.com")
    print("\nCaso incorrecto:", email4.retornarMail())

    assert verificar("maria@yahoo.com")
    assert not verificar("maria@@yahoo.com")

def test2(lista: list["Email"]):
    #datos correctos
    assert Email.cantDominios("gmail", lista)
    #datos incorrectos
    assert not Email.cantDominios("1234", lista)

if __name__== "__main__":
    test()
    nombre=input("Ingrese su nombre: ")
    correo=Email(
        input("Id cuenta: "),
        input("Dominio: "),
        input("Tipo de dominio: "),
        input("Contraseña: "),
        )
    print("Estimado " + nombre + " te enviaremos tus mensajes a la direccion " + correo.retornarMail())

    print("\nMODIFICAR CONTRASEÑA")
    if correo.verificarContraseña(input("Ingrese su contraseña actual: ")):
        correo.modificarContraseña(input("Ingrese su nueva contraseña: "))

    print("\nCREAR CUENTA A PARTIR DE DIRECCION DE CORREO")
    c=Email("","","","")
    nuevocorreo=c.crearCuenta(input("Ingrese la direccion de correo: "))  
 
    print("\nCUENTAS DE ARCHIVO CSV")
    lista=[]
    with open("test.csv","r") as testfile:
        reader=csv.reader(testfile,delimiter=",")
        for fila in reader: 
            if verificar(fila[0]):
                mail=Email("","","","")
                email=mail.crearCuenta(fila[0])
                lista.append(email)
    testfile.close()
    test2(lista)
    Email.cantDominios(input("Ingrese el dominio a buscar: "), lista)
