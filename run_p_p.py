def run_process(url_tar_get=str,text_tar_get=str):
    try:
        show_myhost_ip()
        print("\n")
        print("SESSION HAS BEEN STARTED")
        show_notice()
        time.sleep(1.2)
        print("\n")
        print("\033[1;33m%s\x1b[0m --> %s" % (my_ip, "Your IP Address"))
        define_url(url_tar_get)
        get_ip_from_domain(url_tar_get)
        print("\033[1;33m%s\x1b[0m --> %s" % (main_ip_from_domain, "Your Target IP Address"))
        print("\n")
        time.sleep(1.2)
        print("If you have any doubts, you can prevent it. Do you want to continue?")
        process_fq = str(input("Y/N: ")).replace(" ","").upper()
        if process_fq == "Y":
            time.sleep(1.2)
            print("\n")
            print("PLEASE WAIT, THE PROCESS WILL BE LAUNCHED")
            time.sleep(2.1)
            screen_clear()
            export_txt_file(text_tar_get)
            if Target_URL.endswith("/") == True:
                for x_dir in Cleaning_Header:
                    try:
                        x_dir = str(x_dir)
                        Full_Url = Target_URL+x_dir
                        check_status_code(Full_Url)
                    except:
                        how_to_use()
            elif Target_URL.endswith("/") == False:
                for x_dir in Cleaning_Header:
                    try:
                        x_dir = str(x_dir)
                        Full_Url = Target_URL+"/"+x_dir
                        check_status_code(Full_Url)
                    except:
                        how_to_use()
            else:
                pass
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
