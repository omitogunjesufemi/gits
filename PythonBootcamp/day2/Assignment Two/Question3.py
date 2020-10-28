# Claculating Gratuity
subtotal = float(input("Enter the subtotal: "))
gratuity_rate = float(input("Enter the gratuity rate: "))
gratuity = subtotal * (gratuity_rate/100)
total = subtotal * (1 + (gratuity_rate/100)) 
print("The gratuity is " +str(gratuity), "and the total is " +str(total))