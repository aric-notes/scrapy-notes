# pip/pip3
- https://cloud.tencent.com/developer/article/1416214


### 问题描述
~~~
在 zsh 中执行 pip xxx ，出现错误 zsh: command not found: pip3 。 当然我很确定自己是有安装 pip3 的,应该是应该切换了shell，导致环境变量出了问题。

解决方案
我后来在 issue 3565 上找到了解决方案：https://github.com/pypa/pip/issues/3565

先执行 sudo apt-get install --reinstall python3-pip

之所以reinstall是因为虽然安装了,但是可能某些文件等之类的缘故,–reinstall 将会重写所有的文件覆盖这个包。

查看是否安装成功 pip3 -V

搞定 pip3 过后,再回头升级 pip 即可。

再执行 pip3 install --upgrade pip

接着 pip --version 即可。

~~~
