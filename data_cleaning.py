import csv
import requests
import pandas as pd
def data_parser():
    df = pd.read_csv("wages2.csv", index_col=0)
    ##display(df.iloc[:,0].head(10))
    selected_countries = df[df.index.isin(['Australia',"Canada","Finland","France","Germany","New Zealand","Norway",
                                           "Poland","United Kingdom","United States"])]
    df2 = selected_countries.iloc[:,13:]
    df2.columns = range(1970, 2023)
    df2 = df2.fillna(0)
    df3 = df2.iloc[:,30:]
    df2.loc['United Kingdom', 2019] = 47937.000000
    df2.loc['United Kingdom', 2020] = 47147.000000
    df2 = df2.drop(labels=2021, axis=1)
    df2 = df2.drop(labels=2022, axis=1)
    vals = [55206, 55342, 53745, 46230, 45581, 47147, 55780, 45269, 32527, 69392]
    vals2 = df2[2020]
    vals3 = []
    for i in range(10):
        vals3.append((vals[i] + vals2[i]) / 2)
    df2['Average 2020'] = vals3
    df3 = df3.drop(labels=2021, axis=1)
    df3 = df3.drop(labels=2022, axis=1)
    vals = [55206, 55342, 53745, 46230, 45581, 47147, 55780, 45269, 32527, 69392]
    vals2 = df3[2020]
    vals3 = []
    for i in range(10):
        vals3.append((vals[i] + vals2[i]) / 2)
    df3['Average 2020'] = vals3
    #display(df2.loc['United Kingdom', 2020])
    #display(df3) #2000
    df2 = df2.round()
    df2.to_csv("cleaneddownloaded.csv",index=True)
    print(df2) #1970
    #print(selected_countries)

    # Sources:
    # : https://data.worldbank.org/indicator/NY.ADJ.NNTY.PC.CD





############ Function Call ############
data_parser()





from bs4 import BeautifulSoup
import requests
import pandas as pd
from pprint import pprint
def web_parser1():
    countries_name_list = ["Australia","Canada","Finland","France","Germany","New Zealand",
                          "Norway","Poland","United Kingdom","United States"]
    alist = []
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_average_wage'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    taglist = soup.find_all("tr")[1:36]
    for row in taglist:
        country_name = row.find_all('td')
        blist = []
        for word in country_name:
            text = word.text.replace('*', '').replace(',', '').strip()
            blist.append(text)
        alist.append(blist)
    df = pd.DataFrame(alist)
    df.set_index(0, inplace=True)
    df = df.loc[countries_name_list]
    new_columns = [2000, 2005] + list(range(2010, 2021))
    df.set_axis(new_columns, axis=1, inplace=True)
    df['Avg. Wage'] = df.iloc[:,:].astype("int").mean(axis=1).round()
    df['Wage Increase'] = df.iloc[:,-2].astype("float") - df.iloc[:,0].astype("float")
    df.to_csv("cleanedwebscrape.csv",index=True)
    print (df)

    # Sources:
    # https://en.wikipedia.org/wiki/List_of_countries_by_average_wage






############ Function Call ############
web_parser1()







import requests
import pandas as pd
from pprint import pprint
def web_parser2():
    countries_name_list = ["Australia","Canada","Finland","France","Germany","New Zealand",
                          "Norway","Poland","United Kingdom","United States"]
    df = pd.read_json("https://echarts.apache.org/examples/data/asset/data/life-expectancy-table.json")
    df.columns = df.iloc[0]
    df = df[1:]
    del df['Population']
    df = df[df["Year"] >= 2000]
    df = df.set_index('Country')
    df = df.loc[countries_name_list]
    year_life_exp = df.groupby('Year')['Life Expectancy'].mean()
    year_inc = df.groupby('Year')['Income'].mean()
    df.to_csv("cleanedjson.csv",index=True)
    print (year_life_exp)
    print(year_inc)
    print (df)

    # Sources:
    # https://echarts.apache.org/examples/data/asset/data/life-expectancy-table.json





############ Function Call ############
web_parser2()





