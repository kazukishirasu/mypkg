# **ロボットシステム学HW2**  
- 講義で作成したROSのパッケージを改造して数あてゲームを作成した。  
***
## **使用する道具**  
- Raspberry Pi 4 model B  
***
## **環境**  
- Ubuntu 20.04 LTS  
***
## **インストール方法**  
- 以下のコマンドを上から順に実行する。  
```  
$ cd catkin_ws/src  
$ git clone https://github.com/kazukishirasu/mypkg.git  
$ cd ..
$ catkin_make  
```  
## **実行方法**  
```  
$ roslaunch mypkg mypkg.launch  
```  
## **実行動画**
- [数あてゲーム](https://youtu.be/pemWFB9xaKI)
## **ライセンス**  
- [BSD 3-Clause "New" or "Revised" License](https://github.com/kazukishirasu/mypkg/blob/master/COPYING)  
