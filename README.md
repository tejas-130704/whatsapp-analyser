# ChatMate: WhatsApp Chat Analyzer 📊

**ChatMate** is a powerful web application built with **Streamlit** that provides insightful analysis of your WhatsApp chats. Whether it's a personal or group conversation, ChatScope generates comprehensive reports and visualizations to help you uncover trends and patterns from your chat history.

---

## 🌟 Features

- **Overall Analysis**:
  - Total Messages
  - Total Words
  - Total Media Shared
  - Total Links Shared
- **Insights**:
  - Most Active Days of the Week
  - Most Active Months
  - Most Common Words
  - Most Common Emojis
- **Visualizations**:
  - Word Cloud
  - Heatmaps for Engagement
  - Monthly Timeline
  - Most Engaging Time-Periods
- **Custom Reports**: Target individual or group chats for personalized insights.

---

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Framework for building interactive web applications
- **Libraries**:
  - **Pandas**: For data manipulation
  - **Matplotlib & Seaborn**: For creating beautiful visualizations
  - **WordCloud**: To generate word clouds
  - **Emoji**: For analyzing emoji usage

---

## 🚀 How to Install and Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ChatScope.git
   cd ChatScope
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Web App**: Open the link displayed in your terminal to use ChatScope.

---

## 📋 Usage Instructions

1. Export the WhatsApp chat as a `.txt` file from your phone.
2. Upload the file using the **"Upload Chat File"** option in the app.
3. Click **"Show Analysis"** to view insights and visualizations.
4. Explore overall analysis or dive into individual reports.

---

## 🖼️ Screenshots
![Screenshot 2024-12-22 202917](https://github.com/user-attachments/assets/1f4bad07-ca7b-49f3-a958-b3dc3ca64eea)

<hr>

![Screenshot 2024-12-22 202808](https://github.com/user-attachments/assets/220794ee-562a-4cd8-9c79-124e4d2eb4c2)

<hr>

![Screenshot 2024-12-22 202832](https://github.com/user-attachments/assets/ac3fe37f-02b9-49c2-b818-952d95cf630e)

<hr>

![Screenshot 2024-12-22 202847](https://github.com/user-attachments/assets/468b0598-a091-4aba-b8f4-72c9f80dd0b1)

<hr>

![Screenshot 2024-12-22 202859](https://github.com/user-attachments/assets/c4647c13-d2d2-4c47-b4a6-7ea0bf2f809d)

<hr>

---

## 🤝 Contributors

- Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## 🌟 Future Enhancements

- Support for additional messaging platforms.
- Sentiment analysis for conversations.
- Integration with cloud storage for easier file uploads.
