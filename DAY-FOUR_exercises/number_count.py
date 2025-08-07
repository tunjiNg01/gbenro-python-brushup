def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content=file.read()
            words=content.split()
            word_count=len(words)
            print("total number of words is : {}".format(word_count))
    except FileNotFoundError:
        print("The file can not be found.")
    except Exception as e:
        print("an error occured {}".format(e))


count_words_in_file("Realtor_data_processing.txt")