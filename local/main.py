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
def home(name=None,card=None,type=None,card1=None):
    type= request.values.get('type','')
    card = request.values.get('cardname','')
    detail = request.values.get('detail','')
    help = request.values.get('help', '')
    task = cards.Cards()
    help2 = task.guide()
    randomcard = request.values.get('random','')
    if request.values.get('add','') == 'add':
        result = task.insert_card(card, type, detail)
        return render_template('index.html',result=result, name=card,type=type,detail=detail)
    elif help == 'help':
        return render_template('index.html', help=help2)
    elif randomcard != None:
        card1=task.random_card(randomcard)
        return render_template('index.html',card1=card1)
    elif card == None:
        return render_template('index.html', name='card')
    else:
        return render_template('index.html', name=card, type=type, detail=detail )


if __name__ == '__main__':
    app.run(debug=True)
