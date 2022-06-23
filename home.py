from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    # 往模板中传入的数据
    mealData = getData()
    return render_template(r'home.html', result=mealData)


def getData():
    """
    从 mysql 中读取数据并返回
    :return:
    """
    connect = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="meal")
    cursor = connect.cursor()
    mealData = []
    try:
        cursor.execute("select * from `hotMeals`")
        for i in range(10):
            mealData.append(cursor.fetchone())
    finally:
        cursor.close()
    print(mealData[0])
    return mealData


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7500, debug=True)
