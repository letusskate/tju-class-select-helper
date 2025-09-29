## 天津大学tju抢课爬虫（余容监控+辅助秒杀）
本项目基于python selenium进行天津大学教务系统的抢课爬虫设计，你是否还在为抢不到课（信息检索与利用，积极心理学）而感到苦恼，请试试吧。

适用于有一定编程经验的同学，尽量曾经尝试过编写python。


https://github.com/user-attachments/assets/33677087-3a9d-45c7-94e4-ee2726cea294


（免责声明，本项目是以学习python为目标编写的，本人是一名研究生，并未将此项目用于真实抢课中，希望使用者也不要为了满足一己私利用这个脚本抢课！！！！！）

## quick start
### 步骤一
安装最新版本chrome浏览器，安装一个版本的python解释器，比如python 3.9

查看当前的chrome浏览器版本号，方法为：打开chrome---点击右上角三个点---进入帮助子选项卡---点击关于google chrome。（或者进入chrome设置页面，点击关于chrome）

下载与计算机的chrome版本号一致的chrome driver，下载地址：https://chromedriver.chromium.org/downloads ||| 20250929注：如果chrome版本高于114，则下载地址为：https://googlechromelabs.github.io/chrome-for-testing/

并将chrome driver放置在工作区正确的位置：./chromedriver-win64/chromedriver-win64/chromedriver.exe
### 步骤二
进入项目，在终端中输入pip install -r requirements.txt，安装python相关包
### 步骤三
在qiangke.py中输入学号、密码、要抢的课程
### 步骤四
执行脚本qiangke.py，登陆界面输入验证码，点击黄色登录按钮，之后不要动，会自动抢课。

## 关于执行
qiangke.py是不刷新浏览器，每次失败后间隔一小段时间重新抢，抢课间隔短，容易被检测到并要求输入验证码

qiangkeshuaxin.py会在每一轮抢课后刷新浏览器，抢课间隔更长，更不容易被检测
