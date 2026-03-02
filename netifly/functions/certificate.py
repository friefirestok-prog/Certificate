from flask import Flask, Response
import os

app = Flask(__name__)

# Gunakan prefix 'r' (raw string) atau double backslash '\\'
# agar Python tidak bingung dengan karakter backslash di Windows.
CERT_PATH = r"C:\Users\Administrator\.mitmproxy\mitmproxy-ca-cert.pem"

@app.route('/api/certificate', methods=['GET'])
def get_certificate():
    try:
        if os.path.exists(CERT_PATH):
            with open(CERT_PATH, 'r') as f:
                cert_content = f.read()
            return Response(cert_content, mimetype='text/plain')
        else:
            return "File tidak ditemukan di path yang ditentukan.", 404
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    # Berjalan di port 5000
    print("Server API berjalan di http://localhost:5000/api/certificate")
    app.run(host='0.0.0.0', port=5000)