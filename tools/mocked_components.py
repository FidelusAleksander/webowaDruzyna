def get_form_source1():
    # Dane z SQL
    # Na podstawie tego stworzyć formularz z podanymi pytaniami i odpowiedziami, po zatwierdzeniu wysłać HTTP POST
    return [
        {
            "question_id": 1,
            "question_text": "Czy poleciłbyś Inżynierię Biomedyczną koledze?",
            "possible_answers": {
                0: "Tak",
                1: "Nie",
                2: "Nie wiem",
                3: "ŻŹĆŃĄĘŁÓ"
            }
        },
        {
            "question_id": 0,
            "question_text": "Jak bardzo coś tam...",
            "possible_answers": {
                4: '1',
                5: '2',
                6: '3',
                7: '4',
                8: '5'
            }
        }
    ]

def form_results1():
    # Zwrócone przez formularz, wysłane metodą HTTP POST i wrzucone do SQL
    # lista AnswerID z possible_answers
    return [2, 3]


def get_all_plots_data():
    # dane do wykresu
    # kto to będzie robił musi sobie wymyślić w jakiej formie chce mieć dane, raczej tu nie ma ograniczeń
    #
    return {
        "gender_pie_plot": {
            "male": 43.7,
            "female": 56.3
        },
        "specialty_pie_plot": {
            "ib": 13.4,
            "it": 55.3,
            "bi": 31.3
        }
    }
