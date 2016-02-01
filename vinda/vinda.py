# -*- coding:utf-8 -*-
import os
import jinjia2


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


def look(path='.', ignore=[], output='vinda.html'):
    ignore = set(ignore)
    ignore.add('.')
    ignore.add('..')
    if isinstance(output, str) or isinstance(output, unicode):
        head = '<head><meta charset="utf-8"></head>'
        link_tag = '<a href="{href}">{name}</a>'
        content = []
        with open(output, mode='w') as f:
            for name in os.listdir(path):
                full_path = os.path.join(path, name)
                print 'dealing', full_path
                if name not in ignore and os.path.isdir(full_path):
                    raw_size = get_size(full_path)
                    content.append(link_tag.format(
                        href=name + '/',
                        name=name,
                        size=format_size(raw_size)
                    ))
                if name not in ignore and os.path.isfile(full_path):
                    raw_size = os.path.getsize(full_path)
                    content.append(link_tag.format(
                        href=name,
                        name=name,
                        size=format_size(raw_size)
                    ))
            f.write(head + '<br>'.join(content))
    else:
        pass