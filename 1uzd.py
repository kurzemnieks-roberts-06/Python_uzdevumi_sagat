"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) ar kādiem cipariem tiek ikdienā strādāts? Arābu cipari (pavisam 10)
2) Romiešu cipari I, V, X, D, C, M .... cipari veido skaitli
3) kas ir klase? Klase sastāv no konstruktora vai destruktora un metodēm( iekšējās funkcijas)
kādas datu struktūras zinam? 
    list (saraksts) a="" - tukš saraksts
    arry (masīvs) a=[]
    dict (vārdnīca) {}  dict()
5) kass ir vārdnīca? viena kolona ir atslēga, bet otra ir vērtība 
"""
class AAA:
    #definēju konstruktoru
    def __init__(self):
        self.rome_sk={
        1:'I',
        4:'IV',
        5:'V',
        9: 'IX', 
        10: 'X', 
        40: 'XL', 
        50: 'L', 
        90: 'XC', 
        100: 'C', 
        400: 'CD', 
        500: 'D', 
        900: 'CM', 
        1000: 'M'
        }
        #tā ir metode, tas ir funkcija, kura veiks pārveidošau
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result
    
#izveidojam objektu
kk=AAA()
skaitlis=21
#izsaucam klases iekšējo funkciju (metode)
rom_sks=kk.to_roman(skaitlis)
print(f"{skaitlis} romiešu cipros ir {rom_sks}")