# Flask + PostgreSQL GUI App 🚀  
### From Static HTML to Live Deployed Full-Stack Website

This project demonstrates how to transform a simple **static Flask “Hello World” template** into a **live full-stack web application** backed by a live **PostgreSQL database** and deployed online.

<img width="600" alt="screenshot of complete application" src="https://github.com/user-attachments/assets/3eaba3a4-5e48-41d6-a1d0-7c4c3d1045ab">

## 📺 Full Tutorial

Watch the step-by-step video walkthrough here:  
<a href="" target="_blank"><img width="600" alt="Build PostgreSQL GUI App thumbnail" src="https://github.com/user-attachments/assets/353344d4-65d3-443c-bea3-7932eb6e3489" /></a>
<br>
<br>
By the end of this video, you will have:
- A dynamic Flask web interface.
- A live PostgreSQL database, hosted on Sevalla.  
- User profiles pulled from SQL.
- A fully deployed public website (hosted on Sevalla as well).

## 🎁 What's Inside?

### Starter Files
The starter_files folder contains:
- Static Flask template  
- Basic HTML/CSS layout  
- CSV profile data  
- Image assets

### Complete App
a production-ready instanace of the app - ready to deploy on Sevalla.

## 🧠 What You’ll Learn

- How Flask web apps actually work (frontend + backend)  
- Creating and structuring a PostgreSQL database  
- Importing CSV data into SQL tables  
- Primary Keys, NOT NULL, VARCHAR & constraints explained simply  
- Connecting Python to PostgreSQL using `psycopg`  
- Turning static HTML into dynamic database-driven pages  
- Creating dynamic user routes (`/user/username`)  
- Navigation bars with database loops  
- Environment variables & protecting secrets  
- Deploying a full website with GitHub integration  
- Reading deployment logs & fixing real errors  

## 📁 Project Structure

```
Flask_PostgreSQL_GUIAPP/
│
├── starter_files/   → Minimal Flask template to begin with
├── complete_app/    → Final working full-stack application
├── README.md
└── LICENSE
```

---

## ⚙️ Environment Setup

```bash
conda create -n social_env python=3.12 flask
conda activate social_env
pip install psycopg
```

Run the app locally:

```bash
python app.py
```

Navigate to:

```
http://127.0.0.1:5000
```

## 🗄️ Example SQL Table Creation

```sql
CREATE TABLE user_profiles(
  username VARCHAR(20) PRIMARY KEY,
  full_name TEXT NOT NULL,
  photo_path TEXT,
  bio TEXT,
  country TEXT,
  date_of_birth DATE NOT NULL
);
```

## 🔌 Example Database Connection (Python)

```python
import psycopg

with psycopg.connect(DB_URL) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_profiles;")
    results = cursor.fetchall()
```

## 🚀 Deployment Overview

1. Modify my project and customize it to your needs.
2. Push complete project to your GitHub.
3. Create PostgreSQL database on Sevalla. 
4. Set environment variable DATABASE_URL. 
5. Create application in Sevalla dashboard.  
6. Connect internal database service.  
7. Add start command:

```bash
python app.py
```

7. Deploy 🎉   

## 📜 License

MIT License — free to use, modify, and share.

## ⭐ Support

If this project helped you, consider giving it a star on GitHub — it helps others find beginner-friendly resources like this one!

