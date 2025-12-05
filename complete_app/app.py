from flask import Flask, render_template
import psycopg

app = Flask(__name__)

DB = "postgresql:///social_app"

def get_all_profiles():
    with psycopg.connect(DB) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT username, photo_path FROM user_profiles;
        """)
        return cursor.fetchall()

def get_profile(username):
    with psycopg.connect(DB) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM user_profiles WHERE username = %s;",
            [username]
        )
        return cursor.fetchall()

@app.route("/")
def home():
    first_username = get_all_profiles()[0][0]
    return profile(first_username)

@app.route("/user/<username>")
def profile(username):
    profiles = get_all_profiles()
    user = get_profile(username)[0]
    return render_template("index.html", user=user, profiles=profiles)

if __name__ == "__main__":
    app.run(debug=True)
    
