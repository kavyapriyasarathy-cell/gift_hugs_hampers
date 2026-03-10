from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Gift Hugs Hampers</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f8f0ff;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    color: #6a1b9a;
                }
                p {
                    font-size: 20px;
                    color: #444;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to Gift Hugs Hampers</h1>
            <p>One Stop Destination for Jewelry and Hair Accessories</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
