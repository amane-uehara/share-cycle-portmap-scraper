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
    result.append(port_node_to_dict(port))

  print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))


if __name__ == '__main__':
  main(sys.argv[1:])

