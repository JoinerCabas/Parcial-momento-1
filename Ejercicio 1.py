MontoTotal = int(input("Ingrese el monto de la compra"))
if (MontoTotal < 50):
    print ("No hay descuento")
elif (MontoTotal <=50 >=100):
    Descuento1 = MontoTotal * 0.5
    TotalPago1 = MontoTotal - Descuento1
    print ("Descuento aplicado",Descuento1)
    print ("Total a pagar: $",TotalPago1)
elif (MontoTotal > 100):
    Descuento2 = MontoTotal * 0.10
    TotalPago2 = MontoTotal - Descuento2
    print ("Descuento aplicado",Descuento2)
    print ("Total a pagar: $",TotalPago2)
    
