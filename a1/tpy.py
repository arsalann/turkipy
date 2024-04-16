import pandas as pd
import numpy as np




def user_inputs():
    

def main():
    dictionary_file = 'dictionary.csv'
    phrases_file = 'phrases.csv'

    correct = 0
    wrong = 0
    practice = input('What do you want to practice? ')

    if practice == 'kelime':

        df = pd.read_csv(dictionary_file, encoding='utf-8')
        print(f'Number of words in the dictionary: {len(df)}')

        number_of_words = input('How many words do you want to practice? ')

        kategori = input('Do you want to practice all words or a specific category? (i.e. all or name of category) ')

        if kategori == 'all':
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
                        correct += 1
                        continue

                    else:
                        # print in red color
                        wrong += 1
                        print(f'\033[91m{x} ~> {df.loc[word_id, "anlam"]}\033[0m')
                else:
                    # get the word from the kelime column in dataframe
                    x = df.loc[word_id, 'anlam']
                    response = input(f'{x} ~> ')

                    # find all the matching words in the dataframe
                    list_meanings = df.loc[df['anlam'] == x, 'kelime'].values

                    # check if the response is in the list of meanings
                    if response in list_meanings:
                        correct += 1
                        continue

                    else:
                        # print in red color
                        wrong += 1
                        print(f'\033[91m{x} ~> {df.loc[word_id, "kelime"]}\033[0m')

        else:
            df = df[df['kategori'] == kategori]
            df = df.reset_index(drop=True)

            print(f'Number of words in the category: {len(df)}')

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
                        correct += 1
                        continue

                    else:
                        # print in red color
                        wrong += 1
                        print(f'\033[91m{x} ~> {df.loc[word_id, "anlam"]}\033[0m')
                else:
                    # get the word from the kelime column in dataframe
                    x = df.loc[word_id, 'anlam']
                    response = input(f'{x} ~> ')

                    # find all the matching words in the dataframe
                    list_meanings = df.loc[df['anlam'] == x, 'kelime'].values

                    # check if the response is in the list of meanings
                    if response in list_meanings:
                        correct += 1
                        continue

                    else:
                        # print in red color
                        wrong += 1
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

    print(f'Correct: {correct}')
    print(f'Wrong: {wrong}')
    print(f'Total: {correct + wrong}')
    print(f'Accuracy: {correct / (correct + wrong) * 100}%')

if __name__ == '__main__':
    main()


# create 10 random numbers
