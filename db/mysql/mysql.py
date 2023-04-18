#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pymysql 库使用

import pymysql

def _connect(host, port, user, passwd, db):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8mb4')
    conn.select_db(db)
    return conn

# 注意，查询，不需要 conn.commit(), 增删改都需要conn.commit(), 才能保证事务的提交。

def _execute(conn, sql):
    cur = conn.cursor()
    # execute() 仅仅返回影响的行数。
    row_affected = cur.execute(sql)
    cur.close()
    return row_affected

def _execute_with_return(conn, sql):
    cur = conn.cursor()
    row_affected = cur.execute(sql)
    ret = []
    if row_affected > 0:
        results = cur.fetchall()
        for row in results:
            ret.append(row)
    
    cur.close()
    return row_affected, ret