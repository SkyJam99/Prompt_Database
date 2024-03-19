
import supabase

from flask import Flask, render_template

app = Flask(__name__)


from supabase import create_client, Client

url: str = "https://nbbemlvtjsvhfgwjbdgx.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5iYmVtbHZ0anN2aGZnd2piZGd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk5OTQ5NDMsImV4cCI6MjAyNTU3MDk0M30.0VYbbTNTEVmzM0ooAvLS09mbfAzsuk4GUEltvl6Y5AE"

supabase: Client = create_client(url, key)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/readPrompt', methods=["GET"])
def readPrompt():
    result: str = "readPrompt"
    getConnection()
    result = supabase.table('prompts').select("*").execute()
    return result


@app.route('/createPrompt', methods=["GET"])
def createPrompt():
    result: str = "createPrompt"

    return result


@app.route('/updatePrompt', methods=["GET"])
def updatePrompt():
    result: str = "updatePrompt"

    return result


def getConnection():
    Client = create_client(url, key)