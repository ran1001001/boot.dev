def filter_messages(messages):
    filtered_messages = []
    word_count = []
    bad_words = ['fucking', 'fuck', 'dang', 'deeznuts']
    for message in messages:
        sentence = message.split()
        filtered_sentence = []
        counter = 0
        for word in sentence:
            if word.lower() in bad_words:
                counter += 1
                asterisk = len(word) * '*'
                filtered_sentence.append(asterisk)
                continue
            filtered_sentence.append(word)
        filtered_messages.append(" ".join(filtered_sentence))
        word_count.append(counter)
        
    return filtered_messages, word_count

# Don't edit below this line


def main():
    messages = [
        "well fuck it, dang it",
        "dang the whole fucking thing",
        "kill that knight, dang it",
        "get him!",
        "donkey kong",
        "oh come on, get them",
        "run away from DeezNuts",
    ]
    filtered_messages, words_removed = filter_messages(messages)
    if len(filtered_messages) != len(words_removed):
        print("filtered_messages and words_removed lists should be the same size")
        return
    for i in range(0, len(filtered_messages)):
        print(
            f"Removed {words_removed[i]} words. Censored text: '{filtered_messages[i]}'"
        )


main()


