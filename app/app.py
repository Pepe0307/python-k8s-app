from flask import Flask, jsonify
import os

app = Flask(__name__)

# Get version from environment variable or use default
VERSION = os.environ.get('APP_VERSION', '1.0.0')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/hello')
def hello():
    """Hello world endpoint"""
    return jsonify({"message": "Hello World!"}), 200

@app.route('/version')
def version():
    """Version endpoint"""
    return jsonify({"version": VERSION}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors - return JSON instead of HTML"""
    return jsonify({
        "error": "Not Found",
        "message": "The requested endpoint does not exist",
        "status": 404
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors - wrong HTTP method"""
    return jsonify({
        "error": "Method Not Allowed",
        "message": "The method is not allowed for the requested URL",
        "status": 405
    }), 405

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "status": 500
    }), 500


if __name__ == '__main__':
    # Run on 0.0.0.0 to be accessible from outside the container
    app.run(host='0.0.0.0', port=5000, debug=False)