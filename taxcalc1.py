income=float(input("income="))

if income<10000:
    rate=0.0
else:
    if income<20000:
        rate=0.10
    else:
        if income<40000:
            rate=0.20
        else:
            rate=0.40

tax=income*rate
print("Your tax rate is "+str(100*rate)+"%")
print("You have to pay "+str(tax)+"€ in taxes.")
#klaniari
