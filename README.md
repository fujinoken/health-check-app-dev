# ひだまり 健康チェック管理システム Ver3.3.1

画面分離・安全移行版（起動修正版）です。

## 起動ファイル
Streamlit Cloud の Main file path は `app.py` のままです。

## 構成
- app.py: 起動入口
- services/legacy_app.py: 既存安定版の本体
- services/runtime.py: 共通実行入口
- pages/: 将来の画面分離先

## 注意
GitHubへは、このフォルダの中身をルートへアップロードしてください。
`hidamari_ver3_3_page_split_fixed/` フォルダごと入れないでください。
