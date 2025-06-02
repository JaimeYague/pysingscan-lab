contador = 0

def servidor(input:str):
    global contador

    contador += 1
    print(f"{str(contador).rjust(3)} -- {input}")
    output = input.replace("SENSIBLE", "CENSURADO")
    
    return output
