install:
	# このフォルダでは3.8.16を使用
	pyenv local 3.8.16
	# Pythonのバージョン指定
	poetry env use 3.8.16
	# pipのアップデート
	poetry run pip install -U pip setuptools
	# pyproject.tomlの内容をインストール
	poetry install