from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/reason", methods=["POST"])
def reason():
    data = request.get_json()
    query = data.get("query", "").lower().strip()

    # Basic static reasoning logic
    if "weather" in query:
        response = "I'm not connected to a weather service, but it's probably sunny!"
    elif "who are you" in query:
        response = "I'm your assistant, Jarvis."
    elif "capital of france" in query:
        response = "The capital of France is Paris."
    elif "capital of kenya" in query:
        response = "The capital of Kenya is Nairobi."
    elif "python" in query:
        response = "Python is a high-level, interpreted programming language known for its simplicity."
    elif "jarvis" in query:
        response = "Yes, I am Jarvis, your personal assistant."
    elif "time" in query:
        from datetime import datetime
        response = "The current time is " + datetime.now().strftime("%I:%M %p")
    else:
        response = f"Sorry, I couldn't understand '{query}'. Try rephrasing."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
