import pandas as pd
import numpy as np


def loop_words(df, number_of_words, unique):
    correct = 0
    wrong = 0
    word_ids = np.random.randint(0, len(df), int(number_of_words))
    if unique == 'True':
        word_ids = np.random.choice(len(df), int(number_of_words), replace=False)

    for word_id in word_ids:
        # Select the column based on whether word_id is even or odd
        target_column = 'kelime' if word_id % 2 == 0 else 'anlam'
        opposite_column = 'anlam' if target_column == 'kelime' else 'kelime'

        # Retrieve the target word and prompt the user
        target_word = df.loc[word_id, target_column]
        response = input(f'{target_word} ~> ')

        # Retrieve all matching words from the opposite column
        matching_words = df.loc[df[target_column] == target_word, opposite_column].values

        # Check if the response is among the matching words
        if response in matching_words:
            correct += 1
        else:
            wrong += 1
            correct_word = df.loc[word_id, opposite_column]
            print(f'\033[91m{target_word} ~> {correct_word}\033[0m')

    print(f'Correct: {correct}')
    print(f'Wrong: {wrong}')
    print(f'Total: {correct + wrong}')
    print(f'Accuracy: {correct / (correct + wrong) * 100}%')

def practice_words():
    dictionary_file = 'dictionary.csv'
    df = pd.read_csv(dictionary_file, encoding='utf-8')

    # print all the categories line by line
    print('Chapters:')
    print('\n'.join(str(item) for item in df['chapter'].unique()))
    chapter = input('Do you want to practice all words or a specific chapter? (i.e. "all" or name of category) ')

    # print all the categories line by line
    print('Categories:')
    print('\n'.join(str(item) for item in df['kategori'].unique()))
    kategori = input('Do you want to practice all words or a specific category? (i.e. "all" or name of category) ')

    # print all the subcategories line by line
    print('Subcategories:')
    print('\n'.join(str(item) for item in df['altkategori'].unique()))
    altkategori = input('Do you want to practice all words or a specific subcategory? (i.e. "all" or name of subcategory) ')

    if chapter != 'all':
        df = df[df['chapter'] == chapter]
        df = df.reset_index(drop=True)

    if kategori != 'all':
        df = df[df['kategori'] == kategori]
        df = df.reset_index(drop=True)

    if altkategori != 'all':
        df = df[df['altkategori'] == altkategori]
        df = df.reset_index(drop=True)

    print(f'Number of words in the dictionary: {len(df)}')
    number_of_words = input('How many words do you want to practice? ')
    unique = input('Do you want only unique words? (True or False) ')

    return df, number_of_words, unique

def main():
    phrases_file = 'phrases.csv'
    practice = input('What do you want to practice? ')

    if practice == 'kelime':
        df, number_of_words, unique = practice_words()
        loop_words(df, number_of_words, unique)

    elif practice == 'cumle':
        df = pd.read_csv(phrases_file, encoding='utf-8')

        number_of_phrases = input('How many phrases do you want to practice? ')

        # create n number of random numbers based on the number_of_phrases
        phrase_ids = np.random.randint(0, len(df), int(number_of_phrases))

        for phrase_id in phrase_ids:
            # get the phrase from the cumle column in dataframe
            x = df.loc[phrase_id, 'cumle']
            response = input(f'{x} ~> ')

            if response == df.loc[phrase_id, 'anlam']:
                continue
            else:
                # print in red color
                print(f'\033[91m{x} ~> {df.loc[phrase_id, "anlam"]}\033[0m')
if __name__ == '__main__':
    main()
