---
title: 'python出错ModuleNotFoundError: No module named ''sklearn.cross_validation'''
date: 2019-04-28 22:19:31
tags: 
    - Python错误处理
categories: 
    - Python心得
---

```python
from sklearn.cross_validation import KFold
from sklearn.cross_validation import train_test_split

```
## sklearn更新后在执行以上代码时可能会出现这样的问题：
```python
ModuleNotFoundError: No module named 'sklearn.cross_validation'
```
## 此时可以考虑使用以下方法导入库：
```python
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
```
  此时就不会报错了。

