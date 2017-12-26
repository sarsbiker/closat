#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : sarsiker
# @Site    : ${SITE}
# @File    : ${NAME}.py
# @Software: ${PRODUCT_NAME}

import cards
from flask import render_template, request, Flask

app = Flask(__name__)

@app.route('/',methods = ['get','post'])
@app.route('/<name>',methods = ['get','post'])#增加对各种子页面的支持
def home(help=None,name=None,card=None,type=None,card1=None): #help参数如果是在页面内被调用的话，无须赋值
    type= request.values.get('type','')
    card = request.values.get('cardname','')
    detail = request.values.get('detail','')
    help = request.values.get('help', '')
    task = cards.Cards()
    help2 = task.guide()
    randomcard = request.values.get('random','')
    if request.values.get('add','') == 'add':
        result = task.insert_card(card, type, detail)
        return render_template('index.html',result=result, cardname=card,type=type,detail=detail)
        #名字全部都改成cardname，直接使用name之类的容易与默认名称冲突
    elif help == name: #测试帮助页面
        return render_template('index.html', help=help2, name = name)
    elif randomcard != None:
        card1=task.random_card(randomcard)
        return render_template('show.html',card1=card1)
    elif card == None:
        return render_template('index.html', name='card')
    else:
        return render_template('index.html', cardname=card, type=type, detail=detail )

@app.route('/show',methods = ['get','post'])
def show(name=None,card=None,type=None,card1=None):
    type= request.values.get('type','')
    card = request.values.get('cardname','')
    detail = request.values.get('detail','')
    help = request.values.get('help', '')
    task = cards.Cards()
    help2 = task.guide()
    randomcard = request.values.get('random','')
    if help == 'help':
        return home(help)
    elif randomcard != None:
        card1=task.random_card(randomcard)
        return render_template('show.html',card1=card1)
    elif card == None:
        return render_template('index.html', name='card')
    else:
        return render_template('index.html', name=card, type=type, detail=detail )

if __name__ == '__main__':
    app.run(debug=True)
