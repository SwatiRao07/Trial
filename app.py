from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = "Swati"
    tasks = ["Learn Flask", "Build Project", "Deploy App"]
    return render_template('index.html', name=user_name, todo=tasks)

if __name__ == '__main__':
    app.run(debug=True)
