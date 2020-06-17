from tornado_jinja2 import Jinja2Loader
import jinja2
import datetime

jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template/'), autoescape=True, extensions=['jinja2.ext.loopcontrols', 'jinja2_time.TimeExtension'])
jinja2_loader = Jinja2Loader(jinja2_env)


def datetimeformat(value, format='%d.%m.%Y %H:%M'):
    return datetime.datetime.fromtimestamp(int(value)).strftime(format)

def hoursetime(value):
    hourse = value // 3600
    min = (value - (hourse * 3600))//60
    if len(str(min)) == 1:
        min = f'0{min}'
    return f'{hourse}:{min}'

jinja2_env.filters['datetimeformat'] = datetimeformat
jinja2_env.filters['hoursetime'] = hoursetime