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
