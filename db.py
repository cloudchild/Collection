import pymysql
import traceback

# 读取txt 文件数据
def get_data():
    '''
    读取数据
    :return: data
    '''
    filename = 'data/l_data/20201215.txt' # 文件路径
    with open(filename, 'r') as f:
        data = f.readlines() # 逐行读取带换行符，以列表形式存储
        # print(data)
        for line in data:
            result = [ele.strip(' ') for ele in line.split('+')] #单个数据分隔开并去掉空格
    return result
def get_db_conn():
    '''
    连接数据库
    :return: conn, cursor
    '''
    # 建立连接
    conn = pymysql.connect(user='root', password='123456', database='data1')
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor

def close_db_conn(conn, cursor):
    '''
    关闭数据库连接
    :param conn: 连接
    :param cursor: 游标
    :return: None
    '''
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql, *args):
    '''
    封装通用的查询
    :param sql:sql语句
    :param args:参数
    :return:查询的结果
    '''
    conn, cursor = get_db_conn()
    cursor.execute(sql, args)
    ret = cursor.fetchall()  # 拿到所有数据
    close_db_conn(conn, cursor)
    return ret

def insert_history_data():
    '''
    插入历史数据
    :return:None
    '''
    conn = None
    cursor = None
    try:
        print(get_data())
        dic = get_data() # 读取数据
        print(dic)
        conn, cursor = get_db_conn()
        sql = 'insert into history_data values (%s,%s,%s)'
        for k in dic:
             print(key, value)
        cursor.execute(sql,k)
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        close_db_conn(conn, cursor)

# 数据查询
def query_data():
    '''
    获取查询数据
    :return:
    '''
    conn, cursor = None, None
    sql = ''
    ret = query(sql)
    # print(ret)
    return ret