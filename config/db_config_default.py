# encoding: utf-8

# 存储news与html的数据库配置列表
WEBSITE_CONFIG_LIST = {
    '00': {# 此为公用测试数据库，可以换成自己的
        'host': '192.168.235.5',
        'port': 3306,
        'user': 'dg',
        'password': 'dg',
        'db': 'dg_db_website'
    },
    '01': {
        'host': 'localhost',
        'port': 3306,
        'user': 'your username',
        'password': 'your password',
        'db': 'dg_test'
    }
}