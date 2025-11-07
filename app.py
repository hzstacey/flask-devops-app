from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>My DevOps App</title>
        <style>
            body { 
                background: #1e1e2f; 
                color: #f0f0f0; 
                font-family: Arial, sans-serif; 
                text-align: center; 
                padding-top: 100px;
            }
            h1 { color: #ffcc00; font-size: 50px; }
            p { font-size: 20px; }
            .button {
                background-color: #ff6600;
                color: white;
                padding: 15px 30px;
                text-decoration: none;
                font-size: 20px;
                border-radius: 8px;
                margin-top: 30px;
                display: inline-block;
            }
            .button:hover {
                background-color: #ff9933;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to My DevOps App!</h1>
        <p>Learn Docker, Flask, and DevOps the fun way!</p>
        <a href="#" class="button">Get Started</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
