# -*- coding:utf-8 -*-
import os
import codecs
from jinja2 import Environment, FileSystemLoader


def look(path='.', deep_limit=3, ignore=[]):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__))))
    template = env.get_template('template.html')
    
    link = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        print 'vinda ->', full_path
        if name not in ignore and os.path.isdir(full_path):
            link.append({'href': name.decode('utf-8'), 'name': name.decode('utf-8')})
            if deep_limit > 0:
                look(path=full_path, deep_limit=deep_limit - 1, ignore=ignore)
        if name not in ignore and os.path.isfile(full_path):
            link.append({'href': name.decode('utf-8'), 'name': name.decode('utf-8')})

    if link:
        with open(path + '/index.html', mode='w') as f:
            f.write(template.render(link=link).encode('utf-8'))
