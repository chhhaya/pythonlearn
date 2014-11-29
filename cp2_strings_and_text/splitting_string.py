# coding:utf8

### 切分字符串
import re
line = 'asf asdf; xxx, asdf,sfd, aaa,   i; jjj'
# 可自定义分割字符
print(re.split(r'[\s;,]\s*', line))
# ['asf', 'asdf', 'xxx', 'asdf', 'sfd', 'aaa', 'i', 'jjj']

# 要注意括号为捕获组
print(re.split(r'(\s|;|,)\s*', line))
# ['asf', ' ', 'asdf', ';', 'xxx', ',', 'asdf', ',', 'sfd', ',', 'aaa', ',', 'i', ';', 'jjj']

# 加?:变成非捕获组
print(re.split(r'(?:\s|;|,)\s*', line))

### startswith和endswith多个选择
# 一个的情况：
filename = "spam.txt"
_ = filename.endswith(".txt")
print(_)
# 多个的情况：
import os
filenames = os.listdir('/Users/alpha/Downloads/setups/wget-1.16/src')
# 选出所有.c和.h的文件
print([name for name in filenames if name.endswith(('.c', '.h'))])
# 是否有文件是.c
print(any(name.endswith('.c') for name in filenames))
# 必须要是tuple
line.startswith(tuple(['.c', '.h']))


### 使用shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
print(fnmatchcase('foo.txt', '*.TXT'))  # 区分大小写

### 匹配和搜索
# 简单的使用 ==, str.find(), str.endswith(), str.startswith()
# 复杂的用re
text1 = '11/24/2012'
text2 = 'Nov 23, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# 预编译方法
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.match(text1))  # obj
print(datepat.match(text2))  # None

# 搜索所有的
text = 'today is 11/24/2012, tomorrow is 12/24/2012'
print(datepat.findall(text))  # [item1, item2]

# 一个的时候捕获组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match(text1)
print(m.group(0))  # 11/24/2012
print(m.group(1))  # 11
print(m.groups())  # ('11', '24', '2012')

# 多个的时候捕获组
print(datepat.findall(text))  # [('11', '24', '2012'), ('12', '24', '2012')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(month, day, year))

# match 是从头开始搜的，要匹配整个可以用
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')


### 搜索和替换
# 简单的可用str.replace()
# 复杂的用re.sub()
print(text)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# today is 11/24/2012, tomorrow is 12/24/2012
# today is 2012-11-24, tomorrow is 2012-12-24

# 使用预编译
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# 使用callback处理更复杂情况
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]  # 数字的月转为字母的月
    return '{} {} {}'.format(m.group(3), mon_name, m.group(2))
print(datepat.sub(change_date, text))
# today is 2012 Nov 24, tomorrow is 2012 Dec 24

# 获得替换个数
newtext, n = datepat.subn(change_date, text)
print(newtext)
print(n)


### 忽略大小写搜索
#re.findall(datepat, text, flags=re.IGNORECASE)
#re.sub(datepat, text, flags=re.IGNORECASE)

# 如果替换的时候要保持原来的大小写
text = 'UPPER PYTHON, lowser python, Mixed Python'
def matchcase(word):
    def replace(m):
        text = m.group()
        print('{}-{}'.format(word, text))
        if text.islower():
            return word.lower()
        elif text.isupper():
            return word.upper()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

### 最短匹配, 在+或*后面加?
text1 = '"yes" or "no".'
str_pat = re.compile(r'\"(.*)\"')
print(str_pat.findall(text1))
# ['yes" or "no']
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text1))
# ['yes', 'no']

### 多行匹配
# .不匹配换行
# 法1，正则里加\n支持 (推荐)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
text2 = """/* this is a
    multiline comment*/"""
print(comment.findall(text2))

# 法2，用DOTALL flag
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))


# 标准化unicode文本
# 相同的字符串用不同的代码表达
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
# Spicy Jalapeño
# Spicy Jalapeño
# False
import unicodedata
# NFC 表示字符尽量用简单code构成
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(ascii(t1))
# 'Spicy Jalape\xf1o'
print(t1 == t2)
# True

# NFD 表示字符尽量用组合code构成
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(ascii(t1))
# 'Spicy Jalapen\u0303o'
print(t1 == t2)
# True

# 用来过滤掉可区别的mark
# combining() 用来测试是否是个结合字符
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
# Spicy Jalapeno


### 正则匹配处理unicode字符 （推荐regex库）
# 匹配阿拉伯字符
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0\u08ff]')

# 匹配前最好先让所有的文本都标准化
# 也要注意特殊例子
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print('stra\u00dfe')
print(pat.match(s))  # match
print(pat.match(s.upper()))  # None
print(s.upper())  # STRASSE

### 去掉不想要的字符
# 用str.strip(), lstrip(), rstrip()
# 文件中读出来去掉前后空白
# with open(filename) as fp:
#     lines = (line.strip() for line in fp)  # efficient！
#     for line in lines:
#         ....
# 更高级用translate


### 审查和clean up 文本
s = 'python\fis\tawesome\r\n'
# 先去掉空白
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # delete
}
a = s.translate(remap)
print(a)
# python is awesome
# 再去掉其他组合字符
# import sys
# cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
# b = unicodedata.normalize('NFD', a)
# b.translate(cmb_chrs)
# 通过fromkeys，把那些音标都过滤为None， 就去掉了那些音标

