import streamlit as st
import processing
import pandas as pd
import helper
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("Whatsapp Chat Analyzer")

upload_file=st.sidebar.file_uploader("Choose a file")

if upload_file is not None:
    bytes_data = upload_file.getvalue()
    data = bytes_data.decode("utf-8")
    #st.text(data)
    df=processing.processing(data)
    st.dataframe(df)
    
    user_list=df["User"].unique().tolist()
    user_list.remove("Notification")
    
    user_list.sort()
    user_list.insert(0,"Overall")
    
    select_user=st.sidebar.selectbox("Show Analysis wrt", user_list)
    
    if st.sidebar.button("Show Analysis"):
        
        num_messages, words, media, link =helper.fetch_stats(select_user,df)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media")
            st.title(media)
        with col4:
            st.header("Total Links")
            st.title(link)
        
        #Activity Map
        col1, col2 = st.columns(2)

        # Get the weekly data and monthly data
        weekly, monthly = helper.get_busy_activity(select_user, df)

        # Display the "Most Busy Day" in the first column
        with col1:
            st.header("Most Busy Day")
            fig, ax = plt.subplots()  # Adjust the figure size if needed
            ax.bar(weekly.index, weekly.values, color="#3C0753")
            ax.set_xticklabels(weekly.index, rotation="vertical")  # Rotate the x-axis labels to make them readable
            col1.pyplot(fig)
            
        with col2:
            st.header("Most Busy Month")
            fig, ax = plt.subplots()  # Adjust the figure size if needed
            ax.bar(monthly.index, monthly.values, color="#910A67")
            ax.set_xticklabels(monthly.index, rotation="vertical")  # Rotate the x-axis labels to make them readable
            col2.pyplot(fig)
            
            
        
        #Busy User
        if select_user=="Overall":
            st.title("Busy Users")
            col1, col2 =st.columns(2)
            X,new_df=helper.fetch_busy_user(df)
            with col1:
                fig,ax=plt.subplots()
                ax.bar(X.index , X.values,color="#FF6500")
                ax.set_xticklabels(X.index, rotation="vertical")
                col1.pyplot(fig)
            with col2:
                col2.dataframe(new_df)
            
            
        #WordCloud
        st.title("WordCloud")
        df_wc=helper.create_wordcloud(select_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
        
        #Most Common Words
        st.title("Most Common Words")
        word_count_df=helper.word_frequency(select_user,df)
        fig, ax = plt.subplots()
        ax.barh(word_count_df["Words"],word_count_df["count"],color="#005B41")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        
        #Emoji Analysis
        st.title("Most Common Emoji")
        col1, col2 = st.columns(2)
        emoji_df=helper.emoji_analysis(select_user,df)
        with col1:
            col1.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df["count"].head(),labels=emoji_df["Emoji"].head(), autopct="%0.2f%%")
            #ax.set_xticklabels(X.index, rotation="vertical")
            col2.pyplot(fig)
            
        #Timeline
        st.title("Monthly Timeline")
        X=helper.get_timeline(select_user,df)
        fig, ax =plt.subplots()
        ax.plot(X["Time"],X["Messages"],color="#5C5470")
        ax.set_xticklabels(X["Time"],rotation="vertical")
        st.pyplot(fig)
        
        #Most Enaging Time
        st.title("Most Engaging Time-Period")
        heatmap_data=helper.get_most_engaging_period(select_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(heatmap_data)
        st.pyplot(fig)