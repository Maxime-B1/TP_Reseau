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
    return get_pointed_ip(int(cidr*'1'+(32-cidr)*'0',2))

assert(get_pointed_mask(4)=='240.0.0.0')
assert(get_pointed_mask(8)=='255.0.0.0')
assert(get_pointed_mask(24)=='255.255.255.0')


def get_int_cidr(mask):
    """
    retourne le cidr correspondant au masque sous forme déciamle pointée
    """
    compteur = 0
    binaire = bin(get_int_ip(mask))[2:]
    for nb in binaire :
        if nb == '1':
            compteur += 1
    return compteur

assert get_int_cidr('240.0.0.0')==4
assert get_int_cidr('255.0.0.0')==8
assert get_int_cidr('255.255.255.0')==24


def get_network_address(ip_cidr):
    """
    paramètre : ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne, sous forme d'adresse IP pointée, l'adresse du réseau
    """
    ensemble = ip_cidr.split('/')
    ip = ensemble[0]
    cidr = ensemble[1]
    mask = get_pointed_mask(int(cidr))

    return get_pointed_ip(get_int_ip(ip)&get_int_ip(mask))

assert get_network_address('192.168.1.40/13') == '192.168.0.0'


def get_nb_ip(pointed_mask):
    """
    pointed_mask : le masque sous forme d'une adresse ip décimale pointée
    retourne le nombre d'adresses ip possibles
    """
    cidr = get_int_cidr(pointed_mask)
    n = 32-int(cidr)
    return 2**n


assert   get_nb_ip('255.255.0.0') == 65536  


def get_nb_hosts(pointed_mask):
    """
    pointed_mask : le masque sous forme d'une adresse ip décimale pointée
    retourne le nombre d'hôtes possibles
    """
    return get_nb_ip(pointed_mask)-2
    
assert   get_nb_hosts('255.255.0.0') == 65534