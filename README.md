# Medicine Tracker Application

## 📌 Overview
The **Medicine Tracker** application is a Python-based tool that helps users manage their medicine schedules by tracking expiration dates and refill reminders. It provides notifications via **desktop alerts, email, and voice announcements**.

## 🚀 Features
- ✅ **Track Medicine Expiry Dates** – Notifies you **2 days before** a medicine expires.
- ✅ **Medicine Refill Reminder** – Alerts you **2 days before** a medicine runs out.
- ✅ **Desktop Notifications** – Uses system alerts to notify users.
- ✅ **Email Alerts** – Sends reminder emails using Gmail.
- ✅ **Voice Notifications** – Uses text-to-speech for audible reminders.

## 🛠️ Tech Stack
- **Python** – Core development language.
- **SQLite** – Database for storing medicine data.
- **Plyer** – For system notifications.
- **pyttsx3** – For voice alerts.
- **yagmail** – For sending email reminders.
- **tkinter** – (Optional) If a GUI is added later.

## 📂 Project Structure
```
Medapp/
│── app.py           # Main application (if using GUI)
│── notifier.py      # Notification system
│── medicines.db     # SQLite database
│── .env             # Secure credentials file (DO NOT SHARE!)
│── requirements.txt # List of dependencies
│── README.md        # Project documentation
```

## 🔧 Setup and Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/Medapp.git
cd Medapp
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Create a `.env` file in the project directory and add:
```
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_generated_app_password
RECIPIENT_EMAIL=recipient_email@gmail.com
```
💡 **Note:** Generate an [App Password](https://myaccount.google.com/apppasswords) for Gmail authentication.

### 4️⃣ Run the Application
```sh
python notifier.py
```

## 📩 How It Works
1. The application fetches medicine details from the **SQLite database**.
2. It calculates days remaining for expiry and refill dates.
3. If a medicine is **2 days from expiry or running out**, it sends:
   - 🔔 **Desktop notification**
   - 📧 **Email alert**
   - 🔊 **Voice reminder**

## 📝 To-Do List
- [ ] Improve UI design with **Tkinter**.
- [ ] Add **SMS notifications** using Twilio.
- [ ] Implement a **cloud-based database** (PostgreSQL, Firebase).

## 🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss your proposed changes.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
Developed by **Aditya Nanaware** 🚀

---
⭐ **If you like this project, give it a star on GitHub!** ⭐

