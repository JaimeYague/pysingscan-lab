import re
from patterns import SENSITIVE_PATTERNS


contador = 0

def servidor(input:str):
    global contador
    contador += 1
    print(f"{str(contador).rjust(3)} -- {input}")


    output = input
    for pattern, replacement in SENSITIVE_PATTERNS:
        output = re.sub(pattern, replacement, output, flags=re.IGNORECASE)

    return output
