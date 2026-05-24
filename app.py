# -*- coding: utf-8 -*-
"""
ひだまり 健康チェック管理システム Ver3.3.1
画面分離・安全移行版（起動修正版）

Streamlit Cloudでは __name__ 判定で起動が止まる場合があるため、
app.py読み込み時に必ず services/legacy_app.py を実行します。
"""
from services.runtime import run_legacy_app

# Streamlit Cloudの起動時に必ず本体を表示する
run_legacy_app()
