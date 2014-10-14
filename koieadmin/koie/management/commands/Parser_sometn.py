def parser():
    alt = []
    f = open('tekst.txt','r')
    for n in f:
        if '@' in n and ';' in n and '/' in n:
            alt.append(n)
    for isil in alt:
        if(valide(isil) != False):
            return valide(isil)
        
def valide(res):
    koie = ''
    epost = ''
    dato = ''
    a = res.split(';')
    if ' ' in a[0]:
        b = a[0].split(' ')
        c = len(b)
        koie = b[c-1]
    else:
        koie = a[0].strip(' ')

    if '@' in a[1]:
        e = a[1].split('@')
        if not '.' in e[1]:
            return False
        else:
            epost = a[1]
    else:
        return False

    if(len(a[2])==10 ):
        de = a[2].split('/')
        for ne in de:
            if not ne.isdigit():
                return False
        dato = a[2]
    else:
        return False
    ut = ''
    ut+= koie
    ut += ";"
    ut += epost
    ut += ";"
    ut+= dato
    return ut

print(parser())          
    
        
