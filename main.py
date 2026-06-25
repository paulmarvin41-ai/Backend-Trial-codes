from fastapi import FastAPI
import psycopg2


app = FastAPI()


def get_db():
    return psycopg2.connect(
        host="xxxxxxx", 
        database="xxxxxx", 
        user="xxxxxxx", 
        password="xxxxxxxx"
    )


@app.post("/users")
def create_user(user: dict):
    name = user["name"]
    email = user["email"]
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users(user_name, user_email) VALUES (%s,%s) RETURNING user_id", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": user_id, "name": name, "email": email}


#This just a practice to learn code(API) not intended for production ready projects.