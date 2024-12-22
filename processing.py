import re
import pandas as pd

isTime12Format=False

def processing(data):
    if re.search(r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s',data):
    #pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s'
        isTime12Format=True
        pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s'
    else:
        pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
        
    messages = re.split(pattern, data.strip())[1:]
    dates = re.findall(pattern,data)
    cleaned_dates = [date.replace('\u202f', ' ').strip(' - ') for date in dates]
    df=pd.DataFrame({'Messages':messages,"Date":cleaned_dates})
    if isTime12Format:
        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%y, %I:%M %p")
    else:
        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y, %H:%M")
    
    df["Messages"]=df["Messages"].apply(lambda x:x.replace("\n",""))

    name_pattern = r'^([^:]+):'
    users=[]
    messages=[]
    for msg in df["Messages"]:
        entry=re.split(r'^([^:]+):',msg)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append("Notification")
            messages.append(entry[0])

    df["User"]=users
    df["Messages"]=messages
    df["Year"]=df["Date"].dt.year
    df["Month"]=df["Date"].dt.month_name()
    df["Hour"]=df["Date"].dt.hour
    df["Minute"]=df["Date"].dt.minute
    df["Day"]=df["Date"].dt.day
    df["Day_Names"]=df["Date"].dt.day_name()
    #df.drop("Date",axis=1,inplace=True)
    
    return df