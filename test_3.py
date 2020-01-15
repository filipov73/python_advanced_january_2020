
from pandas import DataFrame

C = {'Programming language': ['Python', 'Java', 'C++'],

     'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],

     'Appeared': ['1991', '1995', '1985'],

     'Extension': ['.py', '.java', '.cpp'],

     }

df = DataFrame(C, columns=['Programming language', 'Designed by', 'Appeared', 'Extension'])

export_csv = df.to_csv(r'program_lang.csv', index=None, header=True)