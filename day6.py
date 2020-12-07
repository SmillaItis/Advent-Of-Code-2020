
with open(r'done\advent\questions.txt', 'r') as f:
    text = f.read()
text = text.split('\n\n')
print(text)
text = [i.replace('\n', '') for i in text]


new_text = ["".join(set(t)) for t in text]

string = ''.join(new_text)
print(len(string))
