from django import forms 

from django.forms import ModelForm
from .models import Scheduler


#モデルを継承したフォーム、P91を参照。modelのクラス名を指定。models.pyで定義した検証するフィールド(今回はdeadlineとtask)を指定。
#これにより、指定した文字数をはみ出していないか、入力必須の項目を入力しているか、型が間違っていないかなどを検証できる。
class SchedulerForm(ModelForm):
    class Meta:
        model   = Scheduler
        fields  = [ "deadline","task" ]

#モデルを継承しないで作るフォーム。フォームクラスの書き方P85を参照。
#今回はIDが数値型であることを確認できればいいので属性は未指定
class SchedulerIDForm(forms.Form):
    id  = forms.IntegerField()

