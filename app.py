from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>Professor Hobbies</title>
        <style>
            body { font-family: sans-serif; background: #eef2f3; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background: white; padding: 40px; border-radius: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); text-align: center; border-top: 8px solid #3498db; }
            h1 { color: #2c3e50; font-size: 2.5rem; }
            p { color: #7f8c8d; font-size: 1.2rem; }
            .status { background: #2ecc71; color: white; padding: 8px 20px; border-radius: 50px; display: inline-block; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>👨‍🏫 بروفيسور الهوايات</h1>
            <p>أهلاً بكم في مشروعي الأول على الإنترنت!</p>
            <div class="status">الموقع يعمل بنجاح ✅</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
  
