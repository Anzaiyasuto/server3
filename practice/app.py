from flask import Flask, render_template
import csv

app = Flask(__name__)
data = []

@app.route("/index")
def index():
    csv_content = read_csv("AirPassenger")
    for row in csv_content:
        data.append(row[0])
        print(data)
    return render_template("index.html",input_from_python= data) # templatesフォルダ内のindex.htmlを表示する

def read_csv(filename):
    csv_file = open("./csv/" + str(filename) + ".csv", "r", encoding="ms932", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    #f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return f

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='18011')