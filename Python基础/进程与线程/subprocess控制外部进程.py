import subprocess
# 启动程序
subprocess.run(r'E:\常用软件\Notepad++\notepad++.exe')
# 关闭进程树
subprocess.run('taskkill /f /t /im notepad++.exe')