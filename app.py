# -*- coding: utf-8 -*-
"""
ひだまり 健康チェック管理システム Ver3.3
画面分離・安全移行版

本番安定性を守るため、既存の単一app.py本体は services/legacy_app.py に退避し、
入口ファイル app.py から読み込みます。

次段階では pages/dashboard.py 等へ画面処理を少しずつ移します。
"""
import importlib

def main():
    importlib.import_module("services.legacy_app")

if __name__ == "__main__":
    main()
