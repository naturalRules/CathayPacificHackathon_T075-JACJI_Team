import sqlite3
import pandas as pd

# 确定你是否要使用 openpyxl 或 xlsxwriter
# 如果你要创建 .xlsx 文件，通常使用 openpyxl 就可以了。
# Windows 用户可能需要先通过 pip install 这两个包
excel_writer_engine = 'openpyxl'  # 或者 'xlsxwriter'


def sqlite_to_excel(sqlite_file, excel_file):
    # 创建一个SQLite3连接
    conn = sqlite3.connect(sqlite_file)

    # 获取数据库中所有的表名
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # 创建一个新的Excel writer
    with pd.ExcelWriter(excel_file, engine=excel_writer_engine) as writer:
        for table_name in tables:
            table_name = table_name[0]

            # 将SQLite的每张表读入到DataFrame
            df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)

            # 写入DataFrame到Excel，保存在相应的Sheet
            df.to_excel(writer, sheet_name=table_name, index=False)

    # 关闭数据库连接
    conn.close()


# 使用该函数
sqlite_to_excel('database/waste.db', 'database/waste.xlsx')
