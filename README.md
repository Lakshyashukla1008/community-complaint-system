# 🚀 Yuva Shakti Sangathan

A **community-driven web platform** built using Streamlit where citizens can raise complaints, contribute funds, and help improve society.

---

## 🌟 Features

### 🔐 Authentication System

* User Signup & Login
* Secure password hashing using bcrypt
* Session management using Streamlit

---

### 📝 Complaint System

Users can report various types of issues:

* 💡 Light Problems
* 🛣 Road Issues
* 🚗 Parking Problems
* 🐕 Street Dog Issues
* 🚰 Sewer Overflow
* 👤 Personal Complaints

📌 Each complaint includes:

* Name, Email
* Complaint Type
* Address
* Status (Pending / Resolved)
* Timestamp

---

### 💰 Contribution System

* Users can contribute money to support community initiatives
* Payment methods: UPI / Card
* Email confirmation sent to:

  * User 📧
  * Admin 📧

---

### 📢 Announcement System

* Admin can post announcements
* Users can view latest updates

---

### 🧑‍💼 Admin Panel

* View all complaints, contributions, feedback
* Filter complaints (Pending / Resolved)
* Update complaint status
* Send resolution email automatically

---

### 📊 Dashboard

* Total complaints
* Pending vs Resolved
* Total contributions ₹
* 📈 Charts:

  * Pie chart (Complaint Status)
  * Bar chart (Complaint Types)

---

### ✉️ Email Integration

* Automatic emails for:

  * Contribution confirmation
  * Complaint resolution

---

### ⚙️ Tech Stack

* 🐍 Python (Streamlit)
* 🍃 MongoDB (Database)
* 🔐 bcrypt (Password hashing)
* 📊 matplotlib / pandas (Charts & data)
* 📧 SMTP (Email service)

---

## 📂 Project Structure (Overview)

```bash
community-complaint-system/
│
├── Home.py
├── pages/
│   ├── complaint.py
│   ├── contribution.py
│   ├── complaint_status.py
│   ├── dashboard.py
│   ├── announcements.py
│   ├── admin.py
│
├── database/
│   └── database.py
│
├── services/
│   ├── mail.py
│   └── auth_helper.py
│
├── auth/
│   └── auth.py
│
├── requirements.txt
└── README.md
```

---

## 🔒 Security Features

* Password hashing using bcrypt
* Session-based authentication
* Admin access control
* User data privacy maintained

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/community-complaint-system.git
cd community-complaint-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Secrets

Create a file:

```
.streamlit/secrets.toml
```

Add your credentials:

```toml
MONGO_URI = "your_mongodb_connection_string"
ADMIN_PASSWORD = "your_admin_password"

EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```

---

### 5️⃣ Run the App

```bash
streamlit run Home.py
```

---

## 🌐 Deployment

* Deployed using **Streamlit Cloud**
* Connected with GitHub repository
* Uses secrets for secure credentials

---

## 🎯 Future Improvements

* AI-based complaint suggestions 🤖
* Real payment gateway integration 💳
* Mobile responsive UI 📱
* Advanced analytics dashboard 📊

---

## ❤️ Acknowledgement

Developed as a college project to solve real-world community problems and empower youth participation.

---

## 👨‍💻 Author

**Yuva Shakti Sangathan Team**
