import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = [pd.DataFrame()] * 8
fileName = 'raw_data_'

for i in [1, 3] :
    df[i] = pd.read_csv(fileName + str(i) + '.csv')
    df[i] = df[i].astype(float)

def statics(dataFrame, column) :
    temp = dataFrame[column].value_counts().sort_index()
    temp = temp.to_frame()
    return temp

def calcNan(i, dataFrame, column) :
    index_sum = dataFrame.sum().loc[column]
    if len(df[i].index) != index_sum :
        nan=pd.DataFrame([len(df[i].index) - index_sum], index = ["nan"], columns = [column])
        dataFrame=pd.concat([nan, dataFrame], axis=0)
    return dataFrame
    
def makeFigPie(i, dataFrame, column) :
    plt.clf()
    plt.figure(figsize = (18, 7))
    plt.pie(dataFrame[column], startangle = 90, counterclock = False, autopct = "%.2f%%", labels = dataFrame.index)
    title = "static_data_" + str(i) + "_" + column
    plt.title(title)
    plt.subplots_adjust(left = 0.05, right = 0.95, bottom=0.05, top=0.95)
    plt.savefig(title + ".png")
    plt.close()
    
def makeFigLine(i, dataFrame, column) : 
    plt.clf()
    plt.figure(figsize = (18, 7))
    plt.plot(dataFrame, 'ko-')
    title = "static_data_" + str(i) + "_" + column
    plt.title(title)
    plt.subplots_adjust(left = 0.03, right = 0.99, bottom = 0.05, top = 0.95, wspace = 0.1)
    plt.savefig(title + ".png")
    plt.close()

for i in [1, 3] :
    df_final = pd.DataFrame()
    
    # Q1 (PIE)
    
    df_temp = pd.concat([df[i]["Q1A1"], df[i]["Q1A2"]], axis = 1)
    df_sum = df_temp.sum(axis=1).to_frame()
    df_sum.columns = ["Q1"]
    for j in range(len(df_sum.index)) :
        if df_sum.iloc[j]["Q1"] == 4 : df_sum.iloc[j]["Q1"] = 0
        else : df_sum.iloc[j]["Q1"] = 1
    
    df_sum = statics(df_sum, "Q1")
    df_sum = calcNan(i, df_sum, "Q1")
    
    makeFigPie(i, df_sum, "Q1")
    
    # Q2 (PIE)
    
    df_temp = pd.concat([df[i]["Q2A11"], df[i]["Q2A12"], df[i]["Q2A13"], df[i]["Q2A2"], df[i]["Q2A3"]], axis = 1)
    df_temp.fillna(0)
    df_sum = df_temp.sum(axis = 1).to_frame()
    df_sum.columns = ["Q2"]
    for j in range(len(df_sum.index)) :
        if df_sum.iloc[j]["Q2"] != 0 : df_sum.iloc[j]["Q2"] = 1
    
    df_sum = statics(df_sum, "Q2")
    df_sum = calcNan(i, df_sum, "Q2")
    
    makeFigPie(i, df_sum, "Q2")
    
    # Q4 (LINE)
    
    df_temp = pd.DataFrame()
    for j in range(1, 8) :
        df_temp = pd.concat([df_temp, df[i]["Q4A"+str(j)]], axis = 1)
        
    df_sum = df_temp.sum(axis = 1).to_frame()
    df_sum.columns = ["Q4"]
    for j in range(len(df_sum.index)) :
        df_sum.iloc[j]["Q4"] = round(df_sum.iloc[j]["Q4"] / 7, 2)
        
    df_sum=statics(df_sum, "Q4")            
    df_sum=calcNan(i, df_sum, "Q4")
    
    makeFigLine(i, df_sum, "Q4")
    
    # Q5 (LINE)
    
    df_temp=pd.DataFrame()
    for j in range(1, 8) :
        df_temp = pd.concat([df_temp, df[i]["Q5A"+str(j)]], axis = 1)
        
    df_sum = df_temp.sum(axis = 1).to_frame()
    df_sum.columns = ["Q5"]
    for j in range(len(df_sum.index)) :
        df_sum.iloc[j]["Q5"] = round(df_sum.iloc[j]["Q5"] / 7, 2)
        
    df_sum = statics(df_sum, "Q5")
    df_sum = calcNan(i, df_sum, "Q5")
    
    makeFigLine(i, df_sum, "Q5")
    
    # Q15A1 ~ Q15A6 (PIE, each)
    
    for j in range(1, 7) :
        columnName = "Q15A" + str(j)
        df_sum = statics(df[i][columnName].to_frame(), columnName)
        df_sum = calcNan(i, df_sum, columnName)
        
        makeFigPie(i, df_sum, columnName)
    
    # Q28&Q29 (LINE)
    
    df_temp = pd.DataFrame()
    for j in range(1, 13) :
        df_temp=pd.concat([df_temp, df[i]["Q28A"+str(j).zfill(2)]], axis = 1)
    for j in range(1, 8) :
        df_temp = pd.concat([df_temp, df[i]["Q29A"+str(j)]], axis = 1)
    
    df_sum = df_temp.sum(axis = 1).to_frame()
    df_sum.columns = ["Q28&Q29"]
    for j in range(len(df_sum.index)) :
        df_sum.iloc[j]["Q28&Q29"] = round(df_sum.iloc[j]["Q28&Q29"] / 19, 2)
    
    df_sum = statics(df_sum, "Q28&Q29")
    df_sum = calcNan(i, df_sum, "Q28&Q29")
    
    makeFigLine(i, df_sum, "Q28&Q29")