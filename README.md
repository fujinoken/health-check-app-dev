# ひだまり 健康チェック管理システム Ver3.3

## 構成

```text
app.py
pages/
  dashboard.py
  health_input.py
  excretion.py
  life.py
  admin.py
services/
  legacy_app.py
  runtime.py
db/
components/
utils/
config/
tests/
requirements.txt
```

## 使い方

Streamlit Cloud の Main file path は `app.py` のままで使えます。

## 重要

この版は「画面分離の第一段階」です。
既存機能を壊さないため、実処理は `services/legacy_app.py` に残しています。
今後は、1画面ずつ `pages/` 側へ移していくと安全です。
