from flask import Flask, request, render_template

from config.base import Configuration

app = Flask(__name__)

app.config.from_object(Configuration)


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        textFilter = request.form['InputText']  # mengambil data dari form
        print(textFilter)
    else:
        print('tidak di baca')
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
