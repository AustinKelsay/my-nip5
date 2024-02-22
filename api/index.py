from flask import Flask, request, jsonify

app = Flask(__name__)

nostr_data = {
    "names": {
        "<YOUR NOSTR ALIAS>": "<YOUR NOSTR PUBLIC KEY IN HEX FORMAT>"
    },
    "relays": {
        "<YOUR NOSTR PUBLIC KEY IN HEX FORMAT>": [ "wss://relay.mutinywallet.com/", "wss://relay.primal.net/" ]
    }
}


@app.route('/.well-known/nostr.json')
def nostr_json():
    name = request.args.get("name")
    public_key = nostr_data["names"].get(name)
    if public_key is None:
        return "", 404

    response_data = {"names": {name: public_key}}
    response = jsonify(response_data)
    response.headers["Content-Type"] = "application/json"
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET")
    return response
