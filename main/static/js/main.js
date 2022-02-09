let url = null;
let currentSection = $("#current-section");
let textSection = currentSection.text();
let methodType = "Get";
let ajaxData = {};

if (textSection === 'home'){
    url = `/api/v1/latest-products/`;
} 
else if (textSection === 'shoes'){
    url = `/api/v1/products/shoes/`;

} else if (textSection === 'search'){
    url = `/api/v1/products/search/`
    methodType = "POST";
    query = $("#query-search")
    ajaxData = {
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(), 
        'query': query.text()
    }
    
    query.remove()
}


currentSection.remove()

$(document).ready(function () {
    $(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    });

    $('#myCarousel').carousel({
        interval: false
    });

    //scroll slides on swipe for touch enabled devices

    $("#myCarousel").on("touchstart", function (event) {
        let yClick = event.originalEvent.touches[0].pageY;
        $(this).one("touchmove", function (event) {

            let yMove = event.originalEvent.touches[0].pageY;
            if (Math.floor(yClick - yMove) > 1) {
                $(".carousel").carousel('next');
            } else if (Math.floor(yClick - yMove) < -1) {
                $(".carousel").carousel('prev');
            }
        });
        $(".carousel").on("touchend", function () {
            $(this).off("touchmove");
        });
    })

});


$.ajax({
    url: url,
    dataType: "json",
    type: methodType,
    async: true,
    data: ajaxData,
    success: function (data) {
        
        if (textSection === "home"){
            addShoes(data);
        } else if (textSection === "shoes"){
            addShoes(data.products)
        } else if (textSection === "search"){
            console.log(data)
            addShoes(data)
        }
       
    },
    error: function (xhr, exception) {
        let msg = "";
        if (xhr.status === 0) {
            msg = "Not connect.\n Verify Network." + xhr.responseText;
        } else if (xhr.status == 404) {
            msg = "Requested page not found. [404]" + xhr.responseText;
        } else if (xhr.status == 500) {
            msg = "Internal Server Error [500]." +  xhr.responseText;
        } else if (exception === "parsererror") {
            msg = "Requested JSON parse failed.";
        } else if (exception === "timeout") {
            msg = "Time out error." + xhr.responseText;
        } else if (exception === "abort") {
            msg = "Ajax request aborted.";
        } else {
            msg = "Error:" + xhr.status + " " + xhr.responseText;
        }

        console.log(msg)
    }
}); 


function addShoes(data){

    let section = $('#shoes-section')

    for (let n = 0; n < data.length; n++){

        section.append(`
    
    <div class="col-sm-4">
        <div class="best_shoes">
            <p class="best_text">${data[n].name}</p>
            <a href=shoes/${data[n].name}>
            <div class="shoes_icon"><img src="${data[n].get_thumbnail}"></div>
            </a>
            <div class="star_text">
                <div class="left_part">
                    <ul>
                        <li><img src="static/images/star-icon.png"></li>
                        <li><img src="static/images/star-icon.png"></li>
                        <li><img src="static/images/star-icon.png"></li>
                        <li><img src="static/images/star-icon.png"></li>
                        <li><img src="static/images/star-icon.png"></li>
                    </ul>
                </div>
                <div class="right_part">
                    <div class="shoes_price">$ <span style="color: #ff4e5b;">${data[n].price}</span></div>
                </div>
            </div>
        </div>
    </div>
    
    `)

    }
}

function addToCart(product){
    
}