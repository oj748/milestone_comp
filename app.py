from flask import Flask
import pymysql


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "oJaswini@07"
app.config["MYSQL_DB"] = "event"


def get_connection():
    conn = pymysql.connect(
        host =app.config["MYSQL_HOST"],
        user = app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        db=app.config["MYSQL_DB"]
    )
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS event_t (
    NAME VARCHAR (20),
    EmailID varchar(50) PRIMARY KEY,
    Phone BIGINT,
    event varchar(30)
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()

#@app.route("/register",methods=["/POST"])
def register(name,email,phone,event):
    '''
    data = request.json
    name = data.get("name")
    email = data.get("email")
    phone = data.get('phone')
    event = data.get('event')
    '''
    get_connection()
    conn = get_connection()
    cursor = conn.cursor()
    try :
        cursor.execute("INSERT INTO event_t values (%s,%s,%s,%s)",(name,email,phone,event))
        conn.commit()
        return {"status":"success"}
    except pymysql.err.DataError:
        conn.rollback()
        return {"status":"failure"}
    finally:
        cursor.close()
        conn.close()



def get_records(event):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM event_t WHERE event = %s",event)
    rec = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return rec


if __name__ == "__main__" :
    init_db()

