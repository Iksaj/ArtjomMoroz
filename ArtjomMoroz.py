#from random import * 
#P=randint(2,10)
#print(f"Sõprade arv: {P}")
#pitsa_hind=12.90
#hind_jootrahaga=1.1*pitsa_hind
#maksumus=hind_jootrahaga/P
#print(f"Iga sõber peab maksma: {maksumus:.2f}  euro")
#print(f"Iga sõber peab maksma: {round(maksumus,2)} euro")

#Arvutame kolmnurha ümbermõõdu. Küsu kolm täisarvulist muutujat a, b, c.
#Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

#while True:
#    try:
#        a=int(input("Sisesta kolmnurga a külje pikkus: "))
#        break
#    except:
#        print("Viga! Palun sisesta täisarv!")
#while True:
#    try:
#        b=int(input("Sisesta kolmnurga b külje pikkus: "))
#        break
#    except:
#        print("Viga! Palun sisesta täisarv!")
#while True:
#    try:
#        c=int(input("Sisesta kolmnurga c külje pikkus: "))
#        break
#    except:
#        print("Viga! Palun sisesta täisarv!")
#
#if a>0 and b>0 and c>0:
#    print("Kõik küljed on positiivsed.")
#    print("Kontrollime. Kas nad on kolmnurga küljed?")
#    if a+b>c and a+c>b and b+c>a:
#        print("Jah, need on ühe kolmnurga küljed.")
#        P=a+b+c
#    else:
#        print("Ei, sellist, kolmnurka ei saa olemas olla.")
#print("Lõpp.")

#t_arvud=0
#for i in range(15):
#    arv = input("Sisesta arv: ")
#    try:
#        int_arv = int(arv)
#        print(f"{arv} on täisarv.")
#        t_arvud+=1
#    except ValueError:
#        print(f"{arv} ei ole täisarv")
#print(f"Sisestatud {t_arvud} täisarvu")


#t_arvud = 0
#count = 0
#while True:
#    arv = input("Sisesta arv: ")
#    try:
#        int_arv = int(arv)
#        print(f"{arv} on täisarv.")
#        t_arvud+=1
#    except ValueError:
#        print(f"{arv} ei ole täisarv!")
#        count+=1
#
#        if count == 15: break
#
#        print(f"{t_arvud} täisarv.")


#t_arvud=0
#count= 0
#while count<=15:
#    arv=input("Sisesta arv: ")
#    try:
#        int_arv= int(arv)
#        print(f"{arv} on täisarv.")
#        t_arvud+=1
#    except ValueError:
#        print(f"{arv} ei ole täisarv.")
#    count += 1
#print(f"Sisestatud arvudest on {t_arvud} täisarvu.")

#summa = 0
#while True:
#    try:
#        a = int(input("Sisesta arv:"))
#        if a > 0:
#            print("Arv on naturaalne.")
#            break
#    except ValueError:
#            print("Arv ei ole naturaalne!")
#
#for i in range(1,a + 1):
#    summa += i
#print(f"Summa on {summa}")

