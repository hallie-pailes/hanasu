from django.shortcuts import render, redirect
from .models import Question
import random



# Create your views here.
def home(request):
    return render(request, "hanasu/home.html", {'active_page': 'home'})

def hiragana(request):
    return render(request, "hanasu/hiragana.html", {'active_page': 'hiragana'})

def katakana(request):
    return render(request, "hanasu/katakana.html", {'active_page': 'katakana'})

def lesson0(request):
    return render(request, "hanasu/lesson0.html", {'active_page': 'lesson'})

def lesson1(request):
    return render(request, "hanasu/lesson1.html", {'active_page': 'lesson'})

hiragana_questions = [
    {"question_text": "あ", "correct_answer": "a"},
    {"question_text": "い", "correct_answer": "i"},
    {"question_text": "う", "correct_answer": "u"},
    {"question_text": "え", "correct_answer": "e"},
    {"question_text": "お", "correct_answer": "o"},
    {"question_text": "か", "correct_answer": "ka"},
    {"question_text": "き", "correct_answer": "ki"},
    {"question_text": "く", "correct_answer": "ku"},
    {"question_text": "け", "correct_answer": "ke"},
    {"question_text": "こ", "correct_answer": "ko"},
    {"question_text": "さ", "correct_answer": "sa"},
    {"question_text": "し", "correct_answer": "shi"},
    {"question_text": "す", "correct_answer": "su"},
    {"question_text": "せ", "correct_answer": "se"},
    {"question_text": "そ", "correct_answer": "so"},
    {"question_text": "た", "correct_answer": "ta"},
    {"question_text": "ち", "correct_answer": "chi"},
    {"question_text": "つ", "correct_answer": "tsu"},
    {"question_text": "て", "correct_answer": "te"},
    {"question_text": "と", "correct_answer": "to"},
    {"question_text": "な", "correct_answer": "na"},
    {"question_text": "に", "correct_answer": "ni"},
    {"question_text": "ぬ", "correct_answer": "nu"},
    {"question_text": "ね", "correct_answer": "ne"},
    {"question_text": "の", "correct_answer": "no"},
    {"question_text": "は", "correct_answer": "ha"},
    {"question_text": "ひ", "correct_answer": "hi"},
    {"question_text": "ふ", "correct_answer": "fu"},
    {"question_text": "へ", "correct_answer": "he"},
    {"question_text": "ほ", "correct_answer": "ho"},
    {"question_text": "ま", "correct_answer": "ma"},
    {"question_text": "み", "correct_answer": "mi"},
    {"question_text": "む", "correct_answer": "mu"},
    {"question_text": "め", "correct_answer": "me"},
    {"question_text": "も", "correct_answer": "mo"},
    {"question_text": "や", "correct_answer": "ya"},
    {"question_text": "ゆ", "correct_answer": "yu"},
    {"question_text": "よ", "correct_answer": "yo"},
    {"question_text": "ら", "correct_answer": "ra"},
    {"question_text": "り", "correct_answer": "ri"},
    {"question_text": "る", "correct_answer": "ru"},
    {"question_text": "れ", "correct_answer": "re"},
    {"question_text": "ろ", "correct_answer": "ro"},
    {"question_text": "わ", "correct_answer": "wa"},
    {"question_text": "を", "correct_answer": "wo"},
    {"question_text": "ん", "correct_answer": "n"},
]

def hiragana_quiz(request, question_number=1):
    # Initialize session variables if not set
    if 'score' not in request.session:
        request.session['score'] = 0  # Initialize score
    if 'incorrect_answers' not in request.session:
        request.session['incorrect_answers'] = []  # Track incorrect answers

    # Shuffle the questions only once when the quiz starts
    if 'shuffled_questions' not in request.session:
        shuffled_questions = hiragana_questions.copy()  # Create a copy to preserve the original order
        random.shuffle(shuffled_questions)  # Shuffle the copied list
        request.session['shuffled_questions'] = shuffled_questions

    # Get the shuffled questions from the session
    shuffled_questions = request.session['shuffled_questions']
    
    # If we've answered all questions, show the result
    if question_number > len(shuffled_questions):
        score = request.session.get('score', 0)
        total_questions = len(shuffled_questions)
        incorrect_answers = request.session.get('incorrect_answers', [])
        request.session.flush()  # Clear session data after quiz completion
        return render(request, 'hanasu/hiragana_result.html', {
            'score': score,
            'total_questions': total_questions,
            'incorrect_answers': incorrect_answers,  # Pass incorrect answers to the results page
 	    'active_page': 'hiragana',
        })

    # Get the current question based on the shuffled list
    question = shuffled_questions[question_number - 1]

    if request.method == 'POST':
        user_answer = request.POST.get('user_answer', '').strip().lower()
        correct_answer = question['correct_answer'].strip().lower()

        # Check if the answer is correct
        if user_answer:
            if user_answer == correct_answer:
                request.session['score'] += 1  # Increment score for correct answer
            return redirect('hiragana_quiz', question_number=question_number + 1)

        # If no answer is provided, reload the same question with an error message
        return render(request, 'hanasu/hiragana_quiz.html', {
            'question': question,
            'question_number': question_number,
            'error_message': "Please enter an answer before submitting.",
	    'active_page': 'hiragana',
        })

    return render(request, 'hanasu/hiragana_quiz.html', {
        'question': question,
        'question_number': question_number,
	'active_page': 'hiragana',
    })


