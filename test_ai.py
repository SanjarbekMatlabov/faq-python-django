import requests
import json
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1"

SYSTEM_PROMPT = (
    "Sen tajribali dasturlash mentori va yordamchi assistantsan. "
    "Berilgan savolga aniq, tushunarli va foydali javob ber. "
    "Javobni o‘zbek tilida yoz. "
    "Qisqa, lekin yetarlicha tushuntir. "
    "Keraksiz kirish so‘zlari yozma. "
    "Faqat javobni qaytar."
)

def answer_question_ollama(question: str):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        "stream": False,
        "options": {
            "temperature": 0.3
        }
    }

    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()
    return r.json()["message"]["content"].strip()
print(
    answer_question_ollama(
        "SQL bo‘limiga qachon dostup ochiladi?"
    )
)
def generate_answers(faq_list):
    result = []

    for item in faq_list:
        try:
            answer = answer_question_ollama(item["question"])
            result.append({
                **item,
                "answer": answer
            })
        except Exception as e:
            print("Xato:", e)
            result.append({
                **item,
                "answer": "Bu savol bo‘yicha hozircha aniq ma’lumot yo‘q."
            })

    return result


with open("faq_top_dbscan.json", "r", encoding="utf-8") as f:
    faq = json.load(f)

faq_with_answers = generate_answers(faq)

with open("faq_top_dbscan_answered.json", "w", encoding="utf-8") as f:
    json.dump(faq_with_answers, f, ensure_ascii=False, indent=2)

print("✅ FAQ javoblar bilan saqlandi")