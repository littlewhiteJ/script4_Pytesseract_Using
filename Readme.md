# 一个用了pytesseract做OCR的脚本

**这里就是个普通的用google的pytesseract实现OCR的脚本**

写出来就是为了方便用

没有任何高级之处

## 使用指东

### 下载安装包
for windows:
- 在[这里](https://digi.bib.uni-mannheim.de/tesseract/)下载喜欢的版本

for macbook:
- 参考[这里](https://www.jianshu.com/p/719c053f170b)

for linux:
- 都用linux还不去看官方网站？

### 下载训练数据
- 在[这里](https://github.com/tesseract-ocr/tessdata)下载需要的语言训练集
- 并放在tesseract路径下的tessdata里面

### 使用这个脚本
- 把要处理的图片放在【image】下
- 运行ocr.py
- 文档会出现在【txt】下
- 中间产物(灰度图)会出现在【threshPic】下
- 可以通过修改config.json改变文件夹名字（虽然没啥用的样子）
- 默认的是处理中文，处理中英文夹杂可能会有部分乱码
