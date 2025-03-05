import pandas as pd 
file_path =r"C:\Users\dhawa\Desktop\mEng Project\virtual_bidding\RT_COMMITMENT_ZONAL\OASIS_Real_Time_Commitment_Zonal_LBMP.csv"
rtc = pd.read_csv(file_path)
file_path = r"C:\Users\dhawa\Desktop\mEng Project\virtual_bidding\RT_LBMP\20240301rtlbmp_zone_csv\20240301rtlbmp_zone.csv"
rtlbmp = pd.read_csv(file_path)
file_path = r"C:\Users\dhawa\Desktop\mEng Project\virtual_bidding\DA_LBMP\20250301damlbmp_zone_csv\20250301damlbmp_zone.csv"
dalbmp = pd.read_csv(file_path)



