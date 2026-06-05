def calculo (val):
    acumulador=0
    for i in val:
        acumulador = acumulador + i
    promedio = acumulador /5
    return promedio
lista=[]
materias = ["Matematica", "fundamento de la progracion", "devops","inteligencia artificia", "ciencia de datos"]

print("==============Centro de calificaciones==============")
print("Ramos:\n 1)Matematica\n 2)fundamento de la progracion\n 3)devops\n 4)inteligencia artificial\n 5)ciencia de datos\n")
for i in range (0,5):
    nombre = materias[i]
    while True:
        try:
            calificacion = int(input(f"Ingrese las notas de {nombre}\n"))  
            break    
        except ValueError:
            print("Entre en error")
    lista.append(calificacion)

Npromedio= calculo(lista)
print(f"Tu promedio es {Npromedio} ")

while True:
    decicion= input("QUIERES SABER LA NOTA INDIVIDUAL DE RAMO?\n 1)SI\n 2)NO\n").upper()
    if decicion == "SI":
       
        enblucle = True
        break
    elif decicion =="NO":
        enblucle= False
        print("Gracias por tu tiempo")
        break
    else:
        print("error digite solo variables validas")
        
        
        
        
while enblucle:
    eleccion = input("Que ramo quieres preguntar: ")
    if eleccion == "1":
        ramo = materias[0]
        nota = lista[0]
        print(f"Tu ramo escogido es {ramo} y tu nota es {nota}")
        break
    elif eleccion == "2":
        ramo = materias[1]
        nota = lista[1]
        print(f"Tu ramo escogido es {ramo} y tu nota es {nota}")
        break
    elif eleccion == "3":
        ramo = materias[2]
        nota = lista[2]
        print(f"Tu ramo escogido es {ramo} y tu nota es {nota}")
        break
    elif eleccion == "4":
        ramo = materias[3]
        nota = lista[3]
        print(f"Tu ramo escogido es {ramo} y tu nota es {nota}")
        break
    elif eleccion == "5":
        ramo = materias[4]
        nota = lista[4]
        print(f"Tu ramo escogido es {ramo} y tu nota es {nota}")
        break
    else: 
        print("Elige una opcion valida")




   
    