katakana_questions = [
    {"question_text": "ア", "correct_answer": "a"},
    {"question_text": "イ", "correct_answer": "i"},
    {"question_text": "ウ", "correct_answer": "u"},
    {"question_text": "エ", "correct_answer": "e"},
    {"question_text": "オ", "correct_answer": "o"},
    {"question_text": "カ", "correct_answer": "ka"},
    {"question_text": "キ", "correct_answer": "ki"},
    {"question_text": "ク", "correct_answer": "ku"},
    {"question_text": "ケ", "correct_answer": "ke"},
    {"question_text": "コ", "correct_answer": "ko"},
    {"question_text": "サ", "correct_answer": "sa"},
    {"question_text": "シ", "correct_answer": "shi"},
    {"question_text": "ス", "correct_answer": "su"},
    {"question_text": "セ", "correct_answer": "se"},
    {"question_text": "ソ", "correct_answer": "so"},
    {"question_text": "タ", "correct_answer": "ta"},
    {"question_text": "チ", "correct_answer": "chi"},
    {"question_text": "ツ", "correct_answer": "tsu"},
    {"question_text": "テ", "correct_answer": "te"},
    {"question_text": "ト", "correct_answer": "to"},
    {"question_text": "ナ", "correct_answer": "na"},
    {"question_text": "ニ", "correct_answer": "ni"},
    {"question_text": "ヌ", "correct_answer": "nu"},
    {"question_text": "ネ", "correct_answer": "ne"},
    {"question_text": "ノ", "correct_answer": "no"},
    {"question_text": "ハ", "correct_answer": "ha"},
    {"question_text": "ヒ", "correct_answer": "hi"},
    {"question_text": "フ", "correct_answer": "fu"},
    {"question_text": "ヘ", "correct_answer": "he"},
    {"question_text": "ホ", "correct_answer": "ho"},
    {"question_text": "マ", "correct_answer": "ma"},
    {"question_text": "ミ", "correct_answer": "mi"},
    {"question_text": "ム", "correct_answer": "mu"},
    {"question_text": "メ", "correct_answer": "me"},
    {"question_text": "モ", "correct_answer": "mo"},
    {"question_text": "ヤ", "correct_answer": "ya"},
    {"question_text": "ユ", "correct_answer": "yu"},
    {"question_text": "ヨ", "correct_answer": "yo"},
    {"question_text": "ラ", "correct_answer": "ra"},
    {"question_text": "リ", "correct_answer": "ri"},
    {"question_text": "ル", "correct_answer": "ru"},
    {"question_text": "レ", "correct_answer": "re"},
    {"question_text": "ロ", "correct_answer": "ro"},
    {"question_text": "ワ", "correct_answer": "wa"},
    {"question_text": "ヲ", "correct_answer": "wo"},
    {"question_text": "ン", "correct_answer": "n"},
]


