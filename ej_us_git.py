import os
import msvcrt

cuentas=[]

while True:
    os.system("cls")
    print("Netflix")
    print("-----------------------")
    print("1-iniciar secion")
    print("2-Registrar usuario")
    print("3-Eliminar usuario")
    print("4-Salir")

    while True:
        try:
            opcion=int(input("ingrese la opcion que desee: "))
            if opcion<=4 and opcion>=1:
                break
            else:
                print("opcion escrita no esta dentro de los parametros")
        except:
            print("valor ingreado invalido")
    if opcion==1:
        os.system("cls")
        i=0
        iniciada="no"
        print("inicio secion")
        pregunta=input("usuario: ")
        pregunta_clave=input("clave: ")
        while i<len(cuentas):
            if cuentas[i]["nombre"]==pregunta and cuentas[i]["clave"]==pregunta_clave:
                print("Secion iniciada con exito")
                iniciada="si"
                break
            i=i+1
        if iniciada=="no":
            print("usuario y/o clave erronea")
        print("presione cualquier tecla para continuar")
        msvcrt.getch()


    elif opcion==2:
        nombre=input("ingrese el nombre que usara en esta cuenta: ")
        clave=input("ingrese la clave que desee: ")

        usuario={
            "nombre":nombre,
            "clave":clave
            }
        cuentas.append(usuario)
        print("Usuario agregado con exito")
        print("presione cualquier tecla para continuar")
        msvcrt.getch()


    elif opcion==3:
        pass


    else:
        print("Adios")
        break