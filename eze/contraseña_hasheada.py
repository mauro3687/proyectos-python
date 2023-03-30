import hashli 

encontrada = 0
input_hash =input("inserte la contraseña hassheada: ")
pass_doc = input("inserte el diccionario: ")

try:
    pass_file =open(pass_doc,"r")
except:
    print("error:" + pass_doc +"no ha sido encontrada")

for palabra in pass_file:
    palabra_cifrada=palabra.encode("utf-8")
    palabra_hasheada=hashli.md5(palabra_cifrada.strip())
    dihest=palabra_hasheada.hexdigest()

    if digest ** input_hash:
        print("contraseña encontrada!!!"
        
