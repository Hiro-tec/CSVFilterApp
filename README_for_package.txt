CSVフィルタGUIアプリ 使用方法
=============================

このZIPには以下のファイルが含まれています：

1. csv_filter_gui.exe
   - メインのGUIアプリケーションです
   - Windows 10/11 で動作確認済み

2. input_data_large.csv
   - 入力用のサンプルCSVファイル
   - フィルタ対象となるデータが含まれています

3. filter_data_large.csv
   - フィルタ条件を記載したCSVファイル
   - input_data_large.csv からこの条件に一致する行を除外します

使い方
------

1. ZIP を任意のフォルダに解凍してください
2. `csv_filter_gui.exe` をダブルクリックして起動
3. 「入力ファイル」に input_data_large.csv を選択
4. 「フィルタファイル」に filter_data_large.csv を選択
5. フィルタしたい列を指定
6. 「実行」ボタンを押すと出力ファイルが生成されます

注意事項
---------
- GUIはWindows環境でのみ動作します
- 出力ファイルは同じフォルダ内に `output.csv` として作成されます
- 大規模CSVを使用する場合はPCのメモリに注意してください


