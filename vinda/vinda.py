# -*- coding:utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def format_size(raw_size):
    if raw_size < 1024:
        return '{} B'.format(raw_size)
    elif raw_size < 1024 ** 2:
        return '{} KB'.format(raw_size / 1024)
    elif raw_size < 1024 ** 3:
        return '{} MB'.format(raw_size / (1024 ** 2))
    elif raw_size < 1024 ** 4:
        return '{} GB'.format(raw_size / (1024 ** 3))
    else:
        return 'lagrer than 1TB'


def look(root_path='.', output_path='vinda.html', ignore_list=[]):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    template = env.get_template('template.html')
    
    link = []
    for name in os.listdir(root_path):
        full_path = os.path.join(root_path, name)
        print 'vinda is dealing', full_path

        if name not in ignore_list and os.path.isdir(full_path):
            link.append({'href': name + '/', 'name': name})
        if name not in ignore_list and os.path.isfile(full_path):
            link.append({'href': name, 'name': name})

    with open(output_path, mode='w') as f:
        f.write(template.render(link=link))
