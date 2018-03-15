# Parse PDF from English to Chinese via Google Translate

## 技术栈
1. 通过pdfminer解析pdf文件
2. 再调用谷歌翻译API进行翻译

## 使用流程
1. 将需要解析翻译的PDF放在脚本目录下
2. 修改file name & target name
3. 运行`python Pdf2Text.py`生成对应语言的对应txt文本文档

不管是学术还是工作，用到的机会应该很多，在此跟大家分享。

*暂时没有考虑效率的问题，如果谁有比较好的方法可以pull request。*

Have Fun!