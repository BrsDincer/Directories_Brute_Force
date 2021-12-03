def screen_clear():
    try:
        if name == "nt":
            _ = system("cls")      
        elif name == "posix":
            _ = system("clear")  
        else:
            _ = system("clear")
    except:
        how_to_use()
