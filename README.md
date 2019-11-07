完整文章请移步 [ 打造完美Python环境(pyenv, virtualenv, pip)](https://www.cnblogs.com/1lin24/p/11811231.html)

> 文章写在博客园，图片在github无法正常显示，请点击上面的原文地址进行阅读

#### 写在最前
在使用 Python 进行开发和部署的时候，经常会碰到Python版本或者依赖包或者对应版本不同导致各种意外情况发生。

本文将介绍如何通过 pyenv, virtualenv, pip三个工具来管理环境，以保证团队内部，使用的Python版本以及使用的依赖包版本都高度一至，并且有很高的移植性。

> pyenv, virtualenv, pip 的安装网上资料很多，这里不再赘述
> Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具

## 我的演示环境
```
CentOS 7.4.1708 
pyenv 1.2.14-5-g68a77df0
Python 3.6.9
pip 16.7.7
```

在实践之前，我们先快速了解几个工具的功能和基本用法
## pyenv 版本管理 
#### 1. 查看可安装的Python版本
```
pyenv install --list 
```
这个命令会列出所有pyenv收纳的所有版本
#### 2. 安装指定Python版本
```
pyenv install 3.6.9
```
从`pyenv install --list`中找到需要的版本号，使用上面的命令安装即可
> 安装过程需要花几分钟的时间

#### 3. 查看已安装的版本
```
pyenv versions
```
![](https://img2018.cnblogs.com/blog/1469514/201911/1469514-20191107140746933-1148610104.png)

#### 4. 设定当前版本
我们可以`pyenv versions`列出的版本中，选择想要的Python版本
```
pyenv global 3.6.9
pyenv local 3.6.9
```
上面两个命令都是用于设定当前的Python版本号，不同之处在于：
* pyenv global 作用于全局
* pyenv local 仅作用于当前目录

## virtualenv 虚拟环境管理
#### 1. 生成虚拟环境
```
virtualenv --no-site-packages .venv
```
这个命令会在当前目录下生成一个 .venv 文件夹，用于存放虚拟环境相关的文件。正常情况下这个目录是我们项目的根目录。

需要说明的是，要生成干净的虚拟环境一定要加上`--no-site-packages`，否则创建的虚拟环境仍然会包含系统环境下的一些依赖包。

.venv是我们的虚拟环境的名称，这里想多说一句，之所以使用在环境面前加了一个点，是在 windows 和 Linux 下以点开头的文件一般不会直接显示出来，这样在视觉会更舒服一些。

#### 2. 激活虚拟环境
```
source .venv/bin/activate
# windows 下使用 .\.venv\Scripts\activate.bat
```
创建好虚拟环境之后，还要激活才能进入到我们刚刚创建的虚拟环境

#### 3. 关闭虚拟环境
```
deactivate
```
当要在其它项目上工作前或者其它不需要当前环境时，需要用上面的命令关闭虚拟环境

## pip 依赖包管理
#### 安装依赖包
```
pip install package_name
```
只要把 package_name 替换成要安装的包名即可

#### 查看已安装的依赖包
```
pip freeze
```
![](https://img2018.cnblogs.com/blog/1469514/201911/1469514-20191107142543140-687514810.png)

#### 备份依赖包列表
```
pip freeze > requirements.txt
```
将上面的内容重定向到一个文件里面，习惯上我都把这个文件命令为`requirements.txt`

#### 批量安装依赖包
```
pip install -r requirements.txt
```
这个命令的作用在于，当我们把项目移交到别的机器时  
可以根据原来的配置安装需要的依赖包，而不会出现遗漏或者多安装的情况。

## 实战
讲了我们需要用到的几个工具的基本使用之后，我们来进行一次实战

### 1. 创建项目并进行环境管理

新建一个目录 demo_python_env,并进入到这个目录
```
~ » mkdir demo_python_env
~ » cd demo_python_env
```

创建虚拟环境
```
~/demo_python_env » virtualenv --no-site-packages .venv
Using base prefix '/home/x/.pyenv/versions/3.6.9'
New python executable in /home/x/demo_python_env/.venv/bin/python3.6
Also creating executable in /home/x/demo_python_env/.venv/bin/python
Installing setuptools, pip, wheel...
done.
```

激活虚拟环境
```
(.venv)~/demo_python_env » source .venv/bin/activate
```

安装 requests 依赖包
```
(.venv)~/demo_python_env » pip install requests
Collecting requests
Using cached https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
Using cached https://files.pythonhosted.org/packages/e0/da/55f51ea951e1b7c63a579c09dd7db825bb730ec1fe9c0180fc77bfb31448/urllib3-1.25.6-py2.py3-none-any.whl
Collecting certifi>=2017.4.17
Using cached https://files.pythonhosted.org/packages/18/b0/8146a4f8dd402f60744fa380bc73ca47303cccf8b9190fd16a827281eac2/certifi-2019.9.11-py2.py3-none-any.whl
Collecting idna<2.9,>=2.5
Using cached https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2
Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Installing collected packages: urllib3, certifi, idna, chardet, requests
Successfully installed certifi-2019.9.11 chardet-3.0.4 idna-2.8 requests-2.22.0 urllib3-1.25.6
```

保存当前的依赖包列表到 requerements.txt 中
```
(.venv)~/demo_python_env » pip freeze > requerements.txt
```

新建一个测试文件
```
(.venv)~/demo_python_env » touch test.py
```

键入以下内容，这段代码功能是向 github 发一个请求，并打印出响应状态码
```
import requests

res = requests.get('https://api.github.com/events')
print('** status_code = {} **'.format(res.status_code))
```

测试是否能正常
```
(.venv)~/demo_python_env » python test.py
** status_code = 200 **
```

关闭虚拟环境
```
~/demo_python_env » deactivate
```

### 2. 在新机器上搭建相同的项目环境
> demo我提交到github上，大家可以用于做第二步的练习 [https://github.com/1lin24/demo_python_env][3]

我们假设，同事的代码已经上传到公司的git服务器，我先将代码下载到我的机器上，并切换到这个目录中
```
~ » git clone https://github.com/1lin24/demo_python_env.git
Cloning into 'demo_python_env'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
~ » cd demo_python_env
```

查看项目文件
```
~/demo_python_env(master) » ls -la
total 24
drwxrwxr-x  3 x x 4096 Nov  7 15:44 .
drwx------ 11 x x 4096 Nov  7 15:44 ..
drwxrwxr-x  8 x x 4096 Nov  7 15:44 .git
-rw-rw-r--  1 x x 1297 Nov  7 15:44 .gitignore
-rw-rw-r--  1 x x   77 Nov  7 15:44 requerements.txt
-rw-rw-r--  1 x x  125 Nov  7 15:44 test.py
```

创建虚拟环境
```
~/demo_python_env(master) » virtualenv --no-site-packages .venv
\Using base prefix '/home/x/.pyenv/versions/3.6.9'
New python executable in /home/x/demo_python_env/.venv/bin/python3.6
Also creating executable in /home/x/demo_python_env/.venv/bin/python
Installing setuptools, pip, wheel...
done.
```

激活刚刚创建的虚拟环境
```
(.venv)~/demo_python_env(master) » source .venv/bin/activate
```

安装项目需要的依赖包
```
(.venv)~/demo_python_env(master) » pip install -r requerements.txt
Collecting certifi==2019.9.11
Using cached https://files.pythonhosted.org/packages/18/b0/8146a4f8dd402f60744fa380bc73ca47303cccf8b9190fd16a827281eac2/certifi-2019.9.11-py2.py3-none-any.whl
Collecting chardet==3.0.4
Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting idna==2.8
Using cached https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl
Collecting requests==2.22.0
Using cached https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl
Collecting urllib3==1.25.6
Using cached https://files.pythonhosted.org/packages/e0/da/55f51ea951e1b7c63a579c09dd7db825bb730ec1fe9c0180fc77bfb31448/urllib3-1.25.6-py2.py3-none-any.whl
Installing collected packages: certifi, chardet, idna, urllib3, requests
Successfully installed certifi-2019.9.11 chardet-3.0.4 idna-2.8 requests-2.22.0 urllib3-1.25.6
```

运行测试代码
```
(.venv)~/demo_python_env(master) » python test.py
** status_code = 200 **
```

关闭虚拟环境
```
~/demo_python_env(master) » deactivate
```

这是我自己使用的python环境管理方案，希望能够帮助到需要的人，如果你有更好的方案，请一定告诉我哦

## ReadMore
[pyenv 官方文档][0]
[virtualenv 官方文档][1]
[pip 官方文档][2]

> 欢迎指教，留言交流

[0]: https://github.com/pyenv/pyenv
[1]: https://virtualenv.pypa.io/en/latest/
[2]: https://pip.pypa.io/en/stable/
[3]: https://github.com/1lin24/demo_python_env

