### 概述
本笔记是基于[追梦人物的博客](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/)以及Youtube上大神 [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) 的视频：[Python Django Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1) 整理而来。

### 准备工作

1. 安装python3（3.7）
2. 安装MySQL
3. 安装virtualenv，创建虚拟环境：

```shell
pip install virtualenv
mkdir project
cd project
virtualenv venv
# 进入虚拟环境
./venv/Scripts/activate
# 退出虚拟环境
./venv/Scripts/deactivate
```

> linux中激活虚拟环境为`source venv/bin/activate`  

3. 安装Django，创建项目：

```shell
# 在虚拟环境中
pip install -U pip
pip install django
django-admin --version
django-admin startproject django_project ./django_project
# 启动服务器
cd django_project
python manage.py runserver
```

> 上面命令中第5行最后的`.`表示在当前路径下创建。启动项目后，浏览器登陆172.0.1.0:8000，访问服务。Ctrl+c，停止服务。  

4. 设置语言时区：

修改`django_project/settiongs.py`

```python
# 此处省略上面的内容

# 设置语言代码
LANGUAGE_CODE = 'zh-hans'
# 设置时区
TIME_ZONE = 'Asia/Shanghai'

# 此处省略下面的内容
```

### 创建应用

1. 创建应用

```shell
python manage.py startapp blog
```

2. 注册到设置中

在`django_project/django_project/setting.py`文件中`INSTALLED_APPS`设置项中添加`blog`应用。

### 绑定URL与视图函数

1. 编写视图函数

在`blog`应用下创建`views.py`视图函数

```python
blog/views.py
 
from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Hello world！")
```

2. 绑定URL

在`blog`应用下创建`urls.py`

```python
from django.urls import path
 
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
]
```

3. 配置URL

修改`django_project/django_project/urls.py`文件

```python
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

4. 结果显示

运行服务器后，浏览器打开` http://127.0.0.1:8000/blog`，就可以看到'Hello world!'了。

### 配置数据库

1. 设置数据库

修改`django_project/django_project/setting.py`文件中`DATABASES`设置项。数据库的默认设置为sqlite3数据库。

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_project',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
    }
}
```

2. 安装MySQL依赖库

```shell
pip install pymysql
```

```
如果使用Python 3需要修改`django_project/django_project/__init__.py`文件并加入如下所示的代码，这段代码的作用是将PyMySQL视为MySQLdb来使用，从而避免Django找不到连接MySQL的客户端工具而询问你：“Did you install mysqlclient? ”（你安装了mysqlclient吗？）。 
```

```python
import pymysql
pymysql.install_as_MySQLdb()
```

3. 在MySQL中创建项目数据库

```mysql
create database django_project default charset utf8;
```

4. 迁移django自带数据模型到数据库

```shell
python manage.py migrate
```

### 创建数据模型

1. 编写数据模型

在blog文件夹中创建`models.py`

```python
from django.db import models
from django.contrib.auth.models import User
 
 
class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)
 
 
class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)
 
 
class Post(models.Model):
    """文章"""
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

> `django.contrib.auth`是 django 内置的应用，专门用于处理网站用户的注册、登录等流程。其中 `User` 是 django 为我们已经写好的用户模型 。  

2. 生成迁移文件

```shell
python manage.py makemigrations
```

3. 迁移到数据库

```shell
python manage.py migrate
```

> 可以运行下面的命令看看 django 究竟做了什么：  
```shell
python manage.py sqlmigrate blog 0001
```

### 模型定义参考

#### 字段
对字段名称的限制

* 字段名不能是Python的保留字，否则会导致语法错误
* 字段名不能有多个连续下划线，否则影响ORM查询操作

Django模型字段类

