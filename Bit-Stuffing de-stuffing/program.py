import re

def hdlc():
    data = input("Enter binary data: ")
    
    # Stuffing: Find five 1s, add a '0' after them
    stuffed = re.sub(r'11111', '111110', data)
    frame = f"01111110{stuffed}01111110"
    print(f"Frame: {frame}")
    
    # De-stuffing: Remove flags, then find five 1s and remove the '0' that follows
    core = frame[8:-8]
    destuffed = re.sub(r'(11111)0', r'\1', core)
    print(f"Data:  {destuffed}")

hdlc()