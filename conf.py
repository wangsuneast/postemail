#coding: utf-8

import ConfigParser
import os

PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)), "send.cnf")

cnf = ConfigParser.ConfigParser()
cnf.read(PATH)
#s = cnf.sections() #获取所有的sections,即[],["mail", "db"]
#s = cnf.items("db")
#print s
def confs(section):
    conf_dict = {}
    for option,value in cnf.items(section):
        if value.isdigit():
            conf_dict[option] = int(value)
        else:
            conf_dict[option] = value
    return conf_dict

if __name__ == "__main__":
    print confs("db")
    print confs("mail")
