import json

stone_physical = [ "荒蛰", "头狼", "幽魉", "罗鬼" ]
stone_magical  = [ "九环朱蝮", "朱焰魔火", "妖术师", "百眼翼魔"]
stone_other    = [ "凶骸兵", "赤练鬼", "刚破鬼", "咒石兵", "死魇鬼卒", "冰魔蝎", "鬼面花蛛", "尸魔术士", "冥葵"]
properties     = [ "炎", "冰", "雷", "光", "暗" ]
heroes_not_ssr = [ "司徒缨", "周崇", "太渊隐逸", "常逸风", "幻镜胧妖", "应奉仁",
                   "慕容筝", "朱缳", "李盈凤", "杨云佐", "白菀", "相桓子",
                   "紫蕴", "赫兰铁罕", "阳寰", "韩无砂", "高戚",
                   "伊丝朶", "呼延崇", "希维亚", "应灵华", "朱浩", "阿尔泰巴",
                   "雅布斯", "青萝", "韦胜", "高世津",
                   "尉迟良", "虞兮", "鹿昭依"]
heroes_ssr     = [ "冰璃", "剑邪", "古伦德", "夏侯仪", "宇韶容", "封寒月",
                   "封铃笙", "慕容璇玑", "曹沁", "殷剑平", "燕明蓉", "皇甫申",
                   "秦惟刚", "紫枫", "葛云依", "解臾", "郸阴", "阴歙",
                   "韩千秀", "黎幽"]

main_dict = {
  "forbidden_list" : {
    0 : {"name" : "仅允许上阵{}位绝英灵", "range" : [x for x in range(0, 3)]},
    1 : {"name" : "仅允许上阵{}位极英灵", "range" : [x for x in range(0, 3)]},
    2 : {"name" : "仅允许使用{}个绝饰品", "range" : [x for x in range(0, 8)]},
    3 : {"name" : "仅允许使用{}个极饰品", "range" : [x for x in range(0, 8)]},
    4 : {"name" : "禁用{}种指定的物理魂石，指定为{}", "range" : [x for x in range(1, 4)], "candidate" : stone_physical},
    5 : {"name" : "禁用{}种指定的法术魂石，指定为{}", "range" : [x for x in range(1, 4)], "candidate" : stone_magical},
    6 : {"name" : "禁用{}种指定的其他魂石，指定为{}", "range" : [x for x in range(1, 4)], "candidate" : stone_other}  ,
  },
  "limited_list" : {
    0 : {"name" : "限定{}及以下回合通关", "range": [x for x in range(5, 9)]},
    1 : {"name" : "限定死亡人数在{}及以下通关", "range": [x for x in range(3)]},
    2 : {"name" : "限定仅使用{}种指定的属性, 指定为{}", "range": [x for x in range(1, 4)], "candidate" : properties},
    3 : {"name" : "限定任意单人战力不得超过{}", "range": [x for x in range(3000, 5000, 500)]},
    4 : {"name" : "限定总战力不得超过{}", "range": [x for x in range(17000, 21000, 1000)]},
    5 : {"name" : "限定必须上阵{}位指定的英灵，指定为{}", "range": [1], "candidate" : heroes_not_ssr},
    6 : {"name" : "限定不能上阵{}位指定的英灵，指定为{}", "range": [1, 2, 3], "candidate" : heroes_ssr},
  },
  "adding_list" : {
    0  : {"name" : "不允许携带被动技能"},
    1  : {"name" : "不允许携带单体技能"},
    2  : {"name" : "不允许携带群体技能"},
    3  : {"name" : "不允许携带铁卫"}    ,
    4  : {"name" : "不允许携带侠客"}    ,
    5  : {"name" : "不允许携带御风"}    ,
    6  : {"name" : "不允许携带咒师"}    ,
    7  : {"name" : "不允许携带祝由"}    ,
    8  : {"name" : "不允许携带男性角色"},
    9  : {"name" : "不允许携带女性角色"},
    10 : {"name" : "仅允许近身战斗"}    ,
    11 : {"name" : "仅允许远程战斗"}    ,
    12 : {"name" : "不允许百分比伤害和固定伤害"}    ,
  },
}

f = open("data.json", "w")
f.write(json.dumps(main_dict, indent=4))
f.close()
