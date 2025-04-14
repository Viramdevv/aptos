from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock storage for sessions
sessions = {}

@app.route('/register_session', methods=['POST'])
def register_session():
    data = request.json
    counselor = data.get("counselor")
    nft_id = data.get("nft_id")
    
    if not counselor or not nft_id:
        return jsonify({"error": "Missing counselor address or NFT ID"}), 400
    
    sessions[counselor] = {"counselor": counselor, "nft_required": nft_id}
    
    return jsonify({"message": "Session registered successfully", "session": sessions[counselor]})

@app.route('/book_session', methods=['POST'])
def book_session():
    data = request.json
    user = data.get("user")
    counselor = data.get("counselor")
    
    if counselor not in sessions:
        return jsonify({"error": "Session not found"}), 404
    
    # Simulate NFT check (replace with real blockchain interaction)
    if data.get("nft_id") != sessions[counselor]["nft_required"]:
        return jsonify({"error": "NFT ownership validation failed"}), 403
    
    return jsonify({"message": f"Session booked successfully with {counselor}!"})

if __name__ == '__main__':
    app.run(debug=True)
