from flask import Flask, render_template, request

app = Flask(__name__)

# 首頁
@app.route("/")
def home():
    return render_template("index.html")

# 醫師介紹頁
@app.route("/about")
def about():
    return render_template("about.html")

# 聯繫我們頁
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
    if request.method == "POST":
        # 從表單獲取資料
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return f"感謝聯繫我們, {name}! 我們將盡快回覆您。"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
