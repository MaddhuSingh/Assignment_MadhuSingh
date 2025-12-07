import configparser
import json
from flask import Flask, jsonify

# -------------------------------------------
# Step 1: Read configuration file
# -------------------------------------------

config = configparser.ConfigParser()

try:
    config.read("config.ini")   # Read file
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# -------------------------------------------
# Step 2: Extract key-value pairs
# -------------------------------------------

data = {}

try:
    data["Database"] = {
        "host": config["Database"]["host"],
        "port": config["Database"]["port"],
        "username": config["Database"]["username"],
        "password": config["Database"]["password"]
    }

    data["Server"] = {
        "address": config["Server"]["address"],
        "port": config["Server"]["port"]
    }

except KeyError as e:
    print(f"Missing configuration key: {e}")
    exit()

# -------------------------------------------
# Step 3: Save parsed data as JSON
# -------------------------------------------

with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("\nConfiguration File Parser Results:\n")

print("Database:")
print(f"- host: {data['Database']['host']}")
print(f"- port: {data['Database']['port']}")
print(f"- username: {data['Database']['username']}")
print(f"- password: {data['Database']['password']}\n")

print("Server:")
print(f"- address: {data['Server']['address']}")
print(f"- port: {data['Server']['port']}")



# -------------------------------------------
# Step 4: Create GET API using Flask
# -------------------------------------------

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True 

@app.route("/")
def home():
    return "API App is running!"

from flask import Response

@app.get("/config")
def get_config():

    formatted_output = (
        "Configuration File Parser Results:\n\n"
        "Database:\n"
        f"- host: {data['Database']['host']}\n"
        f"- port: {data['Database']['port']}\n"
        f"- username: {data['Database']['username']}\n"
        f"- password: {data['Database']['password']}\n\n"
        "Server:\n"
        f"- address: {data['Server']['address']}\n"
        f"- port: {data['Server']['port']}\n"
    )

    return Response(formatted_output, mimetype="text/plain")



if __name__ == "__main__":
    print("API running at: http://127.0.0.1:5000/config")
    app.run()
