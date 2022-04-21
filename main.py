import pandas as pd
files_path = '/Users/kentsao/Downloads/download/'
df_a = pd.read_csv(files_path + 'a_lvr_land_a.csv')
df_b = pd.read_csv(files_path + 'b_lvr_land_a.csv')
df_e = pd.read_csv(files_path + 'e_lvr_land_a.csv')
df_f = pd.read_csv(files_path + 'f_lvr_land_a.csv')
df_h = pd.read_csv(files_path + 'h_lvr_land_a.csv')
df_all = pd.concat([df_a,df_b,df_e,df_f,df_h],axis=0, ignore_index=True)
#filter_a
options = ['一層','二層','三層','四層','五層','六層','七層','八層','九層','十層','十一層','十二層']
filter_a = df_all.loc[df_all['主要用途'] == '住家用']
filter_a = filter_a.loc[filter_a['建物型態'] == '住宅大樓(11層含以上有電梯)']
filter_a = filter_a.loc[~filter_a['總樓層數'].isin(options)]
filter_a.to_csv(files_path + 'filter_a.csv')
#filter_b
def count_lots(parking_lots):
    lots = 0
    for item in parking_lots:
        flag = 0
        num = ""
        for ch in item:
            if ch == '位':
                flag = 1
                continue
            if flag == 1:
                num += ch
        if(num == ""):
            continue
        lots += int(num)
    return lots

def count_average_price(prices):
    total_price = 0
    for item in prices:
        if item[0] == 't':
            continue
        else:
            total_price += int(item)
    return total_price/len(prices)


table = {
    "總件數": 0,
    "總車位數": 0,
    "平均總價元": 0,
    "平均車位總價元": 0
}
filter_b = pd.DataFrame(table, index=[0])
filter_b["總件數"] = len(df_all)
filter_b["總車位數"] = count_lots(df_all["交易筆棟數"])
filter_b["平均總價元"] = count_average_price(df_all["總價元"])
filter_b["平均車位總價元"] = count_average_price(df_all["車位總價元"])
filter_b.index = ['df_all']
filter_b.to_csv(files_path + 'filter_b.csv')
