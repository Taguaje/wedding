
function changeVisibility(name) {
    var visible = name != 'Семга в креветочном соусе';
    var garnishSection = document.getElementById('garnish-id');
    garnishSection.hidden = !visible;
    var garnish = document.getElementsByName('garnish');
    for (var i in garnish){
        garnish[i].checked = false;
    }
}

function saveMenu() {
    var salads = document.getElementsByName('salad');
    var saladId = '';
    for (var i in salads){
        if (salads[i].checked){
            saladId = salads[i].id;
        }
    }



    var mainDishes = document.getElementsByName('mainDish');
    var mainDishId = '';
    for (var i in mainDishes){
        if (mainDishes[i].checked){
            mainDishId = mainDishes[i].id;
        }
    }


    var garnish = document.getElementsByName('garnish');
    var garnishId = '';
    for (var i in garnish){
        if (garnish[i].checked){
            garnishId = garnish[i].id;
        }
    }

    var alcohol = document.getElementsByName('alcohol');
    var alcoholIds = '';
    for (var i in alcohol){
        if (alcohol[i].checked){
            alcoholIds =  alcoholIds + alcohol[i].id + ",";
        }
    }

    saladId = saladId.replace('Sa','');
    if (saladId == ''){
        alert('Необходимо выбрать салат!');
        return;
    }

    mainDishId = mainDishId.replace('Ma','');
    if(mainDishId == ''){
        alert("Необходимо выбрать главное блюдо!");
        return;
    }

    var mainDishname = document.getElementById(mainDishId + 'Ma').getAttribute('data-name');

    garnishId = garnishId.replace('Ga','');
    if(mainDishname != 'Семга в креветочном соусе'){
        if(garnishId == ''){
            alert("Необходимо выбрать гарнир!");
            return;
        }
    }
    else {
        garnishId = '-1'
    }

    alcoholIds = alcoholIds.replace(/Al/g, '');
    if(alcoholIds == ''){
        alert("Необходимо выбрать Алкоголь!");
        return;
    }
    document.getElementById('loader').hidden = false;
    $.post('/invite/save_menu/', {'alcohol': alcoholIds, 'garnish': garnishId, 'mainDish': mainDishId, 'salad': saladId }, OnSuccess)

}


function OnSuccess (data) {
    if(data='ok'){
        location.href = '/invite/profile'
    }
    else {
        document.getElementById('loader').hidden = false;
        alert('Произошла ошибка')
    }

}