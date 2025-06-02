from pyperadaptor import pyperclip, waitForNewPaste
from servidor import servidor

"""
if not pyperclip.is_available():
    print("The system clipboard is not supported.")
    exit()
"""

print("PysingScan listening clipboard...")
while True:
    txt = waitForNewPaste()
    print(txt)
    out = servidor(txt)
    print(out)

    pyperclip.copy(out)
