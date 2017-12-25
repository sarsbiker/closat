'''
创建数据表
'''
import sqlite3
import random
from random import choice
#import time

class Cards():
    def select_card(self):
        '''从数据库中查询指定名称的卡片'''
        conn = sqlite3.connect('closat.db')
        c = conn.cursor()
        get_card = c.execute("select type,cardname,detail from cards ", ())
        #type, name, detail = list(get_card)
        gege = list(get_card)
        conn.close()
        return gege #(type, name, detail)

    def insert_card(self, cardname,type, detail):
        '''新增卡片信息'''
        conn = sqlite3.connect('closat.db')
        c = conn.cursor()
        count_num = c.execute("select count(*) from cards")
        id_num = list(count_num)[0][0]
       # time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #需要增加try，有异常就需要返回错误提示，成功就返回成功
        try:
            c.execute("insert into cards values (?,?,?,?)",
                    (int(id_num) + 1, cardname, type, detail))
            conn.commit()
            conn.close()
            return '提交成功'
        except:
            return '提交失败，该卡片名称已存在'

    def random_card(self,gametype):
        '''按写作课的游戏规则，生成2+1+1形式'''
        type1 = '人物'
        type2 = '地点'
        type3 = '物件'
        list1 = ['人物','地点','物件','主题']
        if gametype == 'random4':
            return self.random_some_card(type1,2) + self.random_some_card(type2, 1) + self.random_some_card(type3, 1)
        elif gametype == 'random1':
            return self.random_some_card(random.choice(list1),1)
        elif gametype == 'allcard':
            return self.select_card()

    def random_some_card(self,type,num):
        '''按指定类型和数量读取N张卡片信息'''
        conn = sqlite3.connect('closat.db')
        c = conn.cursor()
        get_cards = list(c.execute("select type,cardname,detail from cards where type = ? ", (type,)))
        #如果数据量较大，就要考虑先数一下有多少张卡片，然后再取一个随机数，再取读取一遍；或者直接随机取
        if len(get_cards) < num:
            return False
        else:
            return random.sample(get_cards,num)

    def guide(self):
        return '''CLOSAT 游戏是 Michael Rabiger 教授在 《开发故事创意》 里介绍的一个激发灵感的小游戏。CLOSAT 各字母指代如下，你日常就可以积累这些故事素材，做成卡片，以备随时取用、激发灵感：
C~Characters：某个人物以及对人物的描述。有潜力（指外表、言行举止、职业等）成为某个故事角色的人物。
L~Location：有趣的可视化地点。预示着有事情发生的任何地点。当你看到一些不错的场景，都可以记录下来。
O~Object：让人好奇或者能够引起共鸣的事物。它可以让某一地点、时间、情境或者人物更加具说服力。
S~Situation：充满矛盾或者揭示性的情境。同时发生的多种情况的结合，或是把角色推向一些特殊压力之下的困境。
A~Act：不寻常或者揭示性的行动。任何可能含有意义或目的的行为或动作。
T~Theme：任何你感兴趣的主题或者在你的生活中呈现的主题。可以理解为故事的中心思想或者主要思想，是故事内容的基础。
制作完卡片之后，就可以点击上面的按钮，选择几张卡片，开始创作故事。'''

'''- 类文件
  - 支持插入卡片，
  - 读取所有卡片，
  - 读取指定卡片1
  - 按名称查询1
  - 按游戏规则查询
  - 按类别查询1'''
