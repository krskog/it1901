def parser():
    alt = []
    f = open('tekst.txt','r')
    for n in f:
        #Renser ut det som ikke er i nærheten, ved "@", ";", og "/" 
        if '@' in n and ';' in n and '/' in n:
            alt.append(n)
    for isil in alt:
        if(valide(isil) != False):
            return valide(isil)
        else:
            #Ikke legg til blant reservasjonsforespørslene. For-løkken får kjøre videre.

#Finfilteret
def valide(res):
    koie = ''
    epost = ''
    dato = ''
    #a går igjen i hele filteret, da det er de groveste res.format-splittene
    #a er reserversjonsformatet splittet, hvorav a[0] er koienavn, a[1] er e-post
    #og a[2] er dato
    a = res.split(';')
    #Finner koienavn
    if ' ' in a[0]:
        b = a[0].split(' ')
        c = len(b)
        koie = b[c-1]
    else:
        koie = a[0].strip(' ')
    #Sørger for at e-postfeltet ser nogenlunde ut
    if '@' in a[1]:
        e = a[1].split('@')
        if not '.' in e[1]:
            return False
        else:
            epost = a[1]
    else:
        return False
#Sjekker at datoen er oppgitt i siffer, er riktig inndelt, og er "lang" nok.
    if(len(a[2])==10 ):
        de = a[2].split('/')
        for ne in de:
            if(ne.isdigit == False):
                return False
        if(len(de[0]) == 2 and len(de[1]) == 2 and len(de[2]) == 4):
            dato = a[2]
        else:
            return False
    else:
        return False
    #Setter sammen formatet etter å ha renset evt. feil ved koienavnet.
    #Ut er reservasjonsformatet som blir returnet dersom reservasjonen er valid
    ut = ''
    ut+= koie
    ut += ";"
    ut += epost
    ut += ";"
    ut+= dato
    return ut

print(parser())          
    
        
