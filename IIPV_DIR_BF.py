from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import time
from optparse import OptionParser as optparse
import random
import json
import socket
from os import system, name
import os
import sys
import warnings
            
warnings.filterwarnings(action="ignore",message="CHECK PYTHON VERSION")
warnings.filterwarnings(action="ignore",message="ALREADY IMPORTED",category=UserWarning)
warnings.filterwarnings(action="ignore",category=DeprecationWarning)


def show_notice():
    
    log_ipp_v = """
    
     IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
     I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
     I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
     II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
       I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
       I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
       I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
       I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
       I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
       I::::I    I::::I            P::::P                       V:::::V V:::::V      
       I::::I    I::::I            P::::P                        V:::::V:::::V       
       I::::I    I::::I            P::::P                         V:::::::::V        
     II::::::IIII::::::II        PP::::::PP                        V:::::::V         
     I::::::::II::::::::I ...... P::::::::P                         V:::::V          
     I01000110II00110100I .::::. P01000110P                          V:::V           
     IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV 
    
    
    """
    
    Message_War = "When using this tool, please make sure to use VPN or take additional precautions to hide your IP identity"
    
    print(log_ipp_v)
    print("\032[1;36m%s\x1b[0m" % (Message_War))
    
    
def cen_notice():
    
    log_ipp_v = """
    
     IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
     I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
     I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
     II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
       I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
       I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
       I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
       I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
       I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
       I::::I    I::::I            P::::P                       V:::::V V:::::V      
       I::::I    I::::I            P::::P                        V:::::V:::::V       
       I::::I    I::::I            P::::P                         V:::::::::V        
     II::::::IIII::::::II        PP::::::PP                        V:::::::V         
     I::::::::II::::::::I ...... P::::::::P                         V:::::V          
     I01000110II00110100I .::::. P01000110P                          V:::V           
     IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV 
    
    
    """
    Message_Note = """
    
    
    The censorship control application takes place in 3 stages.
    
    [NOTED]
    
    This process may differ depending on your internet connection and permissions.
    If you are getting an additional error, please check your settings and permissions.
    
    PROXY WILL BE SELECTED RANDOMLY (for 2 - 3), PLEASE MAKE SURE YOU ARE USING VPN

    1) QUICK CONTROL WITH STANDARD HTTPS METHODS
    
    2) ACCESSIBILITY CHECK WITH VARIOUS PROXY CONNECTIONS (CAN TAKE A LONG TIME)
    
    3) HTTPS METHOD CONTROL WITH PROXY CONNECTIONS (CAN TAKE A LONG TIME)
    
    [!] '/' FOR EXIT
    
    PLEASE CONTINUE PROCESSING BY ENTERING THE NUMBER CORRECTING THE METHODS

    
    """
    print(log_ipp_v)
    print("\032[1;36m%s\x1b[0m" % (Message_Note))
    

def how_to_use():

    print("""
          
          
     IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
     I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
     I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
     II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
       I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
       I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
       I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
       I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
       I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
       I::::I    I::::I            P::::P                       V:::::V V:::::V      
       I::::I    I::::I            P::::P                        V:::::V:::::V       
       I::::I    I::::I            P::::P                         V:::::::::V        
     II::::::IIII::::::II        PP::::::PP                        V:::::::V         
     I::::::::II::::::::I ...... P::::::::P                         V:::::V          
     I01000110II00110100I .::::. P01000110P                          V:::V           
     IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      


          py DIRBF_RUN.py -d https://example.com [or] py DIRBF_RUN.py --bfdir  https://example.com
          py DIRBF_RUN.py -p https://example.com [or] py DIRBF_RUN.py --portcheck https://example.com
          py DIRBF_RUN.py -a https://example.com [or] py DIRBF_RUN.py --bfdetail https://example.com
          py DIRBF_RUN.py -v https://example.com [or] py DIRBF_RUN.py --bfvul https://example.com
          py DIRBF_RUN.py -f https://example.com txt [or] py DIRBF_RUN.py --bffile https://example.com txt
          py DIRBF_RUN.py -s https://example.com [or] py DIRBF_RUN.py --bfsub https://example.com
          py DIRBF_RUN.py -c https://example.com [or] py DIRBF_RUN.py --censorshipcheck https://example.com
          
          
          -h / --help : Help
          
          -d / --bfdir : Search for common directories
          -a / --bfdetail : Search for all of directories
          -v / --bfvul : Search for all of site directories vulnerabilities
          -f / --bffile : Search for file directories
          -s / --bfsub : Search for subdomains
          -p / --portcheck : Check for common port - open or close
          -c / --censorshipcheck : Check censorship
          
          
          """)




