
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

    saladId = saladId.replace('Sa','');

    var mainDishes = document.getElementsByName('mainDish');
    var mainDishId = '';
    for (var i in mainDishes){
        if (mainDishes[i].checked){
            mainDishId = mainDishes[i].id;
        }
    }

    mainDishId = mainDishId.replace('Ma','');

    var garnish = document.getElementsByName('garnish');
    var garnishId = '';
    for (var i in garnish){
        if (garnish[i].checked){
            garnishId = garnish[i].id;
        }
    }

    garnishId = garnishId.replace('Ga','');

    var alcohol = document.getElementsByName('alcohol');
    var alcoholIds = '';
    for (var i in alcohol){
        if (alcohol[i].checked){
            alcoholIds =  alcoholIds + alcohol[i].id + ",";
        }
    }

    alcoholIds = alcoholIds.replace(/Al/g, '');

    if (saladId == ''){
        alert('Необходимо выбрать салат!');
        return;
    }

    if(mainDishId == ''){
        alert("Необходимо выбрать главное блюдо!");
        return;
    }

    if(mainDishId != '9'){
        if(garnishId == ''){
            alert("Необходимо выбрать гарнир!");
            return;
        }
    }
    else {
        garnishId = '-1'
    }

    if(alcoholIds == ''){
        alert("Необходимо выбрать Алкоголь!");
        return;
    }

    $.post('/invite/save_menu/', {'alcohol': alcoholIds, 'garnish': garnishId, 'mainDish': mainDishId, 'salad': saladId }, OnSuccess)

}


   function OnSuccess (data) {
            if(data='ok'){
                location.href = '/invite/profile'
            }
            else
                alert('Произошла ошибка')

    }