def katakana_quiz(request, question_number=1):
    # Initialize session variables if not set
    if 'score' not in request.session:
        request.session['score'] = 0  # Initialize score
    if 'incorrect_answers' not in request.session:
        request.session['incorrect_answers'] = []  # Track incorrect answers

    # Shuffle the questions only once when the quiz starts
    if 'shuffled_questions2' not in request.session:
        shuffled_questions2 = katakana_questions.copy()  # Create a copy to preserve the original order
        random.shuffle(shuffled_questions2)  # Shuffle the copied list
        request.session['shuffled_questions2'] = shuffled_questions2

    # Get the shuffled questions from the session
    shuffled_questions = request.session['shuffled_questions2']
    
    # If we've answered all questions, show the result
    if question_number > len(shuffled_questions):
        score = request.session.get('score', 0)
        total_questions = len(shuffled_questions)
        incorrect_answers = request.session.get('incorrect_answers', [])
        request.session.flush()  # Clear session data after quiz completion
        return render(request, 'hanasu/katakana_result.html', {
            'score': score,
            'total_questions': total_questions,
            'incorrect_answers': incorrect_answers,  # Pass incorrect answers to the results page
 	    'active_page': 'katakana',
        })

    # Get the current question based on the shuffled list
    question = shuffled_questions[question_number - 1]

    if request.method == 'POST':
        user_answer = request.POST.get('user_answer', '').strip().lower()
        correct_answer = question['correct_answer'].strip().lower()

        # Check if the answer is correct
        if user_answer:
            if user_answer == correct_answer:
                request.session['score'] += 1  # Increment score for correct answer
            return redirect('katakana_quiz', question_number=question_number + 1)

        # If no answer is provided, reload the same question with an error message
        return render(request, 'hanasu/katakana_quiz.html', {
            'question': question,
            'question_number': question_number,
            'error_message': "Please enter an answer before submitting.",
	    'active_page': 'katakana',
        })

    return render(request, 'hanasu/katakana_quiz.html', {
        'question': question,
        'question_number': question_number,
	'active_page': 'katakana',
    })


def greetings_quiz(request, question_number=1):
    # Define the pool of all possible answers (correct and incorrect ones)
    answers_pool = [
        'おはよう', 'おはよう　ございま。', 'こんにちは', 'こんばんは', 'さようなら', 'おやすみ（なさい）', 'ありがとう', 'ありがとう　ございます', 'すみません', 'いいえ', 'いってきます', 'いってらっしゃい', 'ただいま', 'おかえり（なさい）', 'いただきます', 'ごちそうさま（でした）', 'はじめまして', '～です', 'よろしく　おねがいします'
    ]
    
    # Define the questions and their correct answers
    questions = [
        {'question': 'How do you say: Good morning (Casual)?', 'correct_answer': 'おはよう'},
        {'question': 'How do you say: Good morning (Polite)?', 'correct_answer': 'おはよう　ございます'},
        {'question': 'How do you say: Good afternoon?', 'correct_answer': 'こんにちは'},
        {'question': 'How do you say: Good evening?', 'correct_answer': 'こんばんは'},
        {'question': 'How do you say: Good-bye?', 'correct_answer': 'さようなら'},
        {'question': 'How do you say: Good night?', 'correct_answer': 'おやすみ（なさい）'},
        {'question': 'How do you say: Thank you (Casual)?', 'correct_answer': 'ありがとう'},
        {'question': 'How do you say: Thank you (Polite)?', 'correct_answer': 'ありがとう　ございます'},
        {'question': 'How do you say: Excuse me/I\'m sorry?', 'correct_answer': 'すみません'},
        {'question': 'How do you say: No/Not at all?', 'correct_answer': 'いいえ'},
        {'question': 'How do you say: I\'ll go and come back?', 'correct_answer': 'いってきます'},
        {'question': 'How do you say: Please go and come back?', 'correct_answer': 'いってらっしゃい'},
        {'question': 'How do you say: I\'m home?', 'correct_answer': 'ただいま'},
        {'question': 'How do you say: Welcome home?', 'correct_answer': 'おかえり（なさい）'},
        {'question': 'How do you say: Thank you for the meal (before eating)?', 'correct_answer': 'いただきます'},
        {'question': 'How do you say: Thank you for the meal (after eating)?', 'correct_answer': 'ごちそうさま（でした）'},
        {'question': 'How do you say: How do you do?', 'correct_answer': 'はじめまして'},
        {'question': 'How do you say: I am...?', 'correct_answer': '～です'},
        {'question': 'How do you say: Nice to meet you?', 'correct_answer': 'よろしく　おねがいします'},
        # Add more questions here...
    ]
    

    # Initialize session variables if not set
    if 'score' not in request.session:
        request.session['score'] = 0  # Initialize score
    if 'incorrect_answers' not in request.session:
        request.session['incorrect_answers'] = []  # Track incorrect answers

    # If we've answered all questions, show the result
    if question_number > len(questions):
        score = request.session.get('score', 0)
        total_questions = len(questions)
        incorrect_answers = request.session.get('incorrect_answers', [])
        request.session.flush()  # Clear session data after quiz completion
        return render(request, 'hanasu/greetings_result.html', {
            'score': score,
            'total_questions': total_questions,
            'incorrect_answers': incorrect_answers,  # Pass incorrect answers to the results page
 	    'active_page': 'lesson',
        })

    # Get the question for the given number
    question = questions[question_number - 1]  # Adjusting because lists are 0-indexed
    
    # Choose the correct answer
    correct_answer = question['correct_answer']
    
    # Remove the correct answer from the pool to avoid repetition
    choices_pool = [answer for answer in answers_pool if answer != correct_answer]
    
    # Randomly select 3 incorrect answers from the pool
    incorrect_answers = random.sample(choices_pool, 3)
    
    # Combine the correct answer with the incorrect ones and randomize the order
    all_choices = [correct_answer] + incorrect_answers
    random.shuffle(all_choices)
    
    # Handle form submission and check the answer
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        if user_answer == correct_answer:
            result = 'Correct!'
            request.session['score'] += 1
        else:
            result = f'Wrong! The correct answer was {correct_answer}.'
        
        # Redirect to the next question
        next_question_number = question_number + 1
        return redirect('greetings_quiz', question_number=next_question_number)  # Ensure 'greetings_quiz' is the correct URL name
    
    # Initial page load
    return render(request, 'hanasu/greetings_quiz.html', {
        'question': question['question'],
        'choices': all_choices,
        'question_number': question_number,
        'active_page': 'lesson'
    })


