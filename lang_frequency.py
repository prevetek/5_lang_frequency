import sys
import string


def load_data(filepath):
    file = open(filepath, 'r')
    text = file.read()
    file.close()
    return text


def get_most_frequent_words(text):
    table = ''.maketrans('', '', string.punctuation)
    words = text.lower().translate(table).split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
        freq_list = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return freq_list


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Укажите путь к файлу с текстом")
    else:
        if len(sys.argv) >= 3:
            print("Много параметров, необходимо указать только путь к файлу с текстом")
        else:
            try:
                text = load_data(sys.argv[1])
                words = get_most_frequent_words(text)
                for num in range(10):
                    print("{0}. {1} = {2}".format(num + 1, words[num][0], words[num][1]))
            except FileNotFoundError:
                print("Указанного файла не существует")