def show_myhost_ip():
    try:
        global my_ip
        host_get = socket.gethostname()
        my_ip = socket.gethostbyname(host_get)
        return my_ip
    except:
        how_to_use()
    

def screen_clear():
    try:
        if name == "nt":
            _ = system("cls")      
        elif name == "posix":
            _ = system("clear")  
        else:
            _ = system("clear")
    except:
        how_to_use()


def show_status_ip(host_ip=str,port_ip=int):
    try:
        global status_result
        socket_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status_result = socket_host.connect_ex((host_ip,port_ip))
        socket_host.close()
        return status_result
    except:
        how_to_use()


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
            
            
def user_agent_get():
    try:
        global all_list_agent
        Json_Tar="user_agent_all.json"
        f_op = open(Json_Tar)
        j_op = json.loads(f_op.read())
        all_list_agent = []
        for x_value in j_op["user_agents"]:
            for ix_values in j_op["user_agents"][x_value]:
                for ixl_values in j_op["user_agents"][x_value][ix_values]:
                    for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                        all_list_agent.append(ixlp_values)
    except:
        how_to_use()


def define_url(url_x=str):
    try:
        global Target_URL
        Target_URL = url_x
        return Target_URL
    except:
        how_to_use()


def export_txt_file(file_name=str):
    try:
        global Cleaning_Header
        Target_Header = open(file_name,"r")
        Reading_Header = Target_Header.read()
        Cleaning_Header = Reading_Header.replace("\n",",").split(",")
        Target_Header.close()
        return Cleaning_Header
    except:
        how_to_use()


def get_proxies_for_search():
    print("GET PROX")
    try:
        global proxy_main
        Spo_Url_Site = "https://free-proxy-list.net/"
        S_Spo = BeautifulSoup(requests.get(Spo_Url_Site).content, "html.parser")
        IP_L_L = []
        PR_L_L = []
        i_count_spo = 0
        for tr_all_site in S_Spo.find("table",class_="table table-striped table-bordered"):
            tr_tres = tr_all_site.find_all("tr")
            for x_loop_in in tr_tres:
                tds_td = x_loop_in.find_all("td")
                for x_p_in in tds_td:
                    i_count_spo += 1
                    if i_count_spo == 1:
                        IP_L = x_p_in.text
                        IP_L_L.append(str(IP_L))
                    elif i_count_spo == 2:
                        PR_L = x_p_in.text
                        PR_L_L.append(str(PR_L))
                i_count_spo = 0
        user_agent_get()
        print("GETTING ACCESS")
        try:
            for x_ip, x_pr in zip(IP_L_L,PR_L_L):
                proxy_dict_new = {"http":f"http://{x_ip}"+":"+f"{x_pr}",
                              "https":f"https://{x_ip}"+":"+f"{x_pr}"}
                User_Header_List = {
                        "User-Agent":f"{random.choice(all_list_agent)}"
                        }
                try:
                    print("SEARCHING PROXY")
                    time.sleep(0.5)
                    print(x_ip, x_pr)
                    REQ_URL = requests.get('https://www.google.com/', proxies=proxy_dict_new ,headers=User_Header_List)
                    print(REQ_URL.text)
                    print(REQ_URL.status_code)
                    if REQ_URL.status_code == 200:
                        proxy_main = {"http":proxy_dict_new.get("http"),
                                      "https":proxy_dict_new.get("https")}
                        print("FOUND")
                        break
                    else:
                        pass
                except:
                    pass
                    
        except:
            print("DEFINE ALTERNATIVE")
            Def_IPR_Al = "https://52.183.8.192:3128"
        
        try:
            if "Def_IPR_Al" in globals():
                print(f"Alternative is active: {Def_IPR_Al}")
                proxy_main = {"https":Def_IPR_Al}
                return proxy_main
            else:
                return proxy_main
            print("END PROX")
        except:
            print("PASSING")
            sys.exit()
            pass
    except:
        how_to_use()
        
        
