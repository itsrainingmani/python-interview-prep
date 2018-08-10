import random

#List containing the lowercase alphabet + space character
alphabet = [chr(i) for i in range(97, 123)]
alphabet.append(' ')
shakespeare = "to be or not to be that is the question"

# Function that generates a 28 character string from the alphabet + space
def generate(char_set, str_len):
    gen_str = ''
    for i in range(0, str_len):
        rand_char = random.randrange(0, len(char_set)-1)
        gen_str += char_set[rand_char]
    return gen_str

def generate_hill_climb(char_set, current_gen):
    rand_ind = random.randrange(0, len(char_set))
    str_pos = shakespeare.find(char_set[rand_ind])
    if str_pos == -1:
        return current_gen
    while True:
        if current_gen[str_pos] != ' ':
            str_pos = shakespeare.find(char_set[rand_ind], str_pos+1, len(shakespeare))
            if str_pos == -1:
                return current_gen
        else:
            current_gen = current_gen[:str_pos] + char_set[rand_ind] + current_gen[str_pos+1:]
            return current_gen

# Function that scores the generated string
def score(orig_str, gen_str):
    count = 0
    for i, c in enumerate(orig_str):
        if gen_str[i] == c:
            count += 1
    return count

def generate_loop():
    init_gen_str = ' ' * len(shakespeare)
    num_tries = 0
    best_current_score = 0
    while True:
        if num_tries%10000 == 0 and num_tries > 0:
            print("%i tries have passed. The best score so far is - %i with %s" % (num_tries, best_current_score, init_gen_str))
        
        # init_gen_str = generate(alphabet, len(shakespeare))
        init_gen_str = generate_hill_climb(alphabet, init_gen_str)
        gen_str_score = score(shakespeare, init_gen_str)
        
        if gen_str_score > best_current_score:
            best_current_score = gen_str_score
        if gen_str_score == len(shakespeare):
            print("Huzzah the infinite monkeys have succeeded after %i tries" % num_tries)
            break
        num_tries += 1
        # print(num_tries)
        

if __name__ == "__main__":
    print(alphabet, shakespeare)
    generate_loop()