import re
def validar_email(email):
    if re.findall(r"[A-Za-z]+@dominio\.com$", email):
        return True
    else:
        return False

def validar_tel(tel):
    if re.findall(r"\+([54]{2})\s([0-9]{1})\s([0-9]{2})\s([0-9]{4})-([0-9]{4})", tel) or re.findall(r"([0-9]{2})\s([0-9]{4})-([0-9]{4})", tel):
        return True
    else:
        return False

def validar_cp(cp):
    if re.findall(r"[0-9]{4}$", cp) or re.findall(r"^[a-z]{1}[0-9]{4}[a-z]{3}$", cp):
        return True
    else:
        return False

def validar_fecha(fecha):
    if re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha):
        return True
    else:
        return False

tel = ""
print(validar_fecha(tel))