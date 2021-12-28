from flask import Flask, request, render_template
from csv import writer
import re

app = Flask(__name__)
file_path = "./data.csv"
port_num = 18011 # 学籍番号を各自入力


@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_num)
