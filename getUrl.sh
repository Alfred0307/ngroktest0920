#!/bin/bash

#先睡三秒測試
sleep 3

# 切換到存儲庫目錄
cd /home/bigred/alfred/ngrok0920

# 執行 Python 腳本
python3 /home/bigred/alfred/ngrok0920/changeUrl.py

# 添加所有更改到 Git
git add .

# 提交更改
git commit -m "Update URL"

# 推送更改到遠程存儲庫（使用 -f 強制推送）
git push -f

