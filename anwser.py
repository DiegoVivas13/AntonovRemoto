costod=0
costop=0
dist=float(input("digite la distancia en kilometros: "))
tipo_vuelo=str(input("segun su tipo de vuelo, escriba nacio si es nacional o inter si es internacional"))
cont_peso=0
while cont_peso <=(250000*0.95):
    if tipo_vuelo==("nacio"):
        peso=float(input("digite el peso del paquete"))
        if peso<10:
            print("el peso no es aceptable")
        elif (peso>250000) and (cont_peso+peso>250000):
            print("el peso es exedido")
        else:
            Cont_peso= cont_peso+peso
            if peso>100:
                Costop=costop+(peso*4500)*0.85
                Costod= dist*4000
            else:
                Costop=costop+(peso*4500)
                Costod= dist*4000
    else:
        peso=float(input("digite el peso del paquete"))
        if peso<10:
            print("el peso no es aceptable")
        elif (peso>250000) and (cont_peso+peso>250000):
            print("el peso es exedido")
        else:
            Cont_peso= cont_peso+peso
            if dist>8000 and peso>400:
                Costop=costop+(peso*4500)
                Costod= (dist*12872)*0.9
            else:
                Costop=costop+(peso*4500)
                Costod= dist*12872
costo_total=costop+costod
print("el costo total es", costo_total)