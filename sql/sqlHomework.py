import xlrd
import pymysql

class Insert :
    def __init__(self, conn):
        try:
            with conn.cursor() as c:
                table = '''
                CREATE TABLE IF NOT EXISTS homework(id INT NOT NULL,
                                                    product TEXT,
                                                    name TEXT,
                                                    num1 INTEGER,
                                                    num2 FLOAT,
                                                    num3 FLOAT,
                                                    num4 FLOAT,
                                                    text TEXT,
                                                    company TEXT,
                                                    num5 FLOAT,
                                                    PRIMARY KEY(id))
                '''
                c.execute(table)

                data = xlrd.open_workbook('databases/5-4.1000 Rows.xlsx').sheet_by_index(0)
                # print(data.ncols)
                # print(data.nrows)
                for i in range(data.nrows):
                    input = data.row_values(i)
                    if input[9] == '':
                        input[9] = 0

                    c.execute("INSERT INTO homework VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", input)
            conn.commit()
        except Exception as e:
            if e == pymysql.err.InternalError:
                pass
        finally:
            conn.close()

    if __name__ == '__main__' :
        pass




class Search :

    def __init__(self, conn):

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as c:
                c.execute("SELECT * FROM homework WHERE num5 = %s", (0,))
                # print(c.fetchall())
                compDict = {}
                for i in c.fetchall():
                    if i['company'] in compDict:
                        compDict[i['company']] += 1
                    else:
                        compDict[i['company']] = 1
                # print(compDict)

                c.execute("SELECT * FROM homework WHERE name = %s", ('Carlos Soltero',))
                # print(c.fetchall())
                productLi = []
                compLi = []

                for i in c.fetchall():
                    # product 담기
                    productLi.append(i['product'])

                    # company 담기
                    compLi.append(i['company'])

                productLi = set(productLi)
                compLi = set(compLi)

                print("Carlos Soltero : \n - product : {}(".format(len(productLi)), end="")

                # product 프린트
                for n, i in enumerate(productLi):
                    if n + 1 == len(productLi):
                        print("{})".format(i))
                    else:
                        print(i, end="; ")

                # company 프린트
                print(" - company : {}(".format(len(compLi)), end="")
                for n, i in enumerate(compLi):
                    if n + 1 == len(compLi):
                        print("{})".format(i))
                    else:
                        print(i, end="; ")


        finally:
            conn.close()

    if __name__ == '__main__' :
        pass



class myMain :
    conn = pymysql.connect(host='localhost', user='cuzaiPy', password='1111!', db='python_app1', charset='utf8')
    Insert(conn)
    conn = pymysql.connect(host='localhost', user='cuzaiPy', password='1111!', db='python_app1', charset='utf8')
    Search(conn)