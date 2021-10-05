#!/bin/sh

eval curl "$1" \
  | egrep '^ *var  *_pageData *=' \
  | sed -e 's/^ *var  *_pageData *=[^"]*"//' \
  | sed -e 's@" *;</script><script type=.*$@@' \
  | sed -e 's@\\"@"@g' \
  | sed -e 's@\\\\@\\@g'
