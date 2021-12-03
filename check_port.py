def checking_port(url_tar_get=str):
    try:
        get_ip_from_domain(url_tar_get)
        print("\n")
        show_notice()
        time.sleep(1.2)
        print("\n")
        print("\033[1;37m%s\x1b[0m -- %s" % (main_ip_from_domain,"TARGET IP"))
        print("\n")
        time.sleep(1.2)
        print("If you have any doubts, you can prevent it. Do you want to continue?")
        process_fq = str(input("Y/N: ")).replace(" ","").upper()
        time.sleep(1.2)
        print("\n")
        if process_fq == "Y":
            print("SESSION HAS BEEN STARTED")
            print("\n")
            time.sleep(1.2)
            Port_List = [20,21,22,23,25,53,65,67,
                      68,69,80,101,102,105,107,
                      109,110,111,113,115,117,119,
                      123,137,138,139,143,161,162,
                      163,164,174,177,178,179,389,
                      443,444,500,535,611,631,636,
                      765,767,873,989,990,992,993,994,995,3389]
            for x_all_range in Port_List:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                location = (main_ip_from_domain, x_all_range)
                result_of_check = s.connect_ex(location)
                s.close()
                if result_of_check == 0:
                    print("\033[1;32m%s\x1b[0m -- %s -- %s" % (x_all_range,"[+] OPEN",result_of_check))
                else:
                    print("\033[1;31m%s\x1b[0m -- %s -- %s" % (x_all_range,"[-] CLOSE",result_of_check))
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
