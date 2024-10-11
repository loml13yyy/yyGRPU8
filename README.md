# yyGRPU8
用友 GRP-U8 UploadFileData批量检测脚本
![图片](https://github.com/user-attachments/assets/feae2cd5-82d8-492c-971a-c668e4c39603)


```shell
漏洞描述：
用友 GRP-U8 UploadFileData接口存在任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限

fofa搜索语句：
app="用友-GRP-U8"

工具使用方法：
"-u", "--url",指定检测url
"-f", "--file"，指定批量检测漏洞的文件
 "-h","--help"，获取帮助信息

直接运行脚本获取帮助信息
检测成功的url会被输出至同目录下的upload.txt文件中
```
