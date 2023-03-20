(function cartHandler() {

//ждём, когда загрузится документ
//тело функции будет выполнено только после полной загрузки документа
$(document).ready(function () {
    $('.btn').click(function (e) {
        // отменяем событие по умолчанию
        // в нашем случае это переход по ссылке
        e.preventDefault();

        let productId = null;
        // Получаем классы элемента
        // Разбиваем строку с классами на список отдельных классов
        // Перебираем конкретные классы в цикле forEach, подставляя их в переменную item
        e.target.className.split(' ').forEach(function (item) {
            // если подстрока prod содержится в строке item
            if (item.indexOf('prod') != -1)
                productId = Number(item.split('-')[1]) // получаем id конкретного товара
        });

        console.log(productId);

        $(`.${productId}`).remove();
        //$('.btn').attr('class').split(' ').forEach(function (e) { console.log(e); });
        //'prod-2'.indexOf('prod') != -1;
        //e.target.className
    });
});

})();