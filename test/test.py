import random
list_choices = ['banner_skull','banner_key','banner_skull2','banner_snake','banner_world']
list_quotes = ['quote_1','quote_2','quote_3','quote_4','quote_5']
a = ''''''
b = ''
with open(random.choice(list_choices) + '.txt','r') as f:
    a = f.read()
    f.close()
with open(random.choice(list_quotes) + '.txt','r') as f:
    b = f.read()
    f.close()

print a.format(b)
