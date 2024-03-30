from supabase import create_client, Client
from flask import jsonify
from openai import OpenAI
from openaikey import openaikey

# TODO - remove this API key, delete it, and create an environment key
client = OpenAI(
    api_key=openaikey
)

# Backend funtion that takes a prompt and returns the completion
def get_completion(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a flexible assistant, helping the user with anything they ask for in a step by step way to ensure the best possible results."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message

print(get_completion("What is the capital of the United States?"))

url: str = "https://nbbemlvtjsvhfgwjbdgx.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5iYmVtbHZ0anN2aGZnd2piZGd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk5OTQ5NDMsImV4cCI6MjAyNTU3MDk0M30.0VYbbTNTEVmzM0ooAvLS09mbfAzsuk4GUEltvl6Y5AE"

# supabase: Client = create_client(url, key)

table_format = "<table class='table table-hover table-primary table-bordered table-striped'>"
supabase: Client = create_client(url, key)


def getConnection():
    supabase: Client = create_client(url, key)
    return supabase

# getConnection()
# response = supabase.table('prompts').select("*").execute()

# def readPrompt():
#     # Check if data is present in the response
#     if not response.data:  # Simplified error handling
#         print(response)
#         return None

#     # Construct HTML table from response data
#     html_output = table_format  # Start the table and add headers

#     # Add column headers based on the first item keys if there's data
#     if response.data:
#         html_output += '<tr>' + ''.join([f'<th>{col.capitalize()}</th>' for col in response.data[0].keys()]) + '</tr>'

#         # Fill the table rows with the data
#         for item in response.data:
#             html_output += '<tr>' + ''.join([f'<td>{item[col]}</td>' for col in item.keys()]) + '</tr>'

#     html_output += "</table>"  # Close the table
#     print(html_output)  # Print the HTML table

#readPrompt()
    
#Response to HTML function
def response_to_html(response):
    # Check if data is present in the response
    if not response.data:  # Simplified error handling
        print(response)
        return None

    # Construct HTML table from response data
    html_output = table_format  # Start the table and add headers

    # Add column headers based on the first item keys if there's data
    if response.data:
        html_output += '<tr>' + ''.join([f'<th>{col.capitalize()}</th>' for col in response.data[0].keys()]) + '</tr>'

        # Fill the table rows with the data
        for item in response.data:
            html_output += '<tr>' + ''.join([f'<td>{item[col]}</td>' for col in item.keys()]) + '</tr>'

    html_output += "</table>"  # Close the table
    return html_output  # Print the HTML table


#CRUD operations
    
#Get All prompts
def get_all_prompts_db():
    getConnection()
    response = supabase.table('prompts').select("*").execute()
    
    if not response.data:
        return "Error: No data found (GET ALL)", 400

    #return response_to_html(response)
    return response.data


#Get Prompt by id
def get_prompt_by_id_db(id: int):
    getConnection()
    response = supabase.table('prompts').select("*").eq('id', id).execute()

    if not response.data:
        return "Error: No data found (GET BY ID)", 400

    #return response_to_html(response)
    return response.data


#Create Prompt
def create_prompt_db(prompt: dict):
    getConnection()
    response = supabase.table('prompts').insert(prompt).execute()

    if not response.data:
        return "Error: No data found (CREATE)", 400

    #return response_to_html(response)
    return response.data

#Update Prompt
def update_prompt_db(id: int, prompt: dict):
    getConnection()
    response = supabase.table('prompts').update(prompt).eq('id', id).execute()

    if not response.data:
        return "Error: No data found (UPDATE)", 400

    #return response_to_html(response)
    return response.data

#Delete Prompt
def delete_prompt_db(id):
    getConnection()
    response = supabase.table('prompts').delete().eq('id', id).execute()

    if not response.data:
        return "Error: No data found (DELETE)", 400

    #return response_to_html(response)
    return response.data

#prompt JSON format
# {
#     "id": int,
#     "name": string,
#     "prompt_content": string,
#     "prompt_variables": string,
#     "designed_for": string,
#     "parent_prompt_id": int
#}

#Test the functions
# print(get_all_prompts())
# print(get_prompt_by_id(8))
# print(create_prompt({
#     "name": "Test Prompt",
#     "prompt_content": "This is a test prompt",
#     "prompt_variables": "Test",
#     "designed_for": "Test"
# }.json))
# print(update_prompt(1, {
#     "name": "Test Prompt",
#     "prompt_content": "Updated test prompt",
#     "prompt_variables": "Test",
#     "designed_for": "Test",
#     "parent_prompt_id": 1
# }.json))
# print(delete_prompt(1))