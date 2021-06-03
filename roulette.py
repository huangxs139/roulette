import json
import time
import random

main_dict = {}

def gen(cur_dict, num):
  c1 = random.sample( range( len(cur_dict) ), num )
  c1.sort()
  for index in c1:
    line = cur_dict[str(index)]
    if 'range' in line.keys():
      x = random.choice(line['range'])
      if 'candidate' in line.keys():
        y = random.sample( range( len(line['candidate']) ), x )
        y.sort()
        for z in range(len(y)):
          y[z] = line['candidate'][y[z]]
      else:
        y = None
      if y is None:
        print(line["name"].format(x))
      else:
        print(line["name"].format(x, y))
    else:
      print(line["name"])


def init():
  f = open("data.json", "r")
  global main_dict
  main_dict = json.loads(f.read())
  f.close()

def main():
  init()
  result = []
  result.append(gen(main_dict['forbidden_list'], 2))
  result.append(gen(main_dict['limited_list'], 2))
  result.append(gen(main_dict['adding_list'], 3))

if __name__ == "__main__":
  main()
