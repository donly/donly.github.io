# BLOG

## 安装
```
pip3 install virtualenv
virtualenv ENV
source ENV/bin/activate
pip install --upgrade pelican
pelican --version
```

## 写作
```
source NOTE_ENV/bin/activate
pelican content -r -l -s pelicanconf_dev.py
```

## 发布
```
make publish
make github
```

## 相关链接
1. http://docs.getpelican.com/en/stable/index.html
1. https://docs.getpelican.com/en/stable/quickstart.html
1. https://daringfireball.net/projects/markdown/syntax#html