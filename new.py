import json

# Kiruvchi fayl
with open("faq_pairwise.json", "r", encoding="utf-8") as f:
    data = json.load(f)

only_questions = []

for item in data:
    only_questions.append({
        "faq_id": item.get("faq_id"),
        "question": item.get("question")
    })

# Yangi faylga saqlash
with open("faq_questions_only.json", "w", encoding="utf-8") as f:
    json.dump(only_questions, f, ensure_ascii=False, indent=2)

print("✅ faq_questions_only.json saqlandi")
