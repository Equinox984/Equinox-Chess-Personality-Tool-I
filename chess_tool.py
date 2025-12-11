"""Equinox Chess Personality Tool"""


def get_rating(question):
    """Request a response from 1 to 3 and validate the entry."""
    while True:
        answer = input(question + " (1 = Low, 2 = Mid, 3 = High) ").strip()
        if answer in {"1", "2", "3"}:
            return int(answer)
        print("Invalid response. We only accept 1, 2, or 3 as an answer.")


chess_questions = {
    "Tactician": [
        "1. I enjoy looking for sacrifices and sharp combinations to break my opponent.",
        "2. I feel confident calculating long tactical lines under time pressure.",
        "3. I often create complications on purpose to provoke mistakes.",
        "4. I prioritize winning material or delivering mating attacks over long-term structure.",
        "5. I spot tactical motifs (pins, forks, skewers) quickly in most positions.",
        "6. I get frustrated by dry, closed positions with no tactical chances.",
    ],
    "Positional": [
        "7. I prefer improving piece placement and slowly outplaying my opponent.",
        "8. I focus on pawn structure, weak squares, and long-term plans rather than immediate tactics.",
        "9. I willingly trade active pieces if it improves my structure or reduces opponent counterplay.",
        "10. I am comfortable playing slow maneuvering games where progress is small but steady.",
        "11. I study endgames and often convert small advantages into wins.",
        "12. I avoid risky sacrifices unless they have a clear justification.",
    ],
    "Dynamic": [
        "13. I feel comfortable in imbalanced positions with opposite-side attacks or material differences.",
        "14. I look for the initiative and prefer forcing play even if it's risky.",
        "15. I willingly accept weakened pawns or structural defects for active piece play.",
        "16. I thrive when the position becomes unclear and chaotic.",
        "17. I often choose sharp, less-traveled lines to take opponents out of comfort zones.",
        "18. I sometimes overpress or overcomplicate hoping the opponent blunders.",
    ],
    "Theorist": [
        "19. I memorize opening lines and feel most confident when the game follows theory.",
        "20. I prepare specific lines to gain an advantage in the first 15–20 moves.",
        "21. I frequently study master games, opening novelties, and database lines.",
        "22. I prefer positions where my preparation gives practical advantages.",
        "23. I feel annoyed when opponents play weird sidelines that force me to think from scratch.",
        "24. I value known theoretical knowledge more than relying purely on over-the-board intuition.",
    ],
    "Intuitive": [
        "25. I play moves that 'feel right' even if I can't fully calculate every variation.",
        "26. I trust my positional sense to find plans without heavy memorization.",
        "27. I often make moves based on whole-position understanding rather than concrete tactics alone.",
        "28. I adapt quickly to the flow of the game and rely on pattern recognition.",
        "29. I sometimes can't explain my best moves verbally but they work on the board.",
        "30. I prefer flexible systems and moves that keep many plans alive.",
    ],
}

openings = {
    "Tactician": "King's Gambit (White) / Sicilian Dragon (Black)",
    "Positional": "Queen's Gambit (White) / Caro-Kann (Black)",
    "Dynamic": "London System (White) / King's Indian Defense (Black)",
    "Theorist": "Ruy López (White), Sicilian Najdorf (Black)",
    "Intuitive": "English Opening (White), Dutch Defense (Black)",
}


if __name__ == "__main__":
    username = input("Hello, please write your name: \n")
    print(f"Hello {username}!, Welcome to Equinox Chess Personality Tool! \n")

    print("Answer the following questions to find out your chess personality type.\n")

    styles_value = {chess_style: 0 for chess_style in chess_questions.keys()}

    for chess_style, questions in chess_questions.items():
        for q in questions:
            points = get_rating(q)
            styles_value[chess_style] += points

    max_points = max(styles_value.values())
    best_styles = [
        chess_style for chess_style, pts in styles_value.items() if pts == max_points
    ]

    print("\n### Results ###")
    if len(best_styles) > 1:
        print(f"Hello {username}!, you have a tie between: {', '.join(best_styles)}!")
        print(f"Recommended openings for {best_styles[0]}: {openings[best_styles[0]]}")
    else:
        primary_style = best_styles[0]
        print(f"Hello {username}!, your primary chess style is: {primary_style}!")
        print(f"Recommended openings: {openings[primary_style]}")

    print(f"Total points by style: {styles_value}")
