import pandas as pd
import numpy as np






def get_word(word):
    row = df.loc[df['kelime'] == word]
    result = f"""
    kelime: {row['kelime'].values[0]}
    anlam: {row['anlam'].values[0]}
    kategori: {row['kategori'].values[0]}
    altkategori: {row['altkategori'].values[0]}
    misal_1: {row['misal_1'].values[0]}
    """
    return result




def main():
    dictionary_file = 'dictionary.csv'
    phrases_file = 'phrases.csv'

    practice = input('What do you want to practice? ')

    if practice == 'kelime':

        df = pd.read_csv(dictionary_file, encoding='utf-8')

        number_of_words = input('How many words do you want to practice? ')

        # create n number of random numbers based on the number_of_words
        word_ids = np.random.randint(0, len(df), int(number_of_words))

        for word_id in word_ids:
            
            # if word_id is even, get the word from the kelime column in dataframe
            # if word_id is odd, get the word from the anlam column in dataframe

            if word_id % 2 == 0:
                # get the word from the kelime column in dataframe
                x = df.loc[word_id, 'kelime']
                response = input(f'{x} ~> ')

                # find all the matching words in the dataframe
                list_meanings = df.loc[df['kelime'] == x, 'anlam'].values

                # check if the response is in the list of meanings
                if response in list_meanings:
                    continue

                else:
                    # print in red color
                    print(f'\033[91m{x} ~> {df.loc[word_id, "anlam"]}\033[0m')
            else:
                # get the word from the kelime column in dataframe
                x = df.loc[word_id, 'anlam']
                response = input(f'{x} ~> ')

                # find all the matching words in the dataframe
                list_meanings = df.loc[df['anlam'] == x, 'kelime'].values

                # check if the response is in the list of meanings
                if response in list_meanings:
                    continue

                else:
                    # print in red color
                    print(f'\033[91m{x} ~> {df.loc[word_id, "kelime"]}\033[0m')

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


# create 10 random numbers
