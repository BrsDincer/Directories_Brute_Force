def get_ip_from_domain(domain_name=str):
    try:
        global main_ip_from_domain
        domain_name = domain_name.replace("https://","").replace("http://","").split("/")
        if len(domain_name) == 1:
            host_ip_from_domain = socket.gethostbyname(domain_name[0])
        else:
            main_ip_from_domain = socket.gethostbyname(domain_name[0].replace("www.",""))
        if 'main_ip_from_domain' in globals():
            return main_ip_from_domain
        else:
            main_ip_from_domain = host_ip_from_domain
            return main_ip_from_domain
    except:
        how_to_use()
