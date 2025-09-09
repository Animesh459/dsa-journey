def lecture_notes(n, m, languages, lecture):
    """
    Determines how a lecture will be recorded in notes based on word length.

    Args:
        n: The number of words in the lecture.
        m: The number of words in each language.
        languages: A list of tuples, where each tuple contains a pair of words
                   from the two languages that have the same meaning.
        lecture: A list of words from the lecture.

    Returns:
        A list of words representing the recorded lecture.
    """
    word_map = {}
    for a, b in languages:
        if len(b) < len(a):
            word_map[a] = b
        else:
            word_map[a] = a

    notes = []
    for word in lecture:
        notes.append(word_map[word])

    return notes


def main():
    try:
        n, m = map(int, input().split())

        languages = []
        for _ in range(m):
            a, b = input().split()
            languages.append((a, b))

        lecture = input().split()

        result = lecture_notes(n, m, languages, lecture)
        print(*result)

    except (IOError, ValueError) as e:
        print(f"An error occurred: {e}")
        # Optionally, you can handle the error more gracefully or just exit.


if __name__ == "__main__":
    main()