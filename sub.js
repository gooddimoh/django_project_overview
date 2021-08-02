$(document).ready(function () {
    setTimeout(function () {
        console.log("timeout");
        console.clear();
    }, 3000);
    $("#search-input").keypress(function () {
        window.data1 = ' ';
        window.data2 = ' ';
        window.keyword = $("#search-input").val();
        window.rowvalhtml = ' ';
        window.rowvalobjs = [];
        window.json_data = [];
        window.allrows = [];
        window.response_data = [];
        window.result_data = [];
        window.global_json_data = {};
        window.outputdata = [];

        function datacycle(data, keyword) {
            $.each(data, function (row, rowval) {
                $.each(rowval, function (key, val) {
                    if (val === keyword && key === "name") {
                        allrows.push(JSON.parse(JSON.stringify(rowval)));
                        console.log(allrows);
                    } else {
                        console.log("введите правильное имя");
                    }
                });
            });

            $.each(allrows.sort(), function (k, v) {
                outputdata += "<div class=\"results_page\">" + "<ul> <li class='id'> id:  " + v.id + "</li>" +
                    // "<li class=''> level:  " + v.level + "</li>" +
                    "<li class=''> name:  " + v.name + "</li>" +
                    "<li> link:  <a target='_blank' href=" + v.link + ">" + v.name + "</a></li>" +
                    "<li> description  " + v.description +
                    "<li> " + v.level + "</li>" +
                    "</li>" +
                    "</ul></div>";
            });

            $("#all_data").html('Loading....');
            $("#all_data").html(outputdata).fadeIn(400);
        }

        $.ajax({
            url: "http://127.0.0.1:8088/standards_list",
            success: function (response) {
                $.each(response, function (k, v) {
                    response_data.push(v);
                });

            },
        });
        $.ajax({
            url: "http://127.0.0.1:8088/products_list ",
            success: function (response) {
                $.each(response, function (k, v) {
                    response_data.push(v);
                });
            },
        });

        setTimeout(function () {
            datacycle(response_data, keyword);
            console.log("We here", response_data, keyword);

        }, 300);
    });

});
