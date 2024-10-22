import re
#EJ3
def partes(email):
    if re.match(r"^[a-zA-Z0-9]+@uade\.edu\.ar$", email) != None:
        palabra = re.findall(r"\w+", email)
        return palabra
    else:
        print("Email no válido")
        return 0
    
print(partes("alguien@uade.edu.ar"))