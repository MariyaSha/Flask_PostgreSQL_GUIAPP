# Flask + PostgreSQL GUI App 🚀  
From Static HTML to Live Deployed Full-Stack Website

## 📺 Video Tutorial

This repository was created to support the following YouTube tutorial - watch the step-by-step video walkthrough here: 
<br>
<a href="" target="_blank"><img width="600" alt="Build PostgreSQL GUI App thumbnail" src="https://github.com/user-attachments/assets/353344d4-65d3-443c-bea3-7932eb6e3489" /></a>

## 🔎 Overview 

This project demonstrates how to transform a simple **static Flask “Hello World” template** into a **live full-stack web application** backed by a live **PostgreSQL database** and deployed online.

### Screenshots

<img alt="screenshot of complete application" src="https://github.com/user-attachments/assets/9a2c5e9e-0f6d-48b0-a655-f91438079a6f">

## 🎁 What's Inside?

### Starter Files
The starter_files folder contains:
- Static Flask template.  
- Basic HTML/CSS layout.
- Image assets.
- CSV profile data to be inserted into the Database.

### Complete App
The complete_app folder contains a production-ready instanace of the app - ready to deploy on Sevalla.
<br>
<b>🚨 Please note: 🚨</b> You'll need to host a live Database following the instructions below in order to make it work! Watch the full tutorial on YouTube for visual steb by step instructions.

## 📁 Project Structure

```
Flask_PostgreSQL_GUIAPP/
│
├── starter_files/   → Minimal Flask template to begin with
├── complete_app/    → Final working full-stack application
├── README.md
└── LICENSE
```

## 🏃 Run Complete App Locally (Minimal Solution)

If you don't have time to watch my step by step 20-min tutorial, here's a minimal soltuion to run the complete application on your system.
<br>
<br>
<b>🚨 Please note: 🚨</b> the full application is designed to run online with a live database, and be publically accessible. 
For this, you'll need to host the database and the app itself. This minimal solution only hosts the database, while running your app locally - which is not a traditional solution. Only use it if you're extra impatient! 😅

### Clone Repo 💻 

Using WSL:

```bash
git clone https://github.com/MariyaSha/Flask_PostgreSQL_GUIAPP.git
cd Flask_PostgreSQL_GUIAPP
cd complete_app
```

If you're not sure how to install WSL & Miniforge, watch <a href="https://youtu.be/luM5kwH6tjQ">this tutorial</a> of mine.

### Environment Setup ⚙️ 

Using Miniforge:

```bash
conda create -n social_env python=3.12 flask
conda activate social_env
pip install psycopg
```

If you're not sure how to install WSL & Miniforge, watch <a href="https://youtu.be/luM5kwH6tjQ">this tutorial</a> of mine.

### Create Live Database on Sevalla 📊

1. Navigate to a database hosting platform named <a href="https://sevalla.com/?utm_source=pythonsimplified&utm_medium=Referral&utm_campaign=youtube">Sevalla</a>.
2. Register and click on "Deploy a new database".
3. Select a database name (social_app), username, password, and display name (social_app, as well).
4. In the "networking" tab - enable an external connection.
5. In the "overview" tab - copy the URL of your new database.
6. Back in your WSL terminal, type the following:

```bash
sudo apt update
sudo apt install postgresql
psql <PASTE_YOUR_DATABASE_URL>
```

please make sure the last command looks similar to this:
```bash
psql postgres://<YOUR-USERNAME>:<YOUR-PASSWORD>@<DATABASE-LOCATION>.proxy.sevalla.app:30999/<DATABASE_NAME>
```

7. Once you are connected to your remote database on Sevalla, type the following:
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

8. Then, in `complete_app/app.py` replace `os.getenv("DATABASE_URL")` with the URL of your database, such that:
```
DB_URL = "postgres://<YOUR-USERNAME>:<YOUR-PASSWORD>@<DATABASE-LOCATION>.proxy.sevalla.app:30999/<DATABASE_NAME>"
```

9. Run the complete application locally:

```bash
python app.py
```

10. In your browser, navigate to:

```
http://localhost:8080
```

11. Enjoy! 🤩🤩🤩
12. If you'd like to publish this application, and not just the database - please follow the instructions of my YouTube tutorial!

## 📜 License

MIT License — free to use, modify, and share.

## ⭐ Support

If this project helped you, consider giving it a star on GitHub — it helps others find beginner-friendly resources like this one!

