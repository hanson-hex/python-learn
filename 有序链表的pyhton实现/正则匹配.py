# /usr/bin/env python
# -*- coding:utf-8 -*-
import re

text = r"""
 <script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
        <script type="text/javascript" src="js/define.js"></script>
        <script type="text/javascript" src="js/lf.js"></script>
        <script type="text/javascript" src="js/getuserinfo.js"></script>
        <script type="text/javascript" src="js/createjs.min.js"></script>
        <script type="text/javascript" src="js/howler.min.js"></script>
        <script type="text/javascript" src="js/screenfull.js"></script>
        <script type="text/javascript" src="js/ctl_utils.js"></script>        
        <script type="text/javascript" src="js/sprite_lib.js"></script>
        <script type="text/javascript" src="js/settings.js"></script>
        <script type="text/javascript" src="js/CEdge.js"></script>
        <script type="text/javascript" src="js/CEdgeModel.js"></script>
        <script type="text/javascript" src="js/CEdgeViewer.js"></script>
        <script type="text/javascript" src="js/CVector2.js"></script>
        <script type="text/javascript" src="js/CVector3.js"></script>
        <script type="text/javascript" src="js/CTweenController.js"></script>
        <script type="text/javascript" src="js/CShake.js"></script>
        <script type="text/javascript" src="js/CLang.cn.js"></script>
        <script type="text/javascript" src="js/CPreloader.js"></script>
        <script type="text/javascript" src="js/CMain.js"></script>
        <script type="text/javascript" src="js/CMenu.js"></script>
        <script type="text/javascript" src="js/CGame.js"></script>        
        <script type="text/javascript" src="js/CBall.js"></script>
        <script type="text/javascript" src="js/CBonus.js"></script>
        <script type="text/javascript" src="js/CBoard.js"></script>
        <script type="text/javascript" src="js/CToggle.js"></script>
        <script type="text/javascript" src="js/CGfxButton.js"></script>
        <script type="text/javascript" src="js/CTextButton.js"></script>
        <script type="text/javascript" src="js/CInterface.js"></script>
        <script type="text/javascript" src="js/CCreditsPanel.js"></script>        
        <script type="text/javascript" src="js/CAreYouSurePanel.js"></script>
        <script type="text/javascript" src="js/CHelpPanel.js"></script>
        <script type="text/javascript" src="js/CEndPanel.js"></script>
        <script type="text/javascript" src="js/CMsgBox.js"></script>
"""

pattern = re.compile(r'.*src="(.*)"')
# pattern = re.compile(r'.*\((.*)\)')
print(pattern.findall(text))
# res = pattern.findall(text)
# list = []
# for i in res:
#     i = i.replace(',', ':')
#     # i = i.replace('', '')
#     list.append(i)
#     print(i)
# print(list)
