# import os
l=[
    # 'Intro & Vocab Buidling',
    # 'Vocab Building Part II',
    'Text Completion Part I',
    'Text Completion Part II',
    'Short Passages',
    'Medium Passages',
    'Long Passages',
    'Critical Reasoning Part I',
    'Critical Reasoning Part II',
    'Critical Reasoning Part III',
    'Sentence Equivalence',
    'Analyse the Issue (AWA)',
    'Analyse an Argument (AWA)',
    'Doubt Solving & Refresher Part I',
    'Doubt Solving & Refresher Part II',
]

for i in range(len(l)):
    if(len(str(i))<2):
        l[i]=f'0{i}_{l[i]}'
    else:
        l[i]=f'{i}_{l[i]}'

# # x=input()
# # while(int(x)!=-1):
# #     l.append(x)
# #     x=input("Please Name It: ")

# for i in l:
#     if os.path.exists(f'{i}.txt'):
#         pass
#     else:
#         with open(f'{i}.txt', 'w') as f:
#             pass

with open(f'{l[0]}.txt', 'w') as f:
    pass