import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/main", methods=["GET", "POST"])
def start():
    return render_template("main.html")


# 添加用户
@app.route("/add/customer", methods=["GET", "POST"])
def add_customer():
    if request.method == "GET":
        return render_template("add_customer.html")

    try:
        customerid = request.form.get("customerid")
        cname = request.form.get("cname")
        gender = request.form.get("gender")
        if customerid == "" or cname == "" or gender == "":
            return "输入里有空值，请重新输入"

        # 连接MySQL
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                               db="databaselab2")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 执行SQL
        sql = "insert into customer(customerid, cname, gender) values(%s, %s, %s )"
        cursor.execute(sql, [customerid, cname, gender])
        conn.commit()

        # 关闭连接
        cursor.close()
        conn.close()
        return "添加成功"

    except:
        return "主键不能重复"


# 查询商品
@app.route("/query/goods", methods=["GET", "POST"])
def query_goods():
    if request.method == "GET":
        return render_template("query_goods.html")

    goodsid = request.form.get("goodsid")

    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                           db="databaselab2")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(123)

    # 执行SQL
    sql = "select * from goods where goodsid = %s"
    cursor.execute(sql, [goodsid, ])
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()

    return render_template("show_goods.html", data_list=data_list)


@app.route("/join_query", methods=["GET", "POST"])
def join_query():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                           db="databaselab2")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(123)

    # 执行SQL
    sql = "select cname, totalprice from customer, shoppingcart where customer.customerid = shoppingcart.customerid and customer.customerid = 3 "
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()

    return render_template("show_join_query.html", data_list=data_list)


@app.route("/nested_query", methods=["GET", "POST"])
def nested_query():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                           db="databaselab2")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(123)

    # 执行SQL
    sql = "select * from customer where customerid not in (select customerid from orderform)"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()

    return render_template("show_nested_query.html", data_list=data_list)


# 删除id为5的用户
@app.route("/delete", methods=["GET", "POST"])
def delete():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                           db="databaselab2")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(123)

    # 执行SQL
    sql = "delete from customer where customerid = 10"
    cursor.execute(sql)
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()
    return "删除成功"


# 分组查询
@app.route("/group_query", methods=["GET", "POST"])
def group_query():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                           db="databaselab2")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(123)

    # 执行SQL
    sql = "select * from customer, evaluation where customer.customerid = evaluation.customerid group by customer.customerid having count(*) >= 2"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()
    return render_template("show_group_query.html", data_list=data_list)


# 创建视图
@app.route("/create_view", methods=["GET", "POST"])
def create_view():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="kevin", passwd="Kevin220419", charset="utf8",
                           db="databaselab2")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(123)

    # 执行SQL
    # sql = "create view customerOrderView as select orderform.orderid, orderform.ordertime, orderform.totalprice from orderform"
    # cursor.execute(sql)
    sql = "select * from customerOrderView "
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()
    return render_template("show_view1.html", data_list=data_list)


# 索引

if __name__ == '__main__':
    app.run()
