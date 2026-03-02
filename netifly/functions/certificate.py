import os

def handler(event, context):
    # Mencari file sertifikat di direktori utama (root) repositori
    cert_path = os.path.join(os.getcwd(), "mitmproxy-ca-cert.pem")
    
    try:
        # Mengecek apakah file sertifikat ada
        if os.path.exists(cert_path):
            with open(cert_path, "r") as f:
                content = f.read()
            
            # Mengembalikan isi sertifikat sebagai teks murni (plain text)
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/plain",
                    "Access-Control-Allow-Origin": "*" # Agar bisa diakses dari mana saja
                },
                "body": content
            }
        else:
            return {
                "statusCode": 404,
                "body": "Error: File mitmproxy-ca-cert.pem tidak ditemukan di root folder GitHub."
            }
            
    except Exception as e:
        # Menampilkan error jika terjadi masalah teknis
        return {
            "statusCode": 500,
            "body": f"Terjadi kesalahan server: {str(e)}"
        }
