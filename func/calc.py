import sys, hashlib
#############################################################################################
algoritmos = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "sha3_256", "sha3_512", "blake2b", "blake2s"]

def hash(valor):
    archivo_salida = "ALGORITMOS"
    for algoritmo in algoritmos:
        hash_algoritmo = hashlib.new(algoritmo)
        hash_algoritmo.update(valor.encode("utf-8"))
        archivo_salida += "\n\n{}\n{}".format(algoritmo.upper(), hash_algoritmo.hexdigest())
    print(archivo_salida)

def hash_archivo(filepath):
    archivo_salida = "ALGORITMOS"
    try:
        with open(filepath, "rb") as f:
            for algoritmo in algoritmos:
                hash_algoritmo = hashlib.new(algoritmo)
                f.seek(0)
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_algoritmo.update(chunk)
                archivo_salida += "\n\n{}\n{}".format(algoritmo.upper(), hash_algoritmo.hexdigest())
        print(archivo_salida)
    except Exception as e:
        print("ERROR: ", e)
#############################################################################################
def dec_bin(dec):
    print(bin(int(dec)).replace("0b",""))

def dec_hex(dec):
    print(hex(int(dec)).replace("0x",""))

def bin_dec(bin):
    print(int(bin, 2))
#############################################################################################
if str(sys.argv[1]) == "func1":
    dec_bin(str(sys.argv[2]))
if str(sys.argv[1]) == "func2":
    dec_hex(str(sys.argv[2]))
if str(sys.argv[1]) == "func3":
    hash(str(sys.argv[2]))
if str(sys.argv[1]) == "func4":
    hash_archivo(str(sys.argv[2]))
if str(sys.argv[1]) == "func5":
    bin_dec(str(sys.argv[2]))