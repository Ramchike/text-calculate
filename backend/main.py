from text_to_num import text2num
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

str_to_count = ''

operator_dict = {
    'плюс': '+',
    'минус': '-',
    'умножить': '*',
    'делить': '/'
}
operator_words = list(operator_dict.keys())

@app.post("/calculate")
async def str_to_int(text: str = Body(embed=True)):
    try:
        word_itog = ''
        int_str = ''
        sort_text = [word for word in text.split() if word != 'на']
        for word in sort_text:
            if word in operator_words:
                word_itog += str(text2num(int_str, "ru"))
                word_itog += operator_dict[word]
                int_str = ''
            else:
                int_str += ' ' + word
        word_itog += str(text2num(int_str, "ru"))
        return {"result": eval(word_itog)}
    except: return {"result": ""}

