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
