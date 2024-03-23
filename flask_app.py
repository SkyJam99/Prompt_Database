from flask import Flask, redirect, render_template, request, url_for, jsonify
from database_functions import get_all_prompts, get_prompt_by_id, create_prompt, update_prompt, delete_prompt
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
    result: str = get_all_prompts()

    return result

#Get Prompt by id
@app.route('/prompt/<int:id>', methods=["GET"])
def prompt_id(id):
    result: str = get_prompt_by_id(id)

    return result

#Create Prompt
@app.route('/prompt', methods=["POST"])
def create_prompt():
    data = request.json
    result: str = create_prompt(data)

    return result

#Update Prompt
@app.route('/prompt/<int:id>', methods=["PUT"])
def update_prompt(id):
    data = request.json
    result: str = update_prompt(id, data)

    return result

#Delete Prompt
@app.route('/prompt/<int:id>', methods=["DELETE"])
def delete_prompt(id):
    result: str = delete_prompt(id)

    return result



