#coding=utf-8

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# NOTE: 设置基准目录位置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# NOTE: 项目码,自动生成
SECRET_KEY = 'py@qt+#_eqljrja!mp&)8d%=+-4(qrh(&=)=3x$0apz+&u1+f&'

# SECURITY WARNING: don't run with debug turned on in production!
# NOTE: 为True时,在浏览器中会体现错误的具体位置及错误类型.用于调试url中的参数,
DEBUG = True
# NOTE: 与debug配套使用,debug如果为false,则中括号中需要填写地址
ALLOWED_HOSTS = []


# Application definition
# NOTE: !!!!!
# NOTE: 添加应用的列表,使用manage创建一个应用时,需要在此注册,
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'formapp',
    'login_test_app',
]
# NOTE: 中间件注册列表
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# NOTE:!!!!
# NOTE:设置urls根文件
ROOT_URLCONF = 'booksite.urls'
# NOTE: !!!!!
# NOTE: 模板相关设置内容
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
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

WSGI_APPLICATION = 'booksite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# NOTE: !!!
# NOTE: 数据库相关设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # NOTE: 修改引擎
        'NAME': 'Bookdb',                       # NOTE: 修改数据库名称
        'USER': 'root',                          # NOTE: 数据库用户民
        "PASSWORD":'123',                       # NOTE:   数据库密码
        'HOST':'',                              # NOTE: 主机IP
        'PORT':'',                              # NOTE: 主机端口号

    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
# NOTE: 系统自带配置
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# NOTE: 语言编码格式
LANGUAGE_CODE = 'zh-Hans'
# NOTE: 设置时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# NOTE: 邮件相关设置.工作中,一般会使用第三方插件来完成此功能.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USER_TLS = False   # NOTE: 邮件类型
EMAIL_HOST = 'smpy.126.com' # NOTE: 设置邮箱代理
EMAIL_HOST_USER = 'guohao0221@126.com'
EMAIL_HOST_PASSWORD = 'Skying'
DEFAULT_FROM_EMAIL = 'guohao0221@126.com'


# NOTE: midia 设置        创建上传
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'sroot')
STATICFILES_DIRS = (BASE_DIR,'static')


AUTH_USER_MODEL = 'myapp.User'
