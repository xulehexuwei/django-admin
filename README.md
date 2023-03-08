
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