| 字段类                | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| AutoField             | 自增ID字段                                                   |
| BigIntegerField       | 64位有符号整数                                               |
| BinaryField           | 存储二进制数据的字段，对应Python的bytes类型                  |
| BooleanField          | 存储True或False                                              |
| CharField             | 长度较小的字符串                                             |
| DateField             | 存储日期，有auto_now和auto_now_add属性                       |
| DateTimeField         | 存储日期和日期，两个附加属性同上                             |
| DecimalField          | 存储固定精度小数，有max_digits（有效位数）和decimal_places（小数点后面）两个必要的参数 |
| DurationField         | 存储时间跨度                                                 |
| EmailField            | 与CharField相同，可以用EmailValidator验证                    |
| FileField             | 文件上传字段                                                 |
| FloatField            | 存储浮点数                                                   |
| ImageField            | 其他同FileFiled，要验证上传的是不是有效图像                  |
| IntegerField          | 存储32位有符号整数。                                         |
| GenericIPAddressField | 存储IPv4或IPv6地址                                           |
| NullBooleanField      | 存储True、False或null值                                      |
| PositiveIntegerField  | 存储无符号整数（只能存储正数）                               |
| SlugField             | 存储slug（简短标注）                                         |
| SmallIntegerField     | 存储16位有符号整数                                           |
| TextField             | 存储数据量较大的文本                                         |
| TimeField             | 存储时间                                                     |
| URLField              | 存储URL的CharField                                           |
| UUIDField             | 存储全局唯一标识符                                           |

#### 字段属性
通用字段属性

| 选项           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| null           | 数据库中对应的字段是否允许为NULL，默认为False                |
| blank          | 后台模型管理验证数据时，是否允许为NULL，默认为False          |
| choices        | 设定字段的选项，各元组中的第一个值是设置在模型上的值，第二值是人类可读的值 |
| db_column      | 字段对应到数据库表中的列名，未指定时直接使用字段的名称       |
| db_index       | 设置为True时将在该字段创建索引                               |
| db_tablespace  | 为有索引的字段设置使用的表空间，默认为DEFAULT_INDEX_TABLESPACE |
| default        | 字段的默认值                                                 |
| editable       | 字段在后台模型管理或ModelForm中是否显示，默认为True          |
| error_messages | 设定字段抛出异常时的默认消息的字典，其中的键包括null、blank、invalid、invalid_choice、unique和unique_for_date |
| help_text      | 表单小组件旁边显示的额外的帮助文本。                         |
| primary_key    | 将字段指定为模型的主键，未指定时会自动添加AutoField用于主键，只读。 |
| unique         | 设置为True时，表中字段的值必须是唯一的                       |
| verbose_name   | 字段在后台模型管理显示的名称，未指定时使用字段的名称         |

ForeignKey属性

1. limit_choices_to：值是一个Q对象或返回一个Q对象，用于限制后台显示哪些对象。
2. related_name：用于获取关联对象的关联管理器对象（反向查询），如果不允许反向，该属性应该被设置为`'+'`，或者以`'+'`结尾。
3. to_field：指定关联的字段，默认关联对象的主键字段。
4. db_constraint：是否为外键创建约束，默认值为True。
5. on_delete：外键关联的对象被删除时对应的动作，可取的值包括django.db.models中定义的：
	* CASCADE：级联删除。
	* PROTECT：抛出ProtectedError异常，阻止删除引用的对象。
	* SET_NULL：把外键设置为null，当null属性被设置为True时才能这么做。
	* SET_DEFAULT：把外键设置为默认值，提供了默认值才能这么做。

ManyToManyField属性

1. symmetrical：是否建立对称的多对多关系。
2. through：指定维持多对多关系的中间表的Django模型。
3. throughfields：定义了中间模型时可以指定建立多对多关系的字段。
4. db_table：指定维持多对多关系的中间表的表名。

