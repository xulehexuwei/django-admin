
# 创建django项目

```shell
django-admin startproject django_web
```

- 创建新的app

```shell
python manage.py startapp auth
```


# 启动项目

```shell
python manage.py runserver 0:8000

# windows 启动 必须 127.0.0.1
python manage.py runserver 127.0.0.1:8000
```

# templates 位置修改

从模板中我们知道变量使用了双括号。

接下来我们需要向Django说明模板文件的路径 settings.py，修改 TEMPLATES 中的 DIRS 为 [os.path.join(BASE_DIR, 'templates')]，如下所示:

```shell

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 修改位置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

# Django框架 -- 如何在html中导入css,js等文件

https://blog.csdn.net/weixin_42912498/article/details/107687171

- 引入 css文件

```html
{% load static %}
<!doctype html>
<html lang="en">
<head>
<link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"/>
<link href="{% static 'css/login.css' %}" rel="stylesheet"/>
    
<script type='text/javascript' src="{% static 'neo4j/js/jquery-1.8.3.min.js' %}"></script>
</head>
</html>
```


# ajax 案例

```html
$.ajax({
            xhrFields: {
                withCredentials: true
            },
            // {#url: "https://bi.aminer.cn/bi_api/journal_robot/concept_explain?concept=" + kw, //请求的url地址
            url: "query?text=" + kw, //请求的url地址
            dataType: "json", //返回格式为json
            async: false, //请求是否异步，默认为异步，这也是ajax重要特性
            type: "GET",
            success: function (res_dict) {
                var graph_data = res_dict['graph']
                create_graph(graph_data)
            },
            error: function () {
                alert('请求数据失败');
            }
        });
```