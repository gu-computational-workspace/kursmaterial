def run_quiz():
    # Lista med frågor och svar
    questions = [
        {
            "question": "Vilket är Sveriges största stad?",
            "options": ["1) Stockholm", "2) Göteborg", "3) Malmö", "4) Örebro"],
            "answer": 1
        },
        {
            "question": "Vilket år blev Gustav Vasa kung?",
            "options": ["1) 1523", "2) 1600", "3) 1492", "4) 1809"],
            "answer": 1
        },
        {
            "question": "Vad heter Sveriges nationalblomma?",
            "options": ["1) Blåklocka", "2) Prästkrage", "3) Linnea", "4) Smörblomma"],
            "answer": 1
        }
    ]

    # Variabler för poängräkning
    score = 0

    print("Välkommen till quizzet!")
    print("------------------------")

    # Loopa igenom frågorna
    for idx, q in enumerate(questions):
        print(f"Fråga {idx + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Användarens svar
        while True:
            try:
                user_answer = int(input("Skriv numret på ditt svar: "))
                if 1 <= user_answer <= len(q['options']):
                    break
                else:
                    print("Felaktigt val. Försök igen.")
            except ValueError:
                print("Ogiltigt inmatning. Skriv ett nummer.")
        
        # Kontrollera om svaret är korrekt
        if user_answer == q['answer']:
            print("Rätt svar! 🎉")
            score += 1
        else:
            print(f"Fel svar. Rätt svar är alternativ {q['answer']}.")
        print()

    # Visa slutpoängen
    print("------------------------")
    print(f"Du fick {score} av {len(questions)} rätt!")
    if score == len(questions):
        print("Fantastiskt jobb! ⭐")
    elif score > 0:
        print("Bra jobbat! Försök igen för full poäng!")
    else:
        print("Bättre lycka nästa gång!")

# Starta quizzet
if __name__ == "__main__":
    run_quiz()