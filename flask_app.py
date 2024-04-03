from flask import Flask, redirect, render_template, request, url_for, jsonify
from database_functions import get_all_prompts_db, get_prompt_by_id_db, create_prompt_db, get_prompt_by_name_db, update_prompt_db, delete_prompt_db, get_completion
app = Flask(__name__)

#Main Page
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

#Get Prompt by name
#
@app.route('/prompt/name/<string:name>', methods=["GET"])
def prompt_name(name):
    result = get_prompt_by_name_db(name)

    return jsonify(result)


#Get Prompt Completion
@app.route('/prompt/completion', methods=["POST"])
def prompt_completion():
    prompt = request.json
    result = get_completion(prompt).content

    return jsonify({"result": result})

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



