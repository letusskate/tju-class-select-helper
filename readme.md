## quick start
### 步骤一
（安装116版本chrome浏览器（2023年9月最新版本），安装python环境）

注意，如果浏览器已经迭代了许多版本，则需要查看本机chrome浏览器版本。（如果没有，请下载最新版本chrome浏览器）

另外需要下载与计算机的chrome版本对应的chrome driver，下载地址：https://chromedriver.chromium.org/downloads

并将chrome driver放置在工作区正确的位置：./chromedriver-win64/chromedriver-win64/chromedriver.exe
### 步骤二
进入项目，在终端中输入pip install -r requirements.txt，安装python相关包
### 步骤三
在qiangke中输入学号、密码、要抢的课程
### 步骤四
执行脚本qiangke.py，登陆界面输入验证码，点击黄色登录按钮，之后不要动，会自动抢课。
## 关于执行
qiangke.py是不刷新浏览器，每次失败后间隔一小段时间重新抢，抢课间隔短，容易被检测到并要求输入验证码

qiangkeshuaxin.py会在每一轮抢课后刷新浏览器，抢课间隔更长，更不容易被检测
