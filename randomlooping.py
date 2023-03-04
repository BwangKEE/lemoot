import random
from time import sleep
x = 1

hurufkecil = "10"
hurufbesar="10"
angka = "10"
karakter = "10"
string = hurufkecil + hurufbesar + angka + karakter
lenght = 8
while  x >0:
    password = "".join(random.sample(string,lenght) )
    print(" MAU \n"+password)
    sleep(x)
    
