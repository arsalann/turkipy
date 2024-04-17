import pandas as pd
import numpy as np


def loop_words(df, number_of_words):
    correct = 0
    wrong = 0
    word_ids = np.random.randint(0, len(df), int(number_of_words))

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
    print('Categories:')
    print('\n'.join(str(item) for item in df['kategori'].unique()))
    kategori = input('Do you want to practice all words or a specific category? (i.e. "all" or name of category) ')

    # print all the subcategories line by line
    print('Subcategories:')
    print('\n'.join(str(item) for item in df['altkategori'].unique()))
    altkategori = input('Do you want to practice all words or a specific subcategory? (i.e. "all" or name of subcategory) ')

    if kategori != 'all':
        df = df[df['kategori'] == kategori]
        df = df.reset_index(drop=True)

    if altkategori != 'all':
        df = df[df['altkategori'] == altkategori]
        df = df.reset_index(drop=True)

    print(f'Number of words in the dictionary: {len(df)}')
    number_of_words = input('How many words do you want to practice? ')

    return df, number_of_words

def main():

    practice = input('What do you want to practice? ')

    if practice == 'kelime':
        df, number_of_words = practice_words()
        loop_words(df, number_of_words)

if __name__ == '__main__':
    main()
