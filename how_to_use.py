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
