import string

def caesar():
    msg = input("Enter message: ")
    s = int(input("Enter shift: "))

    # Create mapping: Shift alphabet by 's' positions
    abc = string.ascii_lowercase
    ABC = string.ascii_uppercase
    
    shifted = abc[s:] + abc[:s] + ABC[s:] + ABC[:s]
    table = str.maketrans(abc + ABC, shifted)
    
    # Encrypt/Decrypt
    enc = msg.translate(table)
    print(f"Encrypted: {enc}")
    
    # To decrypt, we reverse the table mapping
    rev_table = str.maketrans(shifted, abc + ABC)
    print(f"Decrypted: {enc.translate(rev_table)}")

caesar()