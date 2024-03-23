from flask import Flask, render_template

app = Flask(__name__)


# from supabase import create_client, Client

# url: str = "https://nbbemlvtjsvhfgwjbdgx.supabase.co"
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5iYmVtbHZ0anN2aGZnd2piZGd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk5OTQ5NDMsImV4cCI6MjAyNTU3MDk0M30.0VYbbTNTEVmzM0ooAvLS09mbfAzsuk4GUEltvl6Y5AE"

# supabase: Client = create_client(url, key)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/readPrompt', methods=["GET"])
def readPrompt():
    result: str = "readPrompt"
    
    return result


@app.route('/createPrompt', methods=["GET"])
def createPrompt():
    result: str = "createPrompt"

    return result


@app.route('/updatePrompt', methods=["GET"])
def updatePrompt():
    result: str = "updatePrompt"

    return result

#CRUD operations
#Get All prompts
@app.route('/prompt', methods=["GET"])
def prompt():
    result: str = "prompt"

    return result

#Get Prompt by id
@app.route('/prompt/<int:id>', methods=["GET"])
def prompt_id(id):
    result: str = "prompt_id"

    return result

#Create Prompt
@app.route('/prompt', methods=["POST"])
def create_prompt():
    result: str = "create_prompt"

    return result

#Update Prompt
@app.route('/prompt/<int:id>', methods=["PUT"])
def update_prompt(id):
    result: str = "update_prompt"

    return result

#Delete Prompt
@app.route('/prompt/<int:id>', methods=["DELETE"])
def delete_prompt(id):
    result: str = "delete_prompt"

    return result




def getConnection():
    Client = create_client(url, key)