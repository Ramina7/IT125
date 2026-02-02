class Quiz:
    def __init__(self):
        self.questions = [
            {"question":"Столица Испании?","options":["Барселона","Мадрид","Валенсия","Севилья"],"correct":"Мадрид","image":"https://picsum.photos/300/200?21"},
            {"question":"3 * 3 = ?","options":["6","9","12","3"],"correct":"9","image":"https://picsum.photos/300/200?22"},
            {"question":"Самая маленькая планета?","options":["Марс","Меркурий","Плутон","Венера"],"correct":"Меркурий","image":"https://picsum.photos/300/200?23"},
            {"question":"Столица Канады?","options":["Оттава","Торонто","Ванкувер","Монреаль"],"correct":"Оттава","image":"https://picsum.photos/300/200?24"},
            {"question":"8 + 5 = ?","options":["11","12","13","14"],"correct":"13","image":"https://picsum.photos/300/200?25"},
            {"question":"Самый быстрый зверь?","options":["Лев","Гепард","Тигр","Волк"],"correct":"Гепард","image":"https://picsum.photos/300/200?26"},
            {"question":"Столица Китая?","options":["Шанхай","Пекин","Гонконг","Ухань"],"correct":"Пекин","image":"https://picsum.photos/300/200?27"},
            {"question":"6 * 7 = ?","options":["42","36","48","49"],"correct":"42","image":"https://picsum.photos/300/200?28"},
            {"question":"Самое глубокое озеро?","options":["Байкал","Каспий","Онтарио","Титикака"],"correct":"Байкал","image":"https://picsum.photos/300/200?29"},
            {"question":"Столица Бразилии?","options":["Рио","Сан-Паулу","Бразилиа","Салвадор"],"correct":"Бразилиа","image":"https://picsum.photos/300/200?30"},
            {"question":"9 + 1 = ?","options":["8","9","10","11"],"correct":"10","image":"https://picsum.photos/300/200?31"},
            {"question":"Самая большая пустыня?","options":["Сахара","Гоби","Атакама","Калахари"],"correct":"Сахара","image":"https://picsum.photos/300/200?32"},
            {"question":"Столица Египта?","options":["Каир","Александрия","Гиза","Луксор"],"correct":"Каир","image":"https://picsum.photos/300/200?33"},
            {"question":"7 + 8 = ?","options":["14","15","16","17"],"correct":"15","image":"https://picsum.photos/300/200?34"},
            {"question":"Самая длинная горная система?","options":["Анды","Альпы","Гималаи","Урал"],"correct":"Анды","image":"https://picsum.photos/300/200?35"},
        ]

    def get_question(self,index):
        if index < len(self.questions):
            return self.questions[index]
        return None

    def total_questions(self):
        return len(self.questions)