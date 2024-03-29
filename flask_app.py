from flask import Flask, redirect, render_template, request, url_for, jsonify
from database_functions import get_all_prompts_db, get_prompt_by_id_db, create_prompt_db, update_prompt_db, delete_prompt_db
app = Flask(__name__)


# from supabase import create_client, Client

# url: str = "https://nbbemlvtjsvhfgwjbdgx.supabase.co"
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5iYmVtbHZ0anN2aGZnd2piZGd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk5OTQ5NDMsImV4cCI6MjAyNTU3MDk0M30.0VYbbTNTEVmzM0ooAvLS09mbfAzsuk4GUEltvl6Y5AE"

# supabase: Client = create_client(url, key)


@app.route('/')
def main_page():
    return render_template('main_page.html')


#CRUD operations
#Get All prompts
@app.route('/prompt', methods=["GET"])
def prompt():
    result = get_all_prompts_db()

    return jsonify(result)

#Get Prompt by id
@app.route('/prompt/<int:id>', methods=["GET"])
def prompt_id(id):
    result = get_prompt_by_id_db(id)

    return jsonify(result)

#Create Prompt
@app.route('/prompt', methods=["POST"])
def create_prompt():
    data = request.json
    result = create_prompt_db(data)

    return jsonify(result)

#Update Prompt
@app.route('/prompt/<int:id>', methods=["PUT"])
def update_prompt(id):
    data = request.json
    result = update_prompt_db(id, data)

    return jsonify(result)

#Delete Prompt
@app.route('/prompt/<int:id>', methods=["DELETE"])
def delete_prompt(id):
    result = delete_prompt_db(id)

    return jsonify(result)



