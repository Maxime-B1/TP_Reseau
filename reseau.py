def get_pointed_ip(int_ip):
    """
    Prend en paramètre ip_int, une ip sous forme de nombre et retourne l'ip sous forme décimale pointée
    """
    quotient1 = int_ip//2**8
    reste1 = int_ip%2**8
    quotient2 = quotient1//2**8
    reste2 = quotient1%2**8
    quotient3 = quotient2//2**8
    reste3 = quotient2%2**8
    reste4 = quotient3%2**8
    return '.'.join([str(reste4), str(reste3), str(reste2), str(reste1)])

def get_int_ip(pointed_ip):
    """
    Prend en paramètre ip_pointed, une ip sous forme déciame pointée et retourne l'ip sous forme de nombre
    """
    numbers = [int(elt) for elt in pointed_ip.split('.')]
    number = 0
    number += numbers[0] << 24
    number += numbers[1] << 16
    number += numbers[2] << 8
    number += numbers[3]
    return number

def get_pointed_mask(cidr):
    """
    retourne le masque sous forme d'une ip décimale pointée. Si le CIDR n'est pas conforme, retourne une string vide.
    """
    bin = 0
    compteur = cidr
    binaire = cidr*'1'+(32-cidr)*'0'
    nombre_dec = int(binaire,2)
    return get_pointed_ip(nombre_dec)

assert(get_pointed_mask(4)=='240.0.0.0')
assert(get_pointed_mask(8)=='255.0.0.0')
assert(get_pointed_mask(24)=='255.255.255.0')
