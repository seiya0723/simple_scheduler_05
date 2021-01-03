from django.shortcuts import render,redirect,get_object_or_404

from django.views import View

#カスタムクエリを使う
from django.db.models import Q

#models.pyで定義したSchedulerをimportする
from .models import Scheduler

from .forms import SchedulerForm,SchedulerIDForm


#P35のビュー関数の書き方(関数ベース vs クラスベース)を参照。後の汎用性も考慮しクラスベースのビューを採用した。
class SchedulerView(View):

    def get(self, request, *args, **kwargs):

            # GET文のリクエストの中に、name属性searchがある場合(検索された時)の処理
        if "search" in request.GET:

                # (1)キーワードが空欄もしくはスペースのみの場合、ページにリダイレクト
                if request.GET["search"] == "" or request.GET["search"].isspace():
                    return redirect("scheduler:index")

                # (2)キーワードをリスト化させる(複数指定の場合に対応させるため)
                search = request.GET["search"].replace("　", " ")
                search_list = search.split(" ")

                # (3)クエリを作る
                query = Q()

                # TODO:ここでANDとORを分岐させる
                for word in search_list:
                    # TIPS:AND検索の場合は&を、OR検索の場合は|を使用する。
                    if "checkbox" in request.GET:
                        if request.GET["checkbox"]:
                            query &= Q(task__contains=word)
                        else:
                            query |= Q(task__contains=word)
                    else:
                        query |= Q(task__contains=word)

                    # (4)作ったクエリを実行
                data = Scheduler.objects.filter(query)

        else:
                # .all()メソッドを使用することでDBに格納されているSchedulerのデータを全て抽出できる(P57)
                # .order_by()メソッドを使い、並び替えをする(P61)
                data = Scheduler.objects.all().order_by("deadline")

        context = {"data": data}

        return render(request, "scheduler/index.html", context)

    def post(self ,request, *args, **kwargs):

        #クライアントから受け取ったデータをDBに格納する。(P62)
        """
        posted  = Scheduler(  deadline    = request.POST["deadline"],
                              task        = request.POST["task"]    )
        posted.save()
        """

        #ここに送信されたデータがSchedulerFormに引数として与えられ、.is_valid()でバリデーションを行う。P87のビューでの利用例を参照
        formset = SchedulerForm(request.POST)
        
        #バリデーションOKの場合、Trueが返ってくる。
        if formset.is_valid():
            #モデルを継承して作ったformsのクラスの場合、.save()メソッドを使うことでDBに保存できる。
            formset.save()
        else:
            print("バリデーションエラー")
        return redirect("scheduler:index")

#クラスで記述したビューを関数化するための処理。これによりurls.pyから呼び出せる
index   = SchedulerView.as_view()


#指定したスケジュールを削除するクラス
class SchedulerDelete(View):

    def post(self ,request, *args, **kwargs):

        #削除対象のレコードをIDで一意に特定する。.delete()で削除
        """
        posted  = Scheduler.objects.filter(id=request.POST["id"])
        posted.delete()
        """

        #バリデーションを行う
        formset = SchedulerIDForm(request.POST)

        #バリデーションが適切であれば削除処理、そうでなければエラー表示
        if formset.is_valid():

            #バリデーションした後の値を取り出す
            clean_data  = formset.clean()

            #filterで絞り込み、.delete()で削除処理をする。
            Scheduler.objects.filter(id=clean_data["id"]).delete()

        else:
            print("バリデーションエラー")
        return redirect("scheduler:index")

delete  = SchedulerDelete.as_view()


#編集処理を行うクラス
class SchedulerEdit(View):

    def post(self ,request, *args, **kwargs):

        formset = SchedulerIDForm(request.POST)

        if formset.is_valid():
            clean_data      = formset.clean()
            target          = clean_data["id"]
        else:
            print("バリデーションNG(IDがありません)")
            return redirect("scheduler:index")
            
        #get_object_or_404は存在するIDであればそのまま次の処理を、存在しなければNotFoundを返す。
        instance    = get_object_or_404(Scheduler.objects.all(), pk=target)

        #第二引数にinstanceを指定することで、対象の編集ができる
        formset     = SchedulerForm(request.POST, instance=instance)

        if formset.is_valid():
            print("バリデーションOK")
            formset.save()
        else:
            print("バリデーションNG")

        return redirect("scheduler:index")

edit    = SchedulerEdit.as_view()


