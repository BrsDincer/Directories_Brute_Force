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
