from flask import Flask, request, jsonify

app = Flask(__name__)

nostr_data = {
    "names": {
        "bob": "b0635d6a9851d3aed0cd6c495b282167acf761729078d975fc341b22650b07b9"
    },
    "relays": {
        "b0635d6a9851d3aed0cd6c495b282167acf761729078d975fc341b22650b07b9": ["wss://relay.example.com", "wss://relay2.example.com"]
    }
}


@app.route('/.well-known/nostr.json')
def nostr_json():
    name = request.args.get("name")
    print(type(name))
    if name not in nostr_data["names"]:
        return "", 404
    return jsonify(nostr_data)


@app.route('/')
def welcome():
    return "server is online"


if __name__ == '__main__':
    app.run()
