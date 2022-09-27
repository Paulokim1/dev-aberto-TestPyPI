from dev_aberto import hello
from datetime import date 
from dateutil import parser
from babel.dates import format_datetime
import gettext 

gettext.install('cli', localedir='./locale') 

if __name__ == '__main__':
    date, name = hello()
    f_date = format_datetime(parser.parse(date), 'full')
    last_commit_str = _('Last commit made at: ')
    by_str = _('by')
    print(last_commit_str + f_date + by_str + name)