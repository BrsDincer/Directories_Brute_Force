def show_myhost_ip():
    try:
        global my_ip
        host_get = socket.gethostname()
        my_ip = socket.gethostbyname(host_get)
        return my_ip
    except:
        how_to_use()
