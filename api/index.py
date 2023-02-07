from flask import Flask, request, jsonify

app = Flask(__name__)

nostr_data = {
    "names": {
        "bitcoinplebdev": "8172b9205247ddfe99b783320782d0312fa305a199fb2be8a3e6563e20b4f0e2"
    }
}


@app.route('/.well-known/nostr.json')
def nostr_json():
    name = request.args.get("name")
    if name not in nostr_data["names"]:
        return "", 404
    response = jsonify(nostr_data)
    response.headers["Content-Type"] = "application/json"
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET")
    return response
