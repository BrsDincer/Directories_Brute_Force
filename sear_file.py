def search_file(url_tar_get=str,tar_doc=str):
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
        file_ext_list = ["deeppas.txt","deepfile.txt","deeppwn.txt","vuln.txt","common.txt"]
        if process_fq == "Y":
            for x_tar_lo_f in file_ext_list:
                with open(x_tar_lo_f, "r") as file_ext:
                    for x_line in file_ext:
                        time.sleep(0.9)
                        tar_word = x_line.strip()
                        if "{FILE}" in tar_word: 
                            if "http://" in url_tar_get or "https://" in url_tar_get:
                                if url_tar_get.endswith("/") == True:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = url_tar_get + tar_word.replace("{FILE}",f"{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = url_tar_get + tar_word.replace("{FILE}",f".{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    else:
                                        pass
                                elif url_tar_get.endswith("/") == False:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = url_tar_get + "/" + tar_word.replace("{FILE}",f"{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = url_tar_get + "/" + tar_word.replace("{FILE}",f".{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    else:
                                        pass        
                            else:
                                if url_tar_get.endswith("/") == True:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = "http://" + url_tar_get + tar_word.replace("{FILE}",f"{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = "http://" + url_tar_get + tar_word.replace("{FILE}",f".{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    else:
                                        pass
                                elif url_tar_get.endswith("/") == False:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = "http://" + url_tar_get + "/" + tar_word.replace("{FILE}",f"{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = "http://" + url_tar_get + "/" + tar_word.replace("{FILE}",f".{tar_doc.lower().replace(' ','')}")
                                        check_status_code(new_tar_url)
                                    else:
                                        pass
                        else:
                            if "http://" in url_tar_get or "https://" in url_tar_get:
                                if url_tar_get.endswith("/") == True:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = url_tar_get + tar_word + tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = url_tar_get + tar_word + "." +tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    else:
                                        pass
                                elif url_tar_get.endswith("/") == False:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = url_tar_get + "/" + tar_word + tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = url_tar_get + "/" + tar_word + "." +tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    else:
                                        pass        
                            else:
                                if url_tar_get.endswith("/") == True:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = "http://" + url_tar_get + tar_word + tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = "http://" + url_tar_get + tar_word + "." +tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    else:
                                        pass
                                elif url_tar_get.endswith("/") == False:
                                    if tar_doc.startswith(".") == True:
                                        new_tar_url = "http://" + url_tar_get + "/" + tar_word + tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
                                    elif tar_doc.startswith(".") == False:
                                        new_tar_url = "http://" + url_tar_get + "/" + tar_word + "." +tar_doc.lower().replace(' ','')
                                        check_status_code(new_tar_url)
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