# 把所有的unicode十进制数字转为对应的ASCII
# digitmap = {c: ord('0') + unicodedata.digit(chr(c))
#             for c in range(sys.maxunicode)
#             if unicodedata.category(chr(c)) == 'Nd'}
# print(len(digitmap))  # 460
# x = '\u0661\u0662\u0663'
# print(x.translate(digitmap))
# 123

# 从性能上来说str.replace()是最快的。


### 校准文本字符串
# 简单的用ljust, rjust, center
text = 'Hello world'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
# Hello world
#          Hello world
#     Hello world

# 可指定填充字符
print(text.rjust(20, '*'))
# *********Hello world

# format
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
# Hello world
#          Hello world
#     Hello world

# 带填充的format
print(format(text, '=>20s'))
# =========Hello world

# format处理多个值
print('{:>10s} {:>10s}'.format('Hello', 'world'))
#      Hello      world

# 对于数字
x = 1234.5
print(format(x, '>10'))
print(format(x, '^10.2f'))
#     1234.5
#  1234.50

# % 是老方法了， 推荐用format


### 连接字符串
# 一般用str.join(list)
# 用+连接很多字符串是很耗性能的，因为每次 += 操作都会生成一个新的字符串对象，要用join来替换
a = 'a'
b = 'b'
c = 'c'
print(a + ':' + b + ':' + c)  # 丑
print(':'.join([a, b, c]))  # 丑
print(a, b, c, sep=':')  # 好

# 下面的例子是优雅得将一大串字符串写到文件中
# generator object
def sample():
    yield 'Is'
    yield 'Chicage'
    yield 'Not'
    yield 'Chicage?'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)
f = open('temp.txt', 'w')
for part in combine(sample(), 32767):
    f.write(part)


### 字符串中插入变量
s = '{name} has {n} messages'
print(s.format(name='guido', n=37))

# 这都可以
name = 'Guido'
n = 37
s = '{name} has {n} messages'
print(s.format_map(vars()))
# 'Guido has 37 messages’

# 也可以在实例中
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido', 37)
s.format_map(vars(a))

# 有个缺点是如果不给n的话会出错
# 解决方法：
# >>> del n
# >>> class safesub(dict):
#     def __missing__(self, key):
#         return '{' + key + '}'
# >>> s.format_map(safesub(vars()))
# 'Guido has {n} messages'

# sys._getframe()是获得调用栈帧，0 是当前，1 是上层
# f_locals是当前的变量字典
import sys
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
print(sub('hello {name}'))
print(sub('you have {n} message'))
print(sub('color is {color}'))
# hello Guido
# you have 37 message
# color is {color}
def test(txt):
    print(sys._getframe(0).f_locals)
test('xx')
# {'txt': 'xx'}


### 格式化文本为固定列
s = "ADAudit Plus is a web based Windows Active Directory Change " \
    "Reporting Software that audits-tracks-reports on Windows - Active Directory," \
    " Workstations Logon / Logoff, File Servers & Servers to help meet the most" \
    "-needed security, audit and compliance demands."
import textwrap
# 70列输出
print(textwrap.fill(s, 70))
# 首行缩进
print(textwrap.fill(s, 40, initial_indent='     '))
# 后面行缩进
print(textwrap.fill(s, 40, subsequent_indent='      '))
import os
#os.get_terminal_size().columns
#  输出控制台列数


### 处理HTML和XML实体
s = 'as "<tag>text</tag>'
import html
print(s)
print(html.escape(s))
# as "<tag>text</tag>
# as &quot;&lt;tag&gt;text&lt;/tag&gt;
# 不escape引号
print(html.escape(s, quote=False))
# as "&lt;tag&gt;text&lt;/tag&gt;

# 把文本转为ascii，把非ascii字符变成实体
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
# b'Spicy Jalape&#241;o'

# 实体转为字符
# 法1
s = 'Spicy &quot;Jalape&#241;o&quot;'
print(html.unescape(s))
# Spicy "Jalapeño"
# 法2
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
# The prompt is >>>


# 标记化文本
text = ' foo = 23 + 42 * 10'
# 要标记成：
tokens = [('NAME', 'foo')]
# 用带名称的捕获组
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# scanner 会生成一个scanner对象，该对象重复调用match
# >>> scanner = mp.scanner('foo = 42')
# >>> scanner.match()
# <_sre.SRE_Match object; span=(0, 3), match='foo'>
# >>> _.lastgroup, _.group()
# ('NAME', 'foo')
# >>> scanner.match()
# <_sre.SRE_Match object; span=(3, 4), match=' '>
# >>> _.lastgroup, _.group()
# ('WS', ' ')
# >>> scanner.match()
# <_sre.SRE_Match object; span=(4, 5), match='='>
# >>> _.lastgroup, _.group()
# ('EQ', '=')
# >>> scanner.match()
# <_sre.SRE_Match object; span=(5, 6), match=' '>
# >>> _.lastgroup, _.group()
# ('WS', ' ')
# >>> scanner.match()
# <_sre.SRE_Match object; span=(6, 8), match='42'>
# >>> _.lastgroup, _.group()
# ('NUM', '42')
# >>> scanner.match()

from collections import namedtuple
Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
print('no whitespace'.center(30, '-'))
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
    