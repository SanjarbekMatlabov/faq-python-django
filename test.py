import json

HASHTAG = "#mentor"

with open("result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

mentor_messages = []

for msg in data.get("messages", []):
    # faqat oddiy xabarlar
    if msg.get("type") == "message":
        text = msg.get("text")

        # text string yoki list bo‘lishi mumkin
        if isinstance(text, str):
            if HASHTAG in text:
                mentor_messages.append(msg)

        elif isinstance(text, list):
            full_text = "".join(
                part["text"] if isinstance(part, dict) else part
                for part in text
            )
            if HASHTAG in full_text:
                mentor_messages.append(msg)

print(f"Topilgan xabarlar soni: {len(mentor_messages)}")

# Natijani alohida faylga saqlash
with open("mentor_messages.json", "w", encoding="utf-8") as f:
    json.dump(mentor_messages, f, ensure_ascii=False, indent=2)
