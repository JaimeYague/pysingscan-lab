from pyperadaptor import pyperclip, waitForNewPaste

contador = 0

while True:
    txt = waitForNewPaste()
    contador += 1
    print(f"{str(contador).rjust(3)} -- {txt}")
    txt = txt.replace("SENSIBLE", "CENSURADO")
    pyperclip.copy(txt)
