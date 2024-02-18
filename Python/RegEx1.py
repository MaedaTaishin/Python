import re
# q1
test =["abccc","aabbcc","aaabc","abccccccc","abccccccc","aabbcccc","aaaaabbbc","bbccccc","aaaccccc"]

pattern = re.compile(r"a{1}b{1}cc+")

new_list = [i for i in test if pattern.search(i)]
print(new_list)
print('\n')
# q2
sequence = "On Jun 12 something happened. Something also happened on June 12 and Jun 12th, but not on July 17th or June 11th. June 12th and Jun twelfth are therefore important dates. They are the same day as June twelfth and Jun Twelfth as well as June Twelfth."

p = re.compile(r"(June?\s(12|[tT]welf)(th)?)")

m = p.findall(sequence)
print(m)
print('\n')
#q3
sequence = "On Jun 12 something happened. Added June twelve Jun twelve June Twelve, and Jun Twelve.. Something also happened on June 12 and Jun 12th, but not on July 17th or June 11th. June 12th and Jun twelfth are therefore important dates. They are the same day as June twelfth and Jun Twelfth as well as June Twelfth."

p = re.compile(r"(June?\s(12|[tT]welf|[tT]welve)(th)?)")

m = p.findall(sequence)
print(m)
print('\n')


