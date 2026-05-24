# -*- coding: utf-8 -*-
"""
画面分離の共通実行入口。
既存機能を壊さないため、当面は legacy_app を読み込む。
"""
import importlib

def run_legacy_app():
    return importlib.import_module("services.legacy_app")
