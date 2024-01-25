from text_to_num import text2num
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Включаем CORS (Cross-Origin Resource Sharing) для обработки запросов из браузера
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Переменная, в которую будет сохраняться строка для вычислений
str_to_count = ''

# Словарь для сопоставления слов-операторов с математическими операторами
operator_dict = {
    'плюс': '+',
    'минус': '-',
    'умножить': '*',
    'делить': '/'
}

# Список слов-операторов
operator_words = list(operator_dict.keys())

@app.post("/calculate")
async def str_to_int(text: str = Body(embed=True)):
    """
    Основная функция обработки текста

    Принимает текстовую строку с математическим выражением на русском языке
    и возвращает результат вычислений.
    """
    try:
        word_itog = ''
        int_str = ''
        # Разбиваем текст на слова, исключая предлоги 'на'
        sort_text = [word for word in text.split() if word != 'на']
        for word in sort_text:
            if word in operator_words:
                word_itog += str(text2num(int_str, "ru"))
                word_itog += operator_dict[word]
                int_str = ''
            else:
                int_str += ' ' + word
        word_itog += str(text2num(int_str, "ru"))
        # Используем eval для вычисления результата математического выражения
        return {"result": eval(word_itog)}
    except:
        # В случае ошибки возвращаем пустую строку
        return {"result": ""}

