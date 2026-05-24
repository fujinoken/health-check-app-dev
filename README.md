# ひだまり 健康チェック管理システム Ver3.3.2

## 修正内容
- Streamlitの自動ページメニューに `app / admin / dashboard / excretion / health input / life` が出ないよう、`pages/` フォルダを削除しました。
- 起動ファイルは `app.py` のままです。
- 本体は `services/legacy_app.py` に退避しています。
- 将来の画面分離用メモは `app_pages/` に置いています。

## GitHubへアップロードするもの
このフォルダの中身すべてをアップロードしてください。

## Streamlit Cloud設定
Main file path: `app.py`