numbers_questions = [
    {"question_text": "ゼロ/れい", "correct_answer": "0"},
    {"question_text": "いち", "correct_answer": "1"},
    {"question_text": "に", "correct_answer": "2"},
    {"question_text": "さん", "correct_answer": "3"},
    {"question_text": "よん/し", "correct_answer": "4"},
    {"question_text": "ご", "correct_answer": "5"},
    {"question_text": "ろく", "correct_answer": "6"},
    {"question_text": "なな/しち", "correct_answer": "7"},
    {"question_text": "はち", "correct_answer": "8"},
    {"question_text": "きゅう/く", "correct_answer": "9"},
    {"question_text": "じゅう", "correct_answer": "10"},
]
def numbers_quiz(request, question_number=1):
    # Initialize session variables if not set
    if 'score' not in request.session:
        request.session['score'] = 0  # Initialize score
    if 'incorrect_answers' not in request.session:
        request.session['incorrect_answers'] = []  # Track incorrect answers

    # Shuffle the questions only once when the quiz starts
    if 'shuffled_questions3' not in request.session:
        shuffled_questions3 = numbers_questions.copy()  # Create a copy to preserve the original order
        random.shuffle(shuffled_questions3)  # Shuffle the copied list
        request.session['shuffled_questions3'] = shuffled_questions3

    # Get the shuffled questions from the session
    shuffled_questions = request.session['shuffled_questions3']
    
    # If we've answered all questions, show the result
    if question_number > len(shuffled_questions):
        score = request.session.get('score', 0)
        total_questions = len(shuffled_questions)
        incorrect_answers = request.session.get('incorrect_answers', [])
        request.session.flush()  # Clear session data after quiz completion

        return render(request, 'hanasu/numbers_result.html', {
            'score': score,
            'total_questions': total_questions,
            'incorrect_answers': incorrect_answers,  # Pass incorrect answers to the results page
 	    'active_page': 'lesson',
        })

    # Get the current question based on the shuffled list
    question = shuffled_questions[question_number - 1]

    if request.method == 'POST':
        user_answer = request.POST.get('user_answer', '').strip().lower()
        correct_answer = question['correct_answer'].strip().lower()

        # Check if the answer is correct
        if user_answer:
            if user_answer == correct_answer:
                request.session['score'] += 1  # Increment score for correct answer
            return redirect('numbers_quiz', question_number=question_number + 1)

        # If no answer is provided, reload the same question with an error message
        return render(request, 'hanasu/numbers_quiz.html', {
            'question': question,
            'question_number': question_number,
            'error_message': "Please enter an answer before submitting.",
	    'active_page': 'lesson',
        })

    return render(request, 'hanasu/numbers_quiz.html', {
        'question': question,
        'question_number': question_number,
	'active_page': 'lesson',
    })

