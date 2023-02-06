from flask import Flask, request, jsonify

app = Flask(__name__)

nostr_data = {
    "names": {
        "devplebbitcoin": "022522f88059c684e200cbfec9f045eb4c9ed57c158e0294cd01eb81de62e211"
    },
    "relays": {
        "022522f88059c684e200cbfec9f045eb4c9ed57c158e0294cd01eb81de62e211": ["wss://nostr.mom", "wss://no-str.org"]
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
