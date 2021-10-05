# -*- coding: utf-8 -*-
import sys
import json


def port_node_to_dict(port):
  ret = {}

  name_node = search_text_parent(port, u'名前')
  s = search_long_text(name_node, 8)
  ret['name'] = s

  explain_node   = search_text_parent(port, u'説明')
  ret['explain'] = search_long_text(explain_node, 8)

  location = search_float_pair(port)
  ret['latitude']  = location[0]
  ret['longitude'] = location[1]

  return ret


def search_threshold(node, threshold):
  ret = node
  for p in node:
    if not isinstance(p, list):
      continue
    if json.dumps(p).count('[') < threshold :
      continue
    ret = search_threshold(p, threshold)

  return ret


def search_text_parent(node, text):
  for p in node:

    if isinstance(p, list):
      tmp = search_text_parent(p, text)
      if tmp is not None:
        return tmp

    if isinstance(p, str):
      if p == text:
        return node

  return None


def search_long_text(node, min_len):
  for p in node:

    if isinstance(p, list):
      tmp = search_long_text(p, min_len)
      if tmp is not None:
        return tmp

    if isinstance(p, str):
      if len(p) > min_len:
        return p

  return None


def search_float_pair(node):
  for p in node:

    if not isinstance(p, list):
      continue

    if isinstance(p, list):
      if len(p) == 2:
        if isinstance(p[0], float) and isinstance(p[1], float):
          return p
      tmp = search_float_pair(p)
      if tmp is not None:
        return tmp

  return None
