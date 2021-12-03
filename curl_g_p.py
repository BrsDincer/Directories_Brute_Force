def curl_methods_x(defined_url=str,prox_x=str):
    try:
        command = os.popen("curl -k -s --proxy %s %s " % (prox_x, defined_url))
        status = command.read()
        if "302" in status or "connection" in status or "Connection" in status or "found" in status or "Found" in status:
            print(status)
            print("\n")
            print("--> \033[1;32;40m%s\033[0m" % ("GOT RESPONSE - IT'S ALIVE / CHECK HEADER"))
            print("\n")
            time.sleep(2.2)
        else:
            print("--> \033[1;31;40m%s\033[0m" % ("IT COULD BE ALIVE OR NOT - CHECK HEADER STATUS"))
            print("\n")
            print(status)
            print("\n")
            time.sleep(2.2)  
    except:
        pass
