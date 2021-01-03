window.addEventListener("load" , function (){

    var config_dt   = {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        "locale"  : "ja"
    };

    flatpickr("#dt",config_dt);

    setInterval('showClock2()',1000);

});

//イベントハンドラを定義する
$(function (){

    $(".edit_button").on("click", function() {
        modal_open($(this).val());
    });

    var modal           = $('#modal');
    var modalContent    = $('#modal_content');

    //画面外が押されたときの処理
    $(modal).on('click', function(event) {
        if(!($(event.target).closest(modalContent).length)){
            modal_close();
        }
    });

});


function set2fig(num) {
   // 桁数が1桁だったら先頭に0を加えて2桁に調整する
   var ret;
   if( num < 10 ) { ret = "0" + num; }
   else { ret = num; }
   return ret;
}
function showClock2() {
   var nowTime = new Date();
   var nowYear = set2fig( nowTime.getFullYear() + 1 );
   var nowMonth = set2fig( nowTime.getMonth() + 1 );
   var nowDate = set2fig( nowTime.getDate() + 1);
   var nowHour = set2fig( nowTime.getHours() );
   var nowMin  = set2fig( nowTime.getMinutes() );
   var nowSec  = set2fig( nowTime.getSeconds() );
   var msg = "現在"+ nowYear + "年" + nowMonth + "月" + nowDate + "日" + nowHour + ":" + nowMin + ":" + nowSec + " です。";
   document.getElementById("RealtimeClockArea2").innerHTML = msg;
}

function modal_open(id){

    $('#modal').show();

    //deadline処理
    var deadline_str    = $("#" + id + "_deadline").text();

    deadline_str        = deadline_str.replace("年","-");
    deadline_str        = deadline_str.replace("月","-");
    deadline_str        = deadline_str.replace("日","");
    deadline_str        = deadline_str.replace("時",":");
    deadline_str        = deadline_str.replace("分","");

    var config_dt   = { 
        defaultDate: deadline_str,
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        "locale"  : "ja"
    };  

    flatpickr('#modal_deadline', config_dt);


    //task処理
    var modal_text  = $("#" + id + "_task").html();
    modal_text      = modal_text.replace(/<br>/mg,"\n");
    $("#modal_task").val(modal_text);


    //id処理
    $("#edit_target_id").val(id)

};
function modal_close(){
    $('#modal').hide();
};

