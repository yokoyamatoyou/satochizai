# MVP開発計画書: 多角的理解支援システム

本ドキュメントは、"多様な文化的・解釈的視点の体系的提示による多角的理解支援システム" のMVPを実装するための計画をまとめたものです。GUIアプリケーションとして動作し、OpenAI API を中核に利用します。

## 1. プロジェクト概要

利用者が入力したテキストを文化的・地理的に多様な経路で翻訳し、その過程で生じる意味変化(セマンティック・ドリフト)を可視化して、多角的理解を支援するデスクトップツールを作成します。

## 2. 技術スタック

- Python 3.10+
- OpenAI API
- ライブラリ: `pandas`, `numpy`, `requests`, `gdelt`, `sentence-transformers`, `scikit-learn`, `plotly` or `matplotlib`, `streamlit`
- 外部データ: Hofstede Cultural Dimensions, WALS, GDELT
- インターネットアクセス可能な環境で動作

## 3. 開発フェーズ

### フェーズ1: バックエンド基盤とデータ処理
1. プロジェクト構造を作成。
2. Hofstede と WALS のCSVを取得し `data` ディレクトリに保存。`data_handler.py` を作成しデータ読み込み・前処理を実装。
3. `core_logic.py` に文化的距離(CDS)、地政学距離(GIS)、言語距離(LDS) を計算する関数を実装。
4. Greedy Algorithm に基づき多様性の高い翻訳言語経路を選択する関数 `select_diverse_languages` を実装。

### フェーズ2: OpenAI API連携と翻訳パイプライン
1. `.env` に `OPENAI_API_KEY` を置き、`openai` ライブラリで読み込む。
2. `translate_text(text, src, tgt)` を作成し Chat Completion API で逐次翻訳。
3. `run_translation_chain(source_text, language_path)` を実装し、選択された言語経路に従って複数段翻訳を実行。

### フェーズ3: 意味分析と可視化
1. `sentence-transformers` でベクトルを取得する `get_embedding`。
2. 各翻訳ステップでベクトルを生成しコサイン距離を計算する `calculate_semantic_drift`。
3. `scikit-learn` と `plotly` を使い翻訳経路をプロットする `generate_trajectory_plot`。

### フェーズ4: GUI開発
1. `streamlit` を用い `app.py` にUIを作成。入力テキスト欄と「分析開始」ボタンを配置。
2. ボタン押下で `select_diverse_languages`→`run_translation_chain`→`generate_trajectory_plot` を順に実行。結果を画面に表示。

### フェーズ5: 調整とパッケージング
1. エラーハンドリング、進捗表示の改善。
2. `requirements.txt` と `README.md` を整備し、セットアップ方法や実行方法(`streamlit run app.py`) を記載。

### フェーズ6: 医用画像連携
1. 画像の手動アップロードフォームを追加し DICOM 表示に対応。
2. PACS から DICOM SCU や DICOMweb を用いた自動取込機能を実装。
3. 解析結果を PACS Overlay や DICOM SR として返却できるようにする。
4. 取得した画像と結果をビューワー上で確認できるよう統合。

## 4. 運用メモ

- 外部データはOpenAI APIを利用して取得できる範囲でダウンロードします。欠損がある場合は再取得を試み、それでも得られないデータは"スキップ"と記録します。
- テストケースとしてニュース記事を入力し、翻訳結果および意味変化の軌跡を確認します。
- 本ファイルは手順の参照用マニュアルとしてリポジトリに配置し、開発状況に応じて随時更新します。

