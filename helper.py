from urlextract import URLExtract 
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji

exractor = URLExtract()

def fetch_stats(user_selected,df):
    
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
    
    #fetching total Messages
    num_messages=df.shape[0]
    
    #fetching total words
    words=[]
    links=[]
    for message in df["Messages"]:
        links.extend(exractor.find_urls(message))
        words.extend(message.split())

    #fetching total medias
    num_media=df[df["Messages"]==" <Media omitted>"].shape[0]
   
    return num_messages,len(words),num_media,len(links)


def fetch_busy_user(df):
    user_list= df["User"].value_counts().head()
    new_df=round((df["User"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"count":"Percent"})
    return user_list,new_df

def create_wordcloud(user_selected,df):
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color="white")
    
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
    
    temp = df[df["User"]!="Notification"]
    temp = temp[temp["Messages"]!=" <Media omitted>"]
    
    df_wc=wc.generate(temp["Messages"].str.cat(sep=" "))
    return df_wc
    
    
    
def word_frequency(user_selected,df):
    chars_to_remove = r'[",\*\^\[\]\{\}\-=+/.]'
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
        
    temp = df[df["User"]!="Notification"]
    temp = temp[temp["Messages"]!=" <Media omitted>"]
    temp["Messages"] = temp["Messages"].str.replace("<This message was edited>", "", regex=False)
    temp=temp[temp["Messages"]!=" This message was deleted"]
    temp=temp[temp["Messages"]!=" You deleted this message"]
    # Removing the characters from the "Messages" column
    temp["Messages"] = temp["Messages"].str.replace(chars_to_remove, "", regex=True)
    f= open('stop_hinglish.txt','r')
    stop_words=f.read()
    words=[]
    for message in temp["Messages"]:
        for word in message.split():
            if word.lower() not in stop_words.lower():
                words.append(word)
    
    return pd.DataFrame(Counter(words).most_common(20),columns=["Words","count"])


def emoji_analysis(user_selected,df):
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
        
    emojis=[]
    
    for message in df["Messages"]:
        emojis.extend([c for c in message if emoji.is_emoji(c)])
        
    emoji_df=pd.DataFrame(Counter(emojis).items(),columns=["Emoji","count"])
    emoji_df.sort_values(by='count', ascending=False).reset_index(drop=True)
    
    return emoji_df

def get_timeline(user_selected,df):
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
    
    df["Month_Num"]=df['Date'].dt.month
    timeline_df=df.groupby(["Year","Month_Num","Month"]).count()["Messages"].reset_index()
    timeline_df["Time"] = timeline_df["Month"].astype(str) + "-" + timeline_df["Year"].astype(str)    
    return timeline_df

def get_busy_activity(user_selected,df):
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
        
    weekly_score=df["Day_Names"].value_counts()
    monthly_score=df["Month"].value_counts()
    print(weekly_score)
    print(monthly_score)
    
    return weekly_score,monthly_score
    
def get_most_engaging_period(user_selected,df):
    if user_selected!="Overall":
        df=df[df["User"]== user_selected]
        
    df["Period"]=df["Hour"].astype("str")+"-"+(df["Hour"]+1).astype("str")
    df["Period"] = df["Period"].replace("23-24", "23-0", regex=False)
    
    heatmap_data = df.pivot_table(index="Day_Names",columns="Period",values="Messages",aggfunc="count").fillna(0)
    
    return heatmap_data