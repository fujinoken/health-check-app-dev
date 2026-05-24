# -*- coding: utf-8 -*-
"""
排泄チェック入力画面
Ver3.3 画面分離・安全移行版

このファイルは将来の画面分離用入口です。
現段階では既存機能を壊さないため、services/legacy_app.py を呼び出します。
画面処理を移す場合は、このファイルへ少しずつ関数を切り出します。
"""
from services.runtime import run_legacy_app

run_legacy_app()
