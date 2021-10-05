# -*- coding: utf-8 -*-
import sys
import json
from module.lib_google_map_parse import *

def main(args):
  f = open(args[0], 'r')
  data = json.load(f)
  f.close()

  all_node_count = json.dumps(data).count('[')
  threshold = int(all_node_count/2)
  all_port = search_threshold(data, threshold)

  result = []
  for port in all_port:
    port_dict = port_node_to_dict(port)
    name_dict = parse_name(port_dict.pop('name'))
    result.append(dict(name_dict, **port_dict))

  print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))


def parse_name(s):
  ret = {}
  state = ''
  if s[0] == u'【':
    state = s.split(u'】')[0][1:]
    s = ''.join(s.split(u'】')[1:])
  ret['state'] = state

  symbol = s.split('.')[0]
  s = ''.join(s.split('.')[1:])
  ret['symbol'] = symbol

  name_ja = s.split('/')[0].strip()
  name_en = ''.join(s.split('/')[1:]).strip()
  ret['name_ja'] = name_ja
  ret['name_en'] = name_en

  return ret


if __name__ == '__main__':
  main(sys.argv[1:])

