from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    #if request.user_agent.is_mobile:
    #    return render_template('mobile/index.html')
    #else:
    #    return render_template('index.html')
    return render_template('index.html')

@app.route("/content")
def main_page():
    return render_template("content.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
