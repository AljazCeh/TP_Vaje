words= {
    "mačka": "Micka ",
    "pes": " Frido ",
    "volk": " Rex ",
    "medved": " Žan ",
    "slon": " Jan ",
    "žirafa": " Helga",
    "lev": " Gašper ",
    "tiger": " Anže" ,
    "papagaj": " Črt" ,
    "ribiva": " Elena" ,
    "krokodil": " Kasper", 
    "zajec": " Lars ",
    "kamela": " Manca"
}
crke= ['r','R']

for value in words.values():
    if value.__contains__(crke[0]) or value.__contains__(crke[1]):
        print(value)


