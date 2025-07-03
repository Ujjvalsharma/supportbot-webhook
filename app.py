from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req['queryResult']['intent']['displayName']

    if intent == 'fallback_to_webhook':
        response_text = "Sure! I can help with appointments and orders. Please provide more details."
    else:
        response_text = "Sorry, I couldn't understand that."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run()
