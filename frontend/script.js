const math = require('mathjs');

function calculateText(str) {
    // Парсим математическое выражение из строки
    const exp = math.parse(str);

    // Вычисляем значение выражения
    const result = exp.evaluate();

    return result;
}

// Пример использования
const inputstr = "two plus three";
const result = calculateText(inputstr);

console.log(`Результат: ${result}`);