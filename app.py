from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    note = request.form.get("note")
    if note:
        notes.append(note)
        return redirect(url_for('index'))
    return render_template("home.html", notes=notes, title="Note Taking App")

if __name__ == '__main__':
    app.run(debug=True)