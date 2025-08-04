from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/reason", methods=["POST"])
def reason():
    data = request.get_json()
    command = data.get("command", "").lower()

    # Simple reasoning logic
    if "capital of france" in command:
        response = "The capital of France is Paris."
    elif "who are you" in command:
        response = "I am your personal AI assistant, built by Mike."
    elif "time in kenya" in command:
        from datetime import datetime
        import pytz
        kenya_time = datetime.now(pytz.timezone('Africa/Nairobi')).strftime("%I:%M %p")
        response = f"The current time in Kenya is {kenya_time}."
    else:
        response = f"I don't know how to answer '{command}' yet."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
