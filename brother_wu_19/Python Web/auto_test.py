import requests
import jsonpath
import pymysql

def get_conn():
    return pymysql.connect(
        host='172.29.76.72',
        port=3320,
        user='testoms',
        password='Test123456',
        database='testoms',
        charset='utf8'
    )

def query_data(sql):
    conn=get_conn()
    try:
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        print(cursor.fetchall())
        return cursor.fetchall()
    finally:
        conn.close()


headers ={"X-SHOPPY-ACCESS-TOKEN":"0c0aa7b4188f434bd829049a6587c052820d0798"}

url="https://openapi.xshoppy.top/order/orders/list"
data={
    'time_start':1618193378,
    'time_end':1618193398,
    'page':1,
    'limit':100,
    'financial_status':'paid'
    }

def xshoppy_orders_list():
    ret=requests.get(url,params=data,headers=headers)
    result=ret.json()
    print(result)
    sku=jsonpath.jsonpath(result,'$.data.data[0].products[0].sku')
    email=jsonpath.jsonpath(result,'$.data.data[0].shipping.email')
    order_number=jsonpath.jsonpath(result,'$.data.data[0].order_number')
    print(sku[0])
    print(email[0])
    print(order_number[0])
    return sku[0],email[0],order_number[0]



if __name__ == '__main__':
    xshoppy_orders_list()
    sql1="SELECT  email FROM `testoms`.`sales_order_master` WHERE `platform_order_number` = '210412100948215'"
    query_data(sql1)
