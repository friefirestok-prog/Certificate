import os

def handler(event, context):
    # Mengambil path folder utama di server Netlify
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    cert_path = os.path.join(root_dir, "mitmproxy-ca-cert.pem")
    
    try:
        if os.path.exists(cert_path):
            with open(cert_path, "r") as f:
                content = f.read()
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "text/plain"},
                "body": content
            }
        else:
            return {
                "statusCode": 404,
                "body": f"File tidak ditemukan di path: {cert_path}"
            }
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
