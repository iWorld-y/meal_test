# from flask import Flask, render_template, request
# import pymysql
#
# app = Flask(__name__)
#
#
# class DataStore():
#     a = None
#
#
# data = DataStore()
#
#
# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index2.html')
#
#
# '''
#     教程测试代码
# '''
#
#
# @app.route('/result', methods=['POST', 'GET'])
# def result():
#         meal_id = request.form['meal_id']
#         # data.a = id
#         meal_score = request.form['meal_score']
#         try:
#             meal_id = float(meal_id)
#             meal_score= float(meal_score)
#             conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306,
#                                    db='student')
#             cur = conn.cursor()  # 生成游标对象
#             sql = "INSERT INTO `meal`( `meal_score`) VALUES (%s,%s)",(meal_score)
#             try:
#                 # 执行sql语句
#                 cur.execute(*sql)
#                 # 提交到数据库执行
#                 conn.commit()
#             except:
#                 # 如果发生错误则回滚
#                 conn.rollback()
#
#             # sql = "SELECT * FROM `student` WHERE `id` = %s" % data.a
#             sql = "SELECT * FROM `meal` "
#             cur.execute(sql)
#             u = cur.fetchall()
#             print(u)
#             conn.close()
#             return render_template('index3.html', u=u)
#
#         except:
#             return render_template('index2.html', message='inputs false!!!')
#
#     # if request.method == 'POST':
#     #
#     #     result = request.form
#     #     # print(f"网页返回的数据： {result}")
#     #     return render_template("result.html", result=result)
#
#
# # @app.route('/', methods=['POST'])
# # def add():
# #     id = request.form['id']
# #     data.a = id
# #     name = request.form['name']
# #     age = request.form['age']
# #     sex = request.form['sex']
# #     try:
# #         id = float(id)
# #         age = float(age)
# #         conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306,
# #                                db='student')
# #         cur = conn.cursor()  # 生成游标对象
# #         sql = "INSERT INTO `student`(`id`, `name`, `age`, `sex`) VALUES (%s,%s,%s,%s)", (id, name, age, sex)
# #         try:
# #             # 执行sql语句
# #             cur.execute(*sql)
# #             # 提交到数据库执行
# #             conn.commit()
# #         except:
# #             # 如果发生错误则回滚
# #             conn.rollback()
# #
# #         # sql = "SELECT * FROM `student` WHERE `id` = %s" % data.a
# #         sql = "SELECT * FROM `student` "
# #         cur.execute(sql)
# #         u = cur.fetchall()
# #         print(u)
# #         conn.close()
# #         return render_template('index3.html', u=u)
# #
# #     except:
# #         return render_template('index2.html', message='inputs false!!!', var1=id, var2=name, var3=age, var4=sex)
#
#
# if __name__ == '__main__':
#     app.run(port=8002)
# -----------------------------------------------------------------------------------

from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

class DataStore():
    a = None
data = DataStore()

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def add():
    mealid = request.form['mealId']
    data.a = mealid
    mealscore = request.form['mealScore']
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306,db='student')
        cur = conn.cursor()  # 生成游标对象
        sql = "INSERT INTO `meal`(`mealId`, `mealScore`) VALUES (%s,%s)",(mealid, mealscore)
        try:
            # 执行sql语句
            cur.execute(*sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

        sql = "SELECT * FROM `meal`"
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        return render_template('index3.html', u=u)
        conn.close()
    except:
        return render_template('index2.html', message='inputs false!!!',)


if __name__ == '__main__':
    app.run(port=8002)

