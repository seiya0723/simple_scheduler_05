window.addEventListener("load" , function (){

    var config_date = {
    }
    var config_time = {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        time_24hr: true,
    }
    var config_dt = {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
    }


    flatpickr("#date", config_date);
    flatpickr("#time", config_time);

    flatpickr("#dt",config_dt)



});

