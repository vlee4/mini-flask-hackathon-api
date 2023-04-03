from flask import Flask, request

app = Flask(__name__)

hackathons = {
    "hackathon1": {
        "Name": "hackathon 1",
        "theme": "APIs",
        "start_date": "2023-04-10 12:00:00",
        "end_date": "2023-04-11 12:00:00",
        "location": "Online",
        "Type": "Online only"
    },
   "hackathon2": {
        "Name": "hackathon 2",
        "theme": "Design",
        "start_date": "2023-04-13 12:00:00",
        "end_date": "2023-04-15 12:00:00",
        "location": "In a building",
        "Type": "In-person"
    }
}

@app.route("/")
def hello_ghw():
    return "<p>What's up Hackers!</p>"

@app.route("/hackathons", methods=['GET', 'POST'])
def getHackathons():
    if request.method == 'POST':
        hackathons["new key"] = request.json
        return hackathons
    else:
        return hackathons

if __name__=="__main__":
    app.run(debug=True)
