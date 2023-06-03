var groupmates = [
    {
        "name": "Павел",
        "surname": "Иванов",
        "group": "БВТ2309",
        "marks": [2, 3, 3]
    },
    {
        "name": "Ярослав",
        "surname": "Петров",
        "group": "БВТ2309",
        "marks": [4, 2, 3]
    },
    {
        "name": "Василий",
        "surname": "Смирнов",
        "group": "БФИ2402",
        "marks": [5, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Никитин",
        "group": "БФИ2402",
        "marks": [4, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Семёнов",
        "group": "БФИ2402",
        "marks": [5, 5, 5]
    }
];

var rpad = function(str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет 
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки return str; // когда все пробелы добавлены, возвратить строку
    return str;
    };
    
var printStudents = function(students) { 
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i<=students.length-1; i++){
    // в цикле выводится каждый экземпляр студента 
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
    };

var filterByGroup = function (students, group) {
    var mas = [];
    for (var i = 0; i <= students.length - 1; i++) {
        if (students[i]["group"] == group) {
            mas.push(students[i]);
        }
    }
    return mas;
}

var filterByMiddleMark = function (students, middleMark) {
    var mas = [];
    var mark = 0;
    for (var i = 0; i <= students.length - 1; i++) {
        mark = students[i]['marks'][0] + students[i]['marks'][1] + students[i]['marks'][2];
        if ((mark / 3) >= middleMark) {
            mas.push(students[i])
        }
    }
    return mas;
}

var group = prompt("Введите номер нужной группы.");
printStudents(filterByGroup(groupmates, group));
var mark = Number(prompt("Введите минимальный средний балл."));
printStudents(filterByMiddleMark(groupmates, mark));
