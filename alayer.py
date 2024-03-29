# alayer 1.0
# Tugas ET3107 Pemrograman Lanjut
# Mengubah suatu kalimat menjadi alay
# dengan memanfaatkan bilangan random
# Collaborator:
# - Fikri F. Akbar 18115011 - github: fikfak 
# - Rama Rahardi 18117026 - github: ramhdi
# Created on Mon Sep  9 09:28:35 2019

import random

def alaykeun(str_in):
    output = ""
    size = len(str_in)
    ch = 0
    inc = 0

    # iterasi pada masing-masing elemen string masukan
    # setiap iterasi ada bilangan random yang dibangkitkan
    # yang dapat bernilai 0-2
    # jika mendapat angka 1, huruf diubah menjadi upper case
    # jika mendapat angka 2, huruf diubah menjadi angka yang mirip atau menjadi huruf yang mirip
    while (ch < size):
        res = str_in[ch]
        inc = random.randint(0,2)
        
        # print(inc)
        if (inc >= 1):
            # buat ngedobel huruf terakhir
            if (str_in[ch] == " "):
                res = chr(ord(str_in[ch-1])-32) + " "
            # lower case jd upper case
            if (ord(str_in[ch]) >= 97 and ord(str_in[ch]) <= 122 and inc == 1):
                res = chr(ord(str_in[ch]) - 32)
                
            elif (inc == 2):
                if (str_in[ch] == "a" or str_in[ch] == "A"):
                    res = "4"
                    
                elif (str_in[ch] == "e" or str_in[ch] == "E"):
                    res = "3"
                    
                elif (str_in[ch] == "i" or str_in[ch] == "I"):
                    res = "1"
                    
                elif (str_in[ch] == "o" or str_in[ch] == "O"):
                    res = "0"
                    
                elif (str_in[ch] == "k"):
                    res = "Q"
                
                elif (str_in[ch] == "K"):
                    res = "q"
                    
                elif (str_in[ch] == "u"):
                    res = "W"
                    
                elif (str_in[ch] == "U"):
                    res = "w"
        
        output += res
        ch += 1
    
    return output

# main loop
while True:
    str_in = input("Tidak alay: " )
    str_out = alaykeun(str_in)
    print("Alay: " + str_out)
