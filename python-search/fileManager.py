def readDict (q_word_file):
    with open(q_word_file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content