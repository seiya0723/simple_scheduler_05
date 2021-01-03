from django.contrib import admin


#admin.pyはDjangoの管理サイトを作るための物。モデルを指定することで、対象モデルのデータ追加、削除、編集も管理サイトから簡単にできるようになる。

#1:まずはmodels.pyから管理したいモデルをimportする
from .models import Scheduler

#2:admin.site.registor()の引数にimportしたモデルを指定
admin.site.register(Scheduler)

#3:後はcreatesuperuserで管理サイトにアクセスするユーザーを作る
"""
python3 manage.py createsuperuser

インタラクティブシェル(対話型シェル)になるので、IDとメールアドレス、パスワードを指定してアカウントを作る
"""