#### 模型元数据选项
| 选项                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| abstract              | 设置为True时模型是抽象父类                                   |
| app_label             | 如果定义模型的应用不在INSTALLED_APPS中可以用该属性指定       |
| db_table              | 模型使用的数据表名称                                         |
| db_tablespace         | 模型使用的数据表空间                                         |
| default_related_name  | 关联对象回指这个模型时默认使用的名称，默认为<model_name>_set |
| get_latest_by         | 模型中可排序字段的名称。                                     |
| managed               | 设置为True时，Django在迁移中创建数据表并在执行flush管理命令时把表移除 |
| order_with_respect_to | 标记对象为可排序的                                           |
| ordering              | 对象的默认排序                                               |
| permissions           | 创建对象时写入权限表的额外权限                               |
| default_permissions   | 默认为`('add', 'change', 'delete')`                          |
| unique_together       | 设定组合在一起时必须独一无二的字段名                         |
| index_together        | 设定一起建立索引的多个字段名                                 |
| verbose_name          | 为对象设定人类可读的名称                                     |
| verbose_name_plural   | 设定对象的复数名称                                           |

### 利用Django后台管理模型

1. 创建超级管理员账号

```shell
python manage.py createsuperuser
Username (leave blank to use 'hao'): jackfrued
Email address: zhang_yide@hotmail.com
Password: 
Password (again): 
Superuser created successfully.
```

2. 启动服务器，登录后台管理系统

```shell
python manage.py runserver
```

访问`http://127.0.0.1:8000/admin`，登录后台管理系统

3. 注册模型类

修改`blog/admin.py`文件

```python
from django.contrib import admin

from hrs.models import Category, Tag, Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
```

4. 对模型进行CRUD操作

可以在管理员平台对模型进行Create（新增）、Read（查看）、Update（更新）、Delete（删除）操作。

5. 注册模型管理类

之前在后台查看部门信息的时候，显示的部门信息并不直观，为此我们再修改`blog/admin.py`文件，通过注册模型管理类，可以在后台管理系统中更好的管理模型。

```python
from django.contrib import admin

from blog.models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'category', 'author')
    ordering = ('-created_time',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
```

> 其中`ordering = ('-created_time',)`中的`-`表示逆序。  

6. 汉化 blog 应用

* 汉化 app 在 admin 后台显示的名字

```python
 blog/apps.py
 from django.apps import AppConfig
  
  
 class BlogConfig(AppConfig):
     name = 'blog'
     verbose_name = '博客'
```

 此前在 `settings.py `中注册应用时，是直接注册的 app 名字 `blog`，现在在 `BlogConfig `类中对 app 做了一些配置，所以应该将这个类注册进去：

```python
 INSTALLED_APPS = [
     'django.contrib.admin',
     ...
  
     'blog.apps.BlogConfig',  # 注册 blog 应用
 ]
```

* 汉化应用下注册的 model

  配置 model 的一些特性是通过 model 的内部类 `Meta` 中来定义。比如对于 Post 模型，要让他在 admin 后台显示为中文，如下： 

```python
 blog/models.py
 ...
 class Post(models.Model):
     ...
     author = models.ForeignKey(User, on_delete=models.CASCADE)
  
     class Meta:
         verbose_name = '文章'
         verbose_name_plural = verbose_name
  
     def __str__(self):
         return self.title
```

> 其中的`__str__()`方法的作用是，当我们使用如`Post.objects.all() `的方法读取数据时，解释器显示的内容将会是 `__str__` 方法返回的内容。   

 相同的方法修改`Category`和`Tag`即可。

* 汉化各 model 的表单 label

 以`Post`为例：

```python
 class Post(models.Model):
     title = models.CharField('标题', max_length=70)
     body = models.TextField('正文')
     created_time = models.DateTimeField('创建时间')
     modified_time = models.DateTimeField('修改时间')
     excerpt = models.CharField('摘要', max_length=200, blank=True)
     category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
     tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
     author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
```

7. 优化表单显示

### 使用ORM完成模型的CRUD操作
在了解了Django提供的模型管理平台之后，我们来看看如何从代码层面完成对模型的CRUD（Create / Read / Update / Delete）操作。我们可以通过manage.py开启Shell交互式环境，然后使用Django内置的ORM框架对模型进行CRUD操作。

