#!/bin/bash

# 切換到存儲庫目錄
cd ~/alfred/ngrok0920

# 執行 Python 腳本
python3 changeUrl.py

# 添加所有更改到 Git
git add .

# 提交更改
git commit -m "Update URL" 

# 推送更改到遠程存儲庫（使用 -f 強制推送）
git push -f
