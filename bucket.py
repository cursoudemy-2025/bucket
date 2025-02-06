from flask import Flask, request, send_from_directory, jsonify
import os

API_KEY = "fake_api_key_123456"
API_SECRET = "fake_secret_password_654321"
app = Flask(__name__)
BUCKET_NAME = "cursohackerudemy.s3.amazonaws.com"
UPLOAD_FOLDER = "./bucket_storage"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": f"Simulador do bucket {BUCKET_NAME} rodando!"})

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({"message": f"Arquivo {file.filename} salvo com sucesso!"})

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route("/list", methods=["GET"])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"files": files})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
