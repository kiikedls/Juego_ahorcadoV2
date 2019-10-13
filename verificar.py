import pymysql


class verificar:

    @staticmethod
    def verificar():
        try:
            db = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',
                                 db='juego')
            return True
        except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return False
