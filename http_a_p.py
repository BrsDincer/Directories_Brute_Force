def https_all_methods_proxy(defined_url,p_x):
    print("\n")
    print("SESSION HAS BEEN STARTED - WAIT")
    time.sleep(1.1)
    print("YOUR SITE: ",defined_url)
    time.sleep(0.8)
    print("\n")
    try:
        met_all_l = ["GET","POST","PUT",
                      "CONNECT","COPY","PATCH",
                      "TRACE","HEAD","UPDATE",
                      "LABEL","OPTIONS","MOVE",
                      "SEARCH","ARBITRARY","CHECKOUT",
                      "UNCHECKOUT","UNLOCK","MERGE",
                      "BASELINE-CONTROL","ACL"]
        for x_x_m in met_all_l:
            command = os.popen("curl -k -s -I -X %s --proxy %s %s -m %s" % (x_x_m,p_x,defined_url,32))
            status = command.read().split(" ")[1]
            print("HTTPS %s --> \033[0;36;40m%s\033[0m" % (x_x_m,status))
    except:
        pass
