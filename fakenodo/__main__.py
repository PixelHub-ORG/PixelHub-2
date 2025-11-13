from flask import Flask
from fakenodo.app.routes import api_bp


# Crear la app Flask
app = Flask(__name__)

# Registrar el blueprint principal
app.register_blueprint(api_bp, url_prefix='/api')

# Health check
@app.route('/health', methods=['GET'])
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    print("Iniciando Fakenodo en http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
