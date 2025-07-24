' ======== PASSWORD DECRYPTION =========
Set WshShell = CreateObject("WScript.Shell")
Set objShell = CreateObject("Shell.Application")
WshShell.Popup "Connecting to secure server...", 2, "Initializing...", 64

Do
    RandomNum = Int((999999999 - 100000000 + 1) * Rnd + 100000000)
    WshShell.Popup "Decrypting password hash: " & RandomNum, 1, "Password Decrypter", 64
Loop
