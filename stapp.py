import streamlit as st
import hashlib as h
import sqlite3 as sq
st.title('餐厅座位预订系统')
st.image('lwj.jpg',width=100)
#登陆
is_loaded=False
name=st.sidebar.text_input('用户名：')
password=st.sidebar.text_input('密码：')
db=sq.connect('E:\王梓毅\Python文件\初学者的web\canting.db')
st.write(h.sha512(password.encode('utf8')).hexdigest())
cur=db.cursor()
try:
    cur.execute('select password from user where user=\'%s\''%name)
    rv=cur.fetchall()
    st.write(rv[0][0])
except:
    st.sidebar.write('用户未找到')
    if st.sidebar.button('创建新用户'):
        n_name=st.sidebar.text_input('新用户名：')
        n_password=st.sidebar.text_input('新密码：')