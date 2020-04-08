# anime_face_detection
Anime face labeling tools

# 关于
动漫人脸数据集标注，可用于未来训练模型。  
可以选择自己喜欢的任意动画，以及里面的任意人物（最好露脸比较多）  
参与标注的人都可以分享数据集，也选择是否完全公开。

# 重要！！！选择动画之前请参考是否已经有人做了该动画
已参与动画列表：https://docs.qq.com/sheet/DSG9sT01NZ2l6VGx1?c=B9A0A0  
万恶的防火墙，不能用google sheet。这个链接里的内容需要微信/qq登录才能编辑。  
如果列表里没有，请登记后再继续，以免后续别人重复工作  

## 要求python包
1，python3  
2，opencv-python  
3，progressbar2  
两个包都可以用pip直接安装

## 文件描述
1，.xml文件为动画人脸识别模型，感谢nagadomi提供的模型：https://github.com/nagadomi/lbpcascade_animeface  
2，python脚本  

## 使用方法：
### Step1
下载文件  
请将两个文件放进同一个文件夹内，再将包含所有动画视频的文件夹（所有视频必须直接存在该文件夹下）一并放入。
### Step2
以动画文件夹名称为参数传入python脚本运行即可。  
例如存放动画的文件夹名称为anime，则：  
`python extract.py anime`  
对于一季12集动画，该脚本运行时间约为1小时，根据动画时长，人脸数目不同而可能有所不同。  
### Step3
脚本运行结束后会输出一个以动画文件夹名称命名的.zip文件，请传入iphone或ipad中任意目录下
### Step4
下载shortcuts到iphone或ipad上：https://www.icloud.com/shortcuts/5a7bec47c7f24a4e8ecac9f57d8bc1b7  
为了方便使用建议在iphone/ipad桌面上建立快捷方式
### Step5
打开shortcuts选择zip文件即可。
### Step6
其余操作请参考shortcuts说明

有问题请联系：wsjyhaozi1@gmail.com
