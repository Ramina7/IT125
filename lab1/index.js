// 1 студент
const student = {
    name: "Рамина",
    surname: "Машанло",
    group: "IT-125",
    currentMonth: 1,
    isGraduate: false,
    direction: "Информационные технологии",
    monthsStudied: 12
  };
  
  
//   // 2 банковский счет
//   const bankAccount = {
//     accountNumber: "123456789",
//     currency: "KG",
//     balance: 100000000,
//     ownerName: "Рамина Машанло",
//     isBlocked: false
//   };
  
  
//   // 3 приветствие 
//   const firstName = prompt("Введите ваше имя:");
//   const lastName = prompt("Введите вашу фамилию:");
  
//   console.log(`Здравствуйте, ${firstName} ${lastName}!`);
  
  
//   // 4 сравнение чисел
//   const number1 = Number(prompt("Введи первое число:"));
//   const number2 = Number(prompt("Введи второе число:"));
  
//   if (number1 > number2) {
//     console.log("Первое число больше");
//   } else if (number2 > number1) {
//     console.log("Второе число больше");
//   } else {
//     console.log("Числа равны");
//   }
  
  
//   // 5 светофор
//   const color = prompt("Введите цвет светофора:").toLowerCase();
  
//   if (color === "красный") {
//     console.log("стой!");
//   } else if (color === "желтый") {
//     console.log("жди!");
//   } else if (color === "зеленый") {
//     console.log("иди!");
//   } else {
//     console.log("такого цвета нет");
//   }
  
  
// // 6 конвертер чисел
//   const number = Number(prompt("Введите число от 1 до 9:"));
  
//   const romanNumbers = {
//     1: "I",
//     2: "II",
//     3: "III",
//     4: "IV",
//     5: "V",
//     6: "VI",
//     7: "VII",
//     8: "VIII",
//     9: "IX"
//   };
  
//   if (number >= 1 && number <= 9) {
//     console.log(romanNumbers[number]);
//   } else {
//     console.log("Введите число от 1 до 9");
//   }


//  // 7 таблица умножения

// const numberForTable = Number(prompt("Введите число от 2 до 10:"));

// if (numberForTable >= 2 && numberForTable <= 10) {
//     for (let i = 1; i <= 10; i++) {
//         console.log(numberForTable + " × " + i + " = " + numberForTable * i);
//     }
// } else {
//     console.log("Введите число от 2 до 10");
// }


// // 8 банковские карты

// const cards = [
//     "46782346",
//     "45781218",
//     "79874568",
//     "12157845",
//     "36151845",
//     "41250895",
//     "41201961"
// ];

// let visaCards = 0;

// for (let i = 0; i < cards.length; i++) {
//     if (cards[i][0] === "4") {
//         visaCards++;
//     }
// }

// console.log("Карт VISA " + visaCards + " из " + cards.length + ".");