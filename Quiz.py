# By Raj Shekhar Aryal
# Simple Quiz game in python

quiz = {
    "question1": {
        "question": "What is the capital city of Nepal?",
        "answer": "Kathmandu"
    },
    "question2": {
        "question": "What is the highest mountain in Nepal?",
        "answer": "Mount Everest"
    },
    "question3": {
        "question": "What is the national flower of Nepal?",
        "answer": "Rhododendron"
    },
    "question4": {
        "question": "What is the national animal of Nepal?",
        "answer": "Cow"
    },
    "question5": {
        "question": "What is the national bird of Nepal?",
        "answer": "Himalayan Monal"
    },
    "question6": {
        "question": "Which river is considered the longest in Nepal?",
        "answer": "Karnali"
    },
    "question7": {
        "question": "What is the official language of Nepal?",
        "answer": "Nepali"
    },
    "question8": {
        "question": "Which city is known as the gateway to the Annapurna region?",
        "answer": "Pokhara"
    },
    "question9": {
        "question": "What is the currency of Nepal?",
        "answer": "Nepalese Rupee"
    },
    "question10": {
        "question": "In which year did Nepal become a federal democratic republic?",
        "answer": "2008"
    },
    "question11": {
        "question": "Which UNESCO World Heritage site is located in Lumbini?",
        "answer": "Birthplace of Buddha"
    },
    "question12": {
        "question": "What is the name of Nepal's largest national park?",
        "answer": "Shey Phoksundo National Park"
    },
    "question13": {
        "question": "Which district is home to Mount Everest?",
        "answer": "Solukhumbu"
    },
    "question14": {
        "question": "What is the second largest city in Nepal by population?",
        "answer": "Pokhara"
    },
    "question15": {
        "question": "Which famous lake is located in Pokhara?",
        "answer": "Phewa Lake"
    },
    "question16": {
        "question": "Who is known as the first king of unified Nepal?",
        "answer": "Prithvi Narayan Shah"
    },
    "question17": {
        "question": "Which city is famous for Janaki Temple?",
        "answer": "Janakpur"
    },
    "question18": {
        "question": "What is the national sport of Nepal?",
        "answer": "Volleyball"
    },
    "question19": {
        "question": "Which wildlife reserve is famous for one-horned rhinoceroses?",
        "answer": "Chitwan National Park"
    },
    "question20": {
        "question": "What is the name of Nepal's international airport in Kathmandu?",
        "answer": "Tribhuvan International Airport"
    }
}

score = 0

for keys, value in quiz.items():
    print(value['question'])
    answer = input('Answer:')

    if answer.lower() == value['answer'].lower():
        score = score + 1
        print('Correct')
        print("Your current score is : " + str(score))

    else:
        print("Your answer is incorrect")
        print("Correct answer is " + value['answer'] )
