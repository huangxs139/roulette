import json
import time
import random

fb_list = []
stone_list_physical = [ "荒蛰", "头狼", "幽魉", "罗鬼" ]
stone_list_magical =  [ "九环朱蝮", "朱焰魔火", "妖术师", "百眼翼魔"]
stone_list_other =    [ "凶骸兵", "赤练鬼", "刚破鬼", "咒石兵", "死魇鬼卒", "冰魔蝎", "鬼面花蛛", "尸魔术士", "冥葵"]

class Entry:
  def __init__(self, name="", num=()):
    self._name = name
    self._num = num 

  def name(self):
    return self._name

  def num(self):
    return self._num

  def output(self, num, stone=set()):
    if len(stone) > 0:
      print(self._name.format(self._num[num], stone))
    else:
      print(self._name.format(self._num[num]))

def init(): 
  fb_list.append(Entry("禁用{}及以上位绝英灵",   (1, 2, 3, 4)))               #0
  fb_list.append(Entry("禁用{}及以上位极英灵",   (1, 2, 3, 4)))               #1
  fb_list.append(Entry("禁用{}及以上个绝饰品",   (1, 2, 3, 4, 5, 6, 7, 8)))   #2
  fb_list.append(Entry("禁用{}及以上个极饰品",   (1, 2, 3, 4, 5, 6, 7, 8)))   #3
  fb_list.append(Entry("禁用{}及以上套指定的物理魂石，包括：{}", (1, 2, 3)))  #4
  fb_list.append(Entry("禁用{}及以上套指定的法术魂石，包括：{}", (1, 2, 3)))  #5
  fb_list.append(Entry("禁用{}及以上套指定的其他魂石，包括：{}", (1, 2, 3)))  #6

def main():
  random.seed(time.time())
  main_set = set()
  while len(main_set) < 2:
    fb_no = random.randint(0, len(fb_list)-1)
    main_set.add(fb_no)
  for fb_no in main_set:
    entry = fb_list[fb_no]
    x = random.randint(0, len(entry.num())-1)
    if fb_no > 3:
      stone_set = set()
      stone_list = []
      if fb_no == 4:
        stone_list = stone_list_physical
      elif fb_no == 5:
        stone_list = stone_list_magical
      else:
        stone_list = stone_list_other

      while len(stone_set) < x+1:
        index = random.randint(0, len(stone_list)-1)
        stone_set.add(stone_list[index])

      entry.output(x, stone_set)
    else:
      entry.output(x)

if __name__ == '__main__':
  init()
  main()
