import spacy
#q1
text = "pg71072.txt"
with open(text, "r") as file:
    text_content = file.read()
print("Read successful!")

nlp = spacy.load("en_core_web_sm")
doc = nlp(text_content)

#q2
tokens = [token.text for token in doc]
print("Tokenization sucessful!")

lemmas = [token.lemma_ for token in doc]
print("Lemmatization Sucessful!")

pos_tags = [token.pos_ for token in doc]
print("POS tagging sucessful!")

#q3
filtered_tokens = [token.text for token in doc if not token.is_stop]
print("Removing Stop Words Successful!")

#q4
adjective_count = 0
for token in doc:
    if token.pos_ == 'ADJ':
        adjective_count += 1

print("Number of adjectives:", adjective_count)

#q5
from collections import defaultdict
pos_freq = defaultdict(int)  

for token in pos_freq:
  pos_freq[token] += 1

print(pos_freq)


#q6
text = "In 2020, CO2 accounted for about 79% of all U.S. greenhouse gas emissions from human activities. The combustion of fossil fuels such as gasoline and diesel to transport people and goods was the largest source of CO2 emissions in 2020, accounting for about 33% of total U.S. CO2 emissions and 26% of total U.S. greenhouse gas emissions. In 2020, the combustion of fossil fuels to generate electricity was the second largest source of CO2 emissions in the nation, accounting for about 31% of total U.S. CO2 emissions and 24% of total U.S. greenhouse gas emissions. The types of fossil fuel used to generate electricity emit different amounts of CO2. To produce"
doc2 = nlp(text)

percentages = []
for token in doc2:
    if token.like_num and token.i < len(doc2) - 1 and doc2[token.i + 1].text == '%':
        percentages.append(token.text + '%')

for percentage in percentages:
    print(percentage)

#q7
text3 = "I like to record records"
reloading_nlp = spacy.load("en_core_web_sm")
doc3 = nlp(text3)

for token in doc3:
    print(token.pos_, end=" ")
