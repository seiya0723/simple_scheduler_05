from django.db import models

#P46のモデルクラスの書き方を参照
class Scheduler(models.Model):
    class Meta:
        db_table    = "scheduler"

    #DBのカラム(タテ列)に当たるフィールドを指定する(P47を参照)
    deadline    = models.DateTimeField(verbose_name="締め切り日時")
    task        = models.CharField(verbose_name="やること",max_length=500)
    done        = models.BooleanField(default=False)


    #管理サイト閲覧時、1つのレコード(ヨコ列)をprint文で出力時、taskが表示される。
    def __str__(self):
        return self.task

#モデルを定義した後はマイグレーションを実行し、DBに反映させる
"""
python3 manage.py makemigrations
python3 manage.py migrate 
"""

