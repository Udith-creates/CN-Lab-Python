def char_stuff():
    data = input("Enter data: ") # Example: A FLAG B ESC C
    
    # Stuffing: ESC must be stuffed before FLAG or another ESC
    # We replace ESC first to avoid double-stuffing the stuffed ESC
    stuffed = data.replace("ESC", "ESC ESC").replace("FLAG", "ESC FLAG")
    frame = f"FLAG {stuffed} FLAG"
    print(f"Stuffed Frame: {frame}")
    
    # De-stuffing: Remove the outer flags, then reverse the replacements
    core = frame[5:-5]
    destuffed = core.replace("ESC FLAG", "FLAG").replace("ESC ESC", "ESC")
    print(f"De-stuffed Data: {destuffed}")

char_stuff()