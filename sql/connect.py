import pymysql.cursors
def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host='ip',
                                 user='login',
                                 password='pass',
                                 db='flightplus',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection