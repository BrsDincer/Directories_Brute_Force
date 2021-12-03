def show_status_ip(host_ip=str,port_ip=int):
    try:
        global status_result
        socket_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status_result = socket_host.connect_ex((host_ip,port_ip))
        socket_host.close()
        return status_result
    except:
        how_to_use()
