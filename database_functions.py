from supabase import create_client, Client


url: str = "https://nbbemlvtjsvhfgwjbdgx.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5iYmVtbHZ0anN2aGZnd2piZGd4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk5OTQ5NDMsImV4cCI6MjAyNTU3MDk0M30.0VYbbTNTEVmzM0ooAvLS09mbfAzsuk4GUEltvl6Y5AE"

# supabase: Client = create_client(url, key)

table_format = "<table class='table table-hover table-primary table-bordered table-striped'>"

def getConnection():
    supabase: Client = create_client(url, key)
    return supabase

supabase = getConnection()
response = supabase.table('prompts').select("*").execute()

def readPrompt():
    # Check if data is present in the response
    if not response.data:  # Simplified error handling
        print("No Data Found")
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
    print(html_output)  # Print the HTML table

readPrompt()
