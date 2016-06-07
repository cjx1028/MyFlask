#encoding=utf8
import sqlite3
from flask import Flask

# configuration
DATABASE='mydb'
DEBUG = True


#create my application
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/urls")
def get_urls(begin=0, size=10):
    sql = "select * from t_url where id >= %d limit 10" % begin
    print sql
    conn = sqlite3.connect(app.config['DATABASE'])
    if not conn:
        return "connect failed"
    resultset = conn.cursor().execute(sql).fetchall();
    return str(resultset)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/readfile")
def readfile():
    f = open("./static/mystaticfile.txt", 'r')
    content = f.read()
    f.close()
    return content;

@app.route("/config")
def config():
    return app.config['DATABASE']

@app.route("/")
def index():
    return "index page"

@app.route("/user/<username>")
def show_user_profile(username):
    return "user is %s" % username

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "post %d" % post_id

@app.route('/static/<path:path>')
def send_static(path):
    return url_for('static', path);
    #return send_from_directory('static', path)

if __name__ == "__main__":
    app.run('0.0.0.0')

