以下是 Django 开发中一些常用的终端指令总结：

### 项目创建与管理
#### 1. 创建 Django 项目
```bash
django-admin startproject project_name
```
此指令用于创建一个新的 Django 项目，`project_name` 需替换为你实际的项目名称。

#### 2. 创建 Django 应用
```bash
python manage.py startapp app_name
```
在项目目录下使用该指令可创建一个新的 Django 应用，`app_name` 要替换成你应用的实际名称。
创建完成记得在settings.py 添加对应配置
INSTALLED_APPS = [
    # ...
    'app_name',
]

```bash
python manage.py startapp app04 apps/app04
```
在APP下创建多个APP

#### 3. 运行开发服务器
```bash
python manage.py runserver
```
默认情况下，服务器会在 `http://127.0.0.1:8000/` 启动。若要指定端口，可以使用如下指令：
```bash
python manage.py runserver 8080
```
这里将端口指定为 8080。

### 数据库操作
#### 1. 创建数据库迁移文件
```bash
python manage.py makemigrations
```
该指令会依据模型的变化生成数据库迁移文件。

#### 2. 执行数据库迁移
```bash
python manage.py migrate
```
此指令会将生成的迁移文件应用到数据库中，从而更新数据库结构。

#### 3. 查看未应用的迁移
```bash
python manage.py showmigrations
```
它能显示出哪些迁移文件已经应用，哪些还未应用。

#### 4. 清空数据库的命令
```bash
python manage.py flush
```
通过 manage.py 执行 flush 命令来清空数据库的内容。flush 命令将删除数据库中的所有数据，但保留数据库结构和模型。

### 用户与权限管理
#### 1. 创建超级用户
```bash
python manage.py createsuperuser
```
运行此指令后，根据提示输入用户名、邮箱和密码，就可以创建一个超级用户，用于登录 Django 管理界面。

### 静态文件管理
#### 1. 收集静态文件
```bash
python manage.py collectstatic
```
在生产环境中，该指令会把项目中的静态文件（如 CSS、JavaScript、图片等）收集到一个指定的目录，方便部署。

### 测试相关
#### 1. 运行测试
```bash
python manage.py test
```
它会运行项目中的所有测试用例，你也可以指定具体的应用来运行测试：
```bash
python manage.py test app_name
```

### 其他
#### 1. 启动 Django shell
```bash
python manage.py shell
```
该指令会启动一个 Python shell，并且已经加载了 Django 环境，你可以在其中进行模型操作、测试代码等。

#### 2. 生成项目依赖文件
```bash
pip freeze > requirements.txt
```
此指令会把当前项目所依赖的 Python 包及其版本信息保存到 `requirements.txt` 文件中，方便在其他环境中进行部署。在新环境中安装依赖时，可以使用：
```bash
pip install -r requirements.txt
``` 



