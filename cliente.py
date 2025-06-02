from pyperadaptor import pyperclip, waitForNewPaste
from servidor import servidor


while True:
    txt = waitForNewPaste()
    print(txt)
    out = servidor(txt)
    print(out)

    pyperclip.copy(out)