```shell
(venv)$ python manage.py shell
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

#### 新增

```shell
>>> from hrs.models import Dept, Emp
>>>
>>> dept = Dept(40, '研发2部', '深圳')
>>> dept.save()
```

#### 更新

```shell
>>> dept.name = '研发3部'
>>> dept.save()
```

#### 查询

1. 查询所有对象。

```shell
>>> Dept.objects.all()
<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>, <Dept: 运维1部>, <Dept: 研发3部>]>
```

2. 过滤数据。

```shell
>>> Dept.objects.filter(name='研发3部') # 查询部门名称为“研发3部”的部门
<QuerySet [<Dept: 研发3部>]>
>>>
>>> Dept.objects.filter(name__contains='研发') # 查询部门名称包含“研发”的部门(模糊查询)
<QuerySet [<Dept: 研发1部>, <Dept: 研发3部>]>
>>>
>>> Dept.objects.filter(no__gt=10).filter(no__lt=40) # 查询部门编号大于10小于40的部门
<QuerySet [<Dept: 销售1部>, <Dept: 运维1部>]>
>>>
>>> Dept.objects.filter(no__range=(10, 30)) # 查询部门编号在10到30之间的部门
<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>, <Dept: 运维1部>]>
```

3. 查询单个对象。

```shell
>>> Dept.objects.get(pk=10)
<Dept: 研发1部>
>>>
>>> Dept.objects.get(no=20)
<Dept: 销售1部>
>>>
>>> Dept.objects.get(no__exact=30)
<Dept: 运维1部>
>>>
>>> Dept.objects.filter(no=10).first()
<Dept: 研发1部>
```

4. 排序数据。

```shell
>>> Dept.objects.order_by('no') # 查询所有部门按部门编号升序排列
<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>, <Dept: 运维1部>, <Dept: 研发3部>]>
>>>
>>> Dept.objects.order_by('-no') # 查询所有部门按部门编号降序排列
<QuerySet [<Dept: 研发3部>, <Dept: 运维1部>, <Dept: 销售1部>, <Dept: 研发1部>]>
```

5. 数据切片（分页查询）。

```shell
>>> Dept.objects.order_by('no')[0:2] # 按部门编号排序查询1~2部门
<QuerySet [<Dept: 研发1部>, <Dept: 销售1部>]>
>>>
>>> Dept.objects.order_by('no')[2:4] # 按部门编号排序查询3~4部门
<QuerySet [<Dept: 运维1部>, <Dept: 研发3部>]>
```

6. 高级查询。

```shell
>>> Emp.objects.filter(dept__no=10) # 根据部门编号查询该部门的员工
<QuerySet [<Emp: 乔峰>, <Emp: 张无忌>, <Emp: 张三丰>]>
>>>
>>> Emp.objects.filter(dept__name__contains='销售') # 查询名字包含“销售”的部门的员工
<QuerySet [<Emp: 黄蓉>]>
>>>
>>> Dept.objects.get(pk=10).emp_set.all() # 通过部门反查部门所有的员工
<QuerySet [<Emp: 乔峰>, <Emp: 张无忌>, <Emp: 张三丰>]>
```

> 说明1：由于员工与部门之间存在多对一外键关联，所以也能通过部门反向查询该部门的员工（从一对多关系中“一”的一方查询“多”的一方），反向查询属性默认的名字是`类名小写_set`（如上面例子中的`emp_set`），当然也可以在创建模型时通过`ForeingKey`的`related_name`属性指定反向查询属性的名字。如果不希望执行反向查询可以将`related_name`属性设置为`'+'`或以`'+'`开头的字符串。  

> 说明2：查询多个对象的时候返回的是QuerySet对象，QuerySet使用了惰性查询，即在创建QuerySet对象的过程中不涉及任何数据库活动，等真正用到对象时（求值QuerySet）才向数据库发送SQL语句并获取对应的结果，这一点在实际开发中需要引起注意！  

> 说明3：可以在QuerySet上使用`update()`方法一次更新多个对象。  

#### 删除

```shell
>>> Dept.objects.get(pk=40).delete()
(1, {'hrs.Dept': 1})
```

### 使用模板系统

1. 创建模板目录

在项目根目录里创建`templates`目录。在该目录下创建`blog`目录用以存放和 blog 相关的模板。

2. 创建`index.html`文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ title }}</title>
</head>
<body>
<h1>{{ welcome }}</h1>
</body>
</html>
```

