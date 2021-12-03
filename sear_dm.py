def search_subdomain(url_tar_get=str):
    try:
        show_myhost_ip()
        print("\n")
        print("SESSION HAS BEEN STARTED")
        show_notice()
        print("\n")
        print("\033[1;33m%s\x1b[0m --> %s" % (my_ip, "Your IP Address"))
        time.sleep(1.2)
        print("If you have any doubts, you can prevent it. Do you want to continue?")
        process_fq = str(input("Y/N: ")).replace(" ","").upper()
        print("\n")
        file_ext_list = ["subbf.txt","subbf2.txt","subbf3.txt","subbf4.txt"]
        if process_fq == "Y":
            if "http://" in url_tar_get or "https://" in url_tar_get:
                new_tar = url_tar_get.replace("http://","").replace("https://","")
                for x_tar_lo_f in file_ext_list:
                    with open(x_tar_lo_f, "r") as file_ext:
                        for x_line in file_ext:
                            time.sleep(0.9)
                            tar_word = x_line.strip()
                            x_tar = "http://"+tar_word+"."+new_tar
                            check_status_code(x_tar)      
            else:
                for x_tar_lo_f in file_ext_list:
                    with open(x_tar_lo_f, "r") as file_ext:
                        for x_line in file_ext:
                            time.sleep(0.9)
                            tar_word = x_line.strip()
                            ex_tar = "http://"+tar_word+"."+url_tar_get
                            check_status_code(ex_tar)               
        elif process_fq == "N":
            time.sleep(0.8)
            screen_clear()
            how_to_use()
            pass
        else:
            time.sleep(0.8)
            print("\n")
            how_to_use()
            pass
    except:
        how_to_use()
