import re
from pyperadaptor import pyperclip, waitForNewPaste
from patterns import SENSITIVE_PATTERNS

contador = 0

while True:
    txt = waitForNewPaste()
    contador += 1
    print(f"{str(contador).rjust(3)} -- ORIGINAL: {txt}")
    
    sanitized = txt
    for pattern, replacement in SENSITIVE_PATTERNS:
        sanitized = re.sub(pattern, replacement, sanitized)
    
    if sanitized != txt:
        print(f"{str(contador).rjust(3)} -- SANITIZED: {sanitized}")
        pyperclip.copy(sanitized)
    else:
        print(f"{str(contador).rjust(3)} -- No se detectaron datos sensibles.")