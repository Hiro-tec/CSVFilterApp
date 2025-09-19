# CSV 列ごとOR条件フィルタGUI

## 内容
- csv_filter_gui.py : 改良GUIスクリプト
- sample_data_large.csv : 入力サンプル
- filter_data_large.csv : フィルタ用サンプル
- dist/ : exe/app出力フォルダ
- icon.ico : 任意（Windowsアイコン）

## 実行方法

### Windows
1. dist/csv_filter_gui.exe をダブルクリックで起動
2. 「入力CSVを選択」で sample_data_large.csv を選択
3. 「フィルタCSVを選択」で filter_data_large.csv を選択
4. 「除外対象列を追加」で列を選択（複数可）
5. 「フィルタ実行」→ 保存先指定 → CSV完成

### Mac
1. dist/CSVFilterApp.app を起動
2. Windowsと同様に操作
3. 初回起動時に「開発元未確認アプリ」警告が出る場合は
   - 「システム環境設定 > セキュリティとプライバシー > 開発元未確認アプリを許可」
   - またはターミナルで `sudo xattr -rd com.apple.quarantine dist/CSVFilterApp.app`

## 注意
- CSVファイルはGUI上で自由に選択可能
- 列ごとOR条件で除外されます

