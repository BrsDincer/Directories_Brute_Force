def define_url(url_x=str):
    try:
        global Target_URL
        Target_URL = url_x
        return Target_URL
    except:
        how_to_use()
