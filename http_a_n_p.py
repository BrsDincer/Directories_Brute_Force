def http_all_methods_no_proxy(defined_url=str):
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
        if "http://" in defined_url or "https://" in defined_url:
            new_tar = defined_url.replace("http://","").replace("https://","")
            x_tar = "https://" + new_tar
            for x_x_m in met_all_l:
                command = os.popen("curl -s -I -X %s %s -m %s" % (x_x_m,x_tar,30))
                try:
                    status_code = command.read().split(" ")[1]
                    if int(status_code) == 200:
                        print("HTTPS %s --> \033[1;32;40m%s\033[0m" % (x_x_m, status_code))
                    else:
                        print("HTTPS %s --> \033[1;37;40m%s\033[0m" % (x_x_m, status_code))
                except:
                    print(x_tar)
                    print(x_x_m, "-- TOO MUCH TIMEOUT/COULD BE BLOCKED IN YOUR REGION")
                    time.sleep(0.8)
                    pass
        else:
            new_tar = defined_url.replace("http://","").replace("https://","")
            x_tar = "https://" + new_tar
            for x_x_m in met_all_l:
                command = os.popen("curl -s -I -X %s %s -m %s" % (x_x_m,x_tar,30))
                try:
                    status_code = command.read().split(" ")[1]
                    if int(status_code) == 200:
                        print("HTTPS %s --> \033[1;32;40m%s\033[0m ACTIVE" % (x_x_m, status_code))
                    else:
                        print("HTTPS %s --> \033[1;37;40m%s\033[0m CHECK CODE" % (x_x_m, status_code))
                except:
                    print(x_tar)
                    print(x_x_m, "-- TOO MUCH TIMEOUT/SITE COULD BE BLOCKED IN YOUR REGION")
                    time.sleep(0.8)
                    pass
    except:
        how_to_use()
