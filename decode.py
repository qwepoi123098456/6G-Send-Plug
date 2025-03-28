import os
import base64
import pymysql.cursors

# MySQL 数据库连接配置
# MYSQL_HOST = 'w6109r6604.goho.co'
# MYSQL_PORT = 10195
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'password'
# MYSQL_DB = 'data'
MYSQL_HOST = '10.193.166.100'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123123'
MYSQL_DB = 'view_5g_data_product'


# 建立 MySQL 数据库连接
connection = pymysql.connect(host=MYSQL_HOST,
                             port=MYSQL_PORT,
                             user=MYSQL_USER,
                             password=MYSQL_PASSWORD,
                             db=MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def retrieve_files_from_db(directory):
    with connection.cursor() as cursor:
        #输出哪个
        filename="1.mp4"
        select_query = "SELECT filename, content FROM program_output WHERE filename=%s"
        cursor.execute(select_query, (filename,))
        result = cursor.fetchone()  # 获取查询结果
        if result:
            fetched_filename = result['filename']
            fetched_content = result['content']
            print(f"Fetched filename: {fetched_filename}, content: {fetched_content}")
        else:
            print("No result found for the given filename.")
        # 解码Base64编码的内容
        decoded_content = base64.b64decode(fetched_content)

        # 写入文件
        file_path = os.path.join(directory, filename)
        with open(file_path, 'wb') as f:
            f.write(decoded_content)

    print("Files retrieved successfully!")

# 指定要保存文件的目录
save_directory = './'

# 调用函数将文件从数据库中检索并保存到指定目录
retrieve_files_from_db(save_directory)