def check_status_code(url_x=str):
    try:
        user_agent_get()
        User_Header = {
                "User-Agent":f"{random.choice(all_list_agent)}"
                }
        Status_Response = requests.get(url_x,headers=User_Header).status_code
        if Status_Response == 200:
            print("\033[1;32m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 404:
            pass
        elif Status_Response == 403:
            print("\033[1;31m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 503:
            print("\033[1;36m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 501:
            print("\033[1;37m%s\x1b[0m -- %s" % (url_x,Status_Response))
        else:
            print("%s -- %s" % (url_x,Status_Response))
    except:
        print("NOT IN POOL: "+url_x)
        pass


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
        

def check_proxies_for_search(url_tar=str):
    print("\n")
    print("SESSION HAS BEEN STARTED")
    time.sleep(1.1)
    print("YOUR SITE: ",url_tar)
    time.sleep(0.8)
    try:
        global proxy_main
        Spo_Url_Site = "https://free-proxy-list.net/"
        S_Spo = BeautifulSoup(requests.get(Spo_Url_Site).content, "html.parser")
        IP_L_L = []
        PR_L_L = []
        i_count_spo = 0
        for tr_all_site in S_Spo.find("table",class_="table table-striped table-bordered"):
            tr_tres = tr_all_site.find_all("tr")
            for x_loop_in in tr_tres:
                tds_td = x_loop_in.find_all("td")
                for x_p_in in tds_td:
                    i_count_spo += 1
                    if i_count_spo == 1:
                        IP_L = x_p_in.text
                        IP_L_L.append(str(IP_L))
                    elif i_count_spo == 2:
                        PR_L = x_p_in.text
                        PR_L_L.append(str(PR_L))
                i_count_spo = 0
        user_agent_get()
        print("GETTING ACCESS")
        time.sleep(0.8)
        try:
            for x_ip, x_pr in zip(IP_L_L,PR_L_L):
                proxy_dict_new = {"http":f"http://{x_ip}"+":"+f"{x_pr}",
                              "https":f"https://{x_ip}"+":"+f"{x_pr}"}
                User_Header_List = {
                        "User-Agent":f"{random.choice(all_list_agent)}"
                        }
                try:
                    print("\n")
                    print("CHECKING PROXY")
                    time.sleep(0.5)
                    print(x_ip, x_pr)
                    if "http://" in url_tar or "https://" in url_tar:
                        new_tar = url_tar.replace("http://","").replace("https://","")
                        x_tar = "https://" + new_tar
                        print(x_tar)
                        REQ_URL = requests.get('https://ipinfo.io/json', proxies=proxy_dict_new ,headers=User_Header_List, timeout=32)
                        Json_Res = json.loads(REQ_URL.text)
                        print(Json_Res["ip"])
                        print(Json_Res["country"])
                        print(Json_Res["org"])
                        print(Json_Res["timezone"])
                        if REQ_URL.status_code == 200:
                            print("PROXY IS ACTIVE")
                            proxy_main = {"http":proxy_dict_new.get("http"),
                                          "https":proxy_dict_new.get("https")}
                            curl_methods_x(x_tar,str(proxy_main['http']))
                        else:
                            time.sleep(0.7)
                            print("PASSING")
                            print("\n")
                            pass
                    else:
                        REQ_URL = requests.get('https://ipinfo.io/json', proxies=proxy_dict_new ,headers=User_Header_List, timeout=32)
                        print("FOUND")
                        print("\n")
                        Json_Res = json.loads(REQ_URL.text)
                        print(Json_Res["ip"])
                        print(Json_Res["country"])
                        print(Json_Res["org"])
                        print(Json_Res["timezone"])
                        print("\n")
                        if REQ_URL.status_code == 200:
                            print("PROXY IS ACTIVE")
                            proxy_main = {"http":proxy_dict_new.get("http"),
                                          "https":proxy_dict_new.get("https")}
                            new_d_h = "https://" + url_tar
                            print(new_d_h)
                            curl_methods_x(new_d_h,str(proxy_main['http']))
                        else:
                            time.sleep(0.7)
                            print("PASSING")
                            print("\n")
                            pass
                except:
                    time.sleep(0.7)
                    print("PASSING")
                    print("\n")
                    pass
        except:
            print("DEFINED ALTERNATIVE")
            Def_IPR_Al = "https://52.183.8.192:3128"
            print("\n")
        try:
            if "Def_IPR_Al" in globals():
                print(f"Alternative is active: {Def_IPR_Al}")
                print("\n")
                proxy_main = {"https":Def_IPR_Al}
                return proxy_main
            else:
                return proxy_main
            print("END PROXY PROCESS")
            print("\n")
        except:
            print("PASSING")
            print("\n")
            pass
    except:
        pass         


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
 
        
def https_proxies_for_search(url_tar=str):
    print("\n")
    print("SESSION HAS BEEN STARTED")
    time.sleep(1.1)
    print("YOUR SITE: ",url_tar)
    time.sleep(0.8)
    try:
        global proxy_main
        Spo_Url_Site = "https://free-proxy-list.net/"
        S_Spo = BeautifulSoup(requests.get(Spo_Url_Site).content, "html.parser")
        IP_L_L = []
        PR_L_L = []
        i_count_spo = 0
        for tr_all_site in S_Spo.find("table",class_="table table-striped table-bordered"):
            tr_tres = tr_all_site.find_all("tr")
            for x_loop_in in tr_tres:
                tds_td = x_loop_in.find_all("td")
                for x_p_in in tds_td:
                    i_count_spo += 1
                    if i_count_spo == 1:
                        IP_L = x_p_in.text
                        IP_L_L.append(str(IP_L))
                    elif i_count_spo == 2:
                        PR_L = x_p_in.text
                        PR_L_L.append(str(PR_L))
                i_count_spo = 0
        user_agent_get()
        print("GETTING ACCESS")
        time.sleep(0.8)
        try:
            for x_ip, x_pr in zip(IP_L_L,PR_L_L):
                proxy_dict_new = {"http":f"http://{x_ip}"+":"+f"{x_pr}",
                              "https":f"https://{x_ip}"+":"+f"{x_pr}"}
                User_Header_List = {
                        "User-Agent":f"{random.choice(all_list_agent)}"
                        }
                try:
                    print("\n")
                    print("CHECKING PROXY")
                    time.sleep(0.5)
                    print(x_ip, x_pr)
                    if "http://" in url_tar or "https://" in url_tar:
                        new_tar = url_tar.replace("http://","").replace("https://","")
                        x_tar = "https://" + new_tar
                        print(x_tar)
                        REQ_URL = requests.get('https://ipinfo.io/json', proxies=proxy_dict_new ,headers=User_Header_List, timeout=32)
                        Json_Res = json.loads(REQ_URL.text)
                        print(Json_Res["ip"])
                        print(Json_Res["country"])
                        print(Json_Res["org"])
                        print(Json_Res["timezone"])
                        if REQ_URL.status_code == 200:
                            print("PROXY IS ACTIVE")
                            proxy_main = {"http":proxy_dict_new.get("http"),
                                          "https":proxy_dict_new.get("https")}
                            https_all_methods_proxy(x_tar,str(proxy_main['http']))
                        else:
                            time.sleep(0.7)
                            print("PASSING")
                            print("\n")
                            pass
                    else:
                        REQ_URL = requests.get('https://ipinfo.io/json', proxies=proxy_dict_new ,headers=User_Header_List, timeout=32)
                        print("FOUND")
                        print("\n")
                        Json_Res = json.loads(REQ_URL.text)
                        print(Json_Res["ip"])
                        print(Json_Res["country"])
                        print(Json_Res["org"])
                        print(Json_Res["timezone"])
                        print("\n")
                        if REQ_URL.status_code == 200:
                            print("PROXY IS ACTIVE")
                            proxy_main = {"http":proxy_dict_new.get("http"),
                                          "https":proxy_dict_new.get("https")}
                            new_d_h = "https://" + url_tar
                            print(new_d_h)
                            https_all_methods_proxy(new_d_h,str(proxy_main['http']))
                        else:
                            time.sleep(0.7)
                            print("PASSING")
                            print("\n")
                            pass
                except:
                    time.sleep(0.7)
                    print("PASSING")
                    print("\n")
                    pass
        except:
            print("DEFINED ALTERNATIVE")
            Def_IPR_Al = "https://52.183.8.192:3128"
            print("\n")
        try:
            if "Def_IPR_Al" in globals():
                print(f"Alternative is active: {Def_IPR_Al}")
                print("\n")
                proxy_main = {"https":Def_IPR_Al}
                return proxy_main
            else:
                return proxy_main
            print("END PROXY PROCESS")
            print("\n")
        except:
            print("PASSING")
            print("\n")
            pass
    except:
        pass

        
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

            
    
def main_process():
    Option_Run = optparse(add_help_option=False,epilog="DIR BRUTE FORCE")
    Option_Run.add_option("-d",
                          "--bfdir",
                          help="Search for common directories",
                          dest="bfdir_x",type="string")
    Option_Run.add_option("-h",
                          "--help",
                          help="Help",
                          dest="help_x",action="store_true")
    Option_Run.add_option("-a",
                          "--bfdetail",
                          help="Search for all of directories",
                          dest="bfdetail_x",type="string")
    Option_Run.add_option("-v",
                          "--bfvul",
                          help="Search for all of site directories vulnerabilities",
                          dest="bfvul_x",type="string")
    Option_Run.add_option("-f",
                          "--bffile",
                          help="Search for file directories",
                          dest="bffile_x",type="string")
    Option_Run.add_option("-s",
                          "--bfsub",
                          help="Search for subdomains",
                          dest="bfsub_x",type="string")
    Option_Run.add_option("-p",
                          "--portcheck",
                          help="Check for common port - open or close",
                          dest="portcheck_x",type="string")
    Option_Run.add_option("-c",
                          "--censorshipcheck",
                          help="Check censorship",
                          dest="censor_x",type="string")
    op_run,op_args = Option_Run.parse_args()
    try:
        if op_run.help_x:
            how_to_use()
        elif op_run.bfdir_x:
            site_target = str(op_run.bfdir_x).replace(" ","")
            run_process(site_target,"common.txt")
        elif op_run.bfdetail_x:
            site_target = str(op_run.bfdetail_x).replace(" ","")
            run_process(site_target,"dir_all.txt")
        elif op_run.bfvul_x:
            site_target = str(op_run.bfvul_x).replace(" ","")
            run_process(site_target,"vuln.txt")
        elif op_run.portcheck_x:
            site_target = str(op_run.portcheck_x).replace(" ","")
            checking_port(site_target)
        elif op_run.bffile_x:
            site_target = str(op_run.bffile_x).replace(" ","")
            doc_target = str(op_args[0]).replace(" ","")
            search_file(site_target,doc_target)
        elif op_run.bfsub_x:
            site_target = str(op_run.bfsub_x).replace(" ","")
        elif op_run.censor_x:
            site_target = str(op_run.censor_x).replace(" ","")
            time.sleep(0.8)
            cen_notice()
            time.sleep(1.5)
            ans_user = str(input("SELECT YOUR PROCESS: ")).upper().replace(" ","")
            if ans_user == "1":
                http_all_methods_no_proxy(site_target)
            elif ans_user == "2":
                check_proxies_for_search(site_target)
            elif ans_user == "3":
                https_proxies_for_search(site_target)
            elif ans_user == "/":
                time.sleep(0.8)
                screen_clear()
                how_to_use()
                pass
            else:
                print("\n")
                print("OUT OF THE SELECTION RANGE OR UNDEFINED INPUT")
                pass
        else:
            pass
    except:
        how_to_use()


if __name__ == "__main__":
    try:
        if len(sys.argv) >= 1:
            time.sleep(1.2)
            main_process()
        elif len(sys.argv) == 0:
            time.sleep(1.2)
            how_to_use()
        else:
            time.sleep(1.2)
            how_to_use()
    except:
        time.sleep(1.2)
        how_to_use()
        sys.exit()
