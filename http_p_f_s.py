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