3. 配置`setting.py`中`TEMPLATES`选项：

```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

4. 修改视图函数

```python
blog/views.py
 
from django.shortcuts import render
 
 
def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
```

### 渲染模板

1. 处理静态文件

* 我们的项目使用了从网上下载的一套博客模板（[点击这里下载全套模板](https://github.com/zmrenwu/django-blog-tutorial-templates)）。这里面除了 HTML 文档外，还包含了一些 CSS 文件和 JavaScript 文件以让网页呈现出我们现在看到的样式。
* 把 CSS 和 JavaScript 文件放在 *blog 应用*的 static 目录下。因此，先在 *blog 应用*下建立一个 static 文件夹。同时，为了避免和其它应用中的 CSS 和 JavaScript 文件命名冲突（别的应用下也可能有和 blog 应用下同名的 CSS 、JavaScript 文件），我们再在 static 目录下建立一个 blog 文件夹，把下载的博客模板中的 css 和 js 文件夹连同里面的全部文件一同拷贝进这个目录。
* 用下载的博客模板中的 index.html 文件替换掉之前我们自己写的 index.html 文件。

2. 修改`index.html`文件，以正确加载静态文件

```html
<!DOCTYPE html>
{% load static %}
<html>
  <head>
      <title>Black &amp; White</title>
 
      <!-- meta -->
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
 
      <!-- css -->
      <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
      <link rel="stylesheet" href="{% static 'blog/css/bootstrap.min.css' %}">
      <link rel="stylesheet" href="{% static 'blog/css/pace.css' %}">
      <link rel="stylesheet" href="{% static 'blog/css/custom.css' %}">
 
      <!-- js -->
      <script src="{% static 'blog/js/jquery-2.1.3.min.js' %}"></script>
      <script src="{% static 'blog/js/bootstrap.min.js' %}"></script>
      <script src="{% static 'blog/js/pace.min.js' %}"></script>
      <script src="{% static 'blog/js/modernizr.custom.js' %}"></script>
  </head>
  <!-- 其它内容 -->
  <body>
      <!-- 其它内容 -->
      <script src="{% static 'blog/js/script.js' %}"></script>
  </body>
</html>
```

> 用 {% %} 包裹起来的叫做模板标签，功能类似于函数。  
> 用{{ }} 包裹起来的叫做模板变量，作用是在最终渲染的模板里显示由视图函数传过来的变量值。  

3. 修改视图函数

修改视图函数，以获取数据库中的数据，并准备好，发送给模板。

```python
blog/views.py
 
from django.shortcuts import render
from .models import Post
 
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```

4. 修改模板

	1. 修改模板，以获取视图函数中的数据。

	2. 将模板中`article`部分替换为一下内容：

```html
templates/blog/index.html
 
...
{% for post in post_list %}
  <article class="post post-{{ post.pk }}">
    ...
  </article>
{% empty %}
  <div class="no-post">暂时还没有发布的文章！</div>
{% endfor %}
...
```

> 这里的 `{{ post.pk }}`（pk 是 primary key 的缩写，即 post 对应于数据库中记录的 id 值，该属性尽管我们没有显示定义，但是 django 会自动为我们添加）  
>  `{% empty %} `的作用是当 `post_list` 为空，即数据库里没有文章时显示 `{% empty %}` 下面的内容  

	3. 并依次将`post`里的属性替换进去。