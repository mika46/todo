#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from cursesmenu import *
from cursesmenu.items import *
import re

import os
extm='^.*\\.'
cmtdic={extm+'f90$':'!',extm+'f$':'C','^make$|'+extm+'py$|'+extm+'sh$':'#'}
menu = CursesMenu(os.path.splitext(os.path.basename(__file__))[0], "in "+ os.path.basename(os.getcwd()))
for root, dirs, files in os.walk("."):
    for fname in files:
        for k,v in cmtdic.items():
            patern=re.compile(k,re.IGNORECASE)
            if re.match(patern,fname) is not None:
                path=os.path.join(root, fname)
                file=open(path,"r")
                for i, line in enumerate(file):
                    if line.lstrip().upper().startswith(v.upper()+'TODO:',):
                        i+=1
                        menu.append_item(CommandItem("in file " +'"'+ path + '": l n°'+ str(i) + " "+  line, "vim +"+ str(i) + " "+ path))
if len(menu.items)>0:
    menu.show()
