from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/reason", methods=["POST"])
def reason():
    data = request.get_json()
    user_command = data.get("command", "").lower()

    # Very basic example logic (expand this later)
    if "weather" in user_command:
        return jsonify({"response": "The weather is sunny with light clouds."})
    elif "name" in user_command:
        return jsonify({"response": "I am your assistant Jarvis."})
    elif "time" in user_command:
        from datetime import datetime
        return jsonify({"response": f"It is {datetime.now().strftime('%I:%M %p')}."})
    else:
        return jsonify({"response": f"Sorry, I couldn't understand '{user_command}'."})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
