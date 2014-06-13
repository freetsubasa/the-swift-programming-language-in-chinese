#!/usr/bin/python
# coding:utf-8


import os


def iter(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            if fn.endswith(".html"):
                with open(root + '/' + fn, 'r') as f:
                    content = f.read()
                content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/ace.js"></script>', '<script src="http://cdn.bootcss.com/ace/1.1.3/ace.js"></script>').replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/mode-javascript.js"></script>', '<script src="http://cdn.bootcss.com/ace/1.1.3/mode-javascript.js"></script>')
                insert_pos = content.find("</li>", content.find("Generated using GitBook")) + 6
                content = content[:insert_pos] + '''<li> <iframe src="http://ghbtns.com/github-btn.html?user=ncunos&repo=the-swift-programming-language-in-chinese&type=watch&count=true" allowtransparency="true" frameborder="0" scrolling="0" width="150" height="20"></iframe></li>''' + content[insert_pos:]
                content.replace(r'<title>.*?</title>', "<title>《The Swift Programming Language》臺灣繁體中文版</title>")
                with open(root + '/' + fn, 'w') as f:
                    f.write(content)

iter(os.getcwd())
