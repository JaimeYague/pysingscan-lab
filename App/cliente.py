from pyperadaptor import pyperclip, waitForNewPaste
from replacement import replace

"""
if not pyperclip.is_available():
    print("The system clipboard is not supported.")
    exit()
    """

print("PysingScan listening clipboard...")
while True:
    txt = waitForNewPaste()
    print(txt)
    out = replace(txt)
    print(out)

    pyperclip.copy(out)
