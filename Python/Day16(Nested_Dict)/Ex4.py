

Institute = {
	'Python' : {'p1' : 'Data Analyst','p2' : 'AI','P3' : 'Machine learning','p4' : 'Web development'},
	'Java'   : {'j1' : 'Android development','j2' : 'OS development','j3' : 'Testing','j4' : 'selinum'},

}
# print(Institute)
# {'Python': {'p1': 'Data Analyst', 'p2': 'AI', 'P3': 'Machine learning', 'p4': 'Web development'},
 # 'Java': {'j1': 'Android development', 'j2': 'OS development', 'j3': 'Testing', 'j4': 'selinum'}}


# {'p5' : 'SEO'}

nest_dict = Institute['Python']
# print(nest_dict) # {'p1': 'Data Analyst', 'p2': 'AI', 'P3': 'Machine learning', 'p4': 'Web development'}
print()
nest_dict.update({'p5' : 'SEO'})
# print(nest_dict)
# {'p1': 'Data Analyst', 'p2': 'AI', 'P3': 'Machine learning', 'p4': 'Web development', 'p5': 'SEO'}


# {'Python': {'p1': 'Data Analyst', 'p2': 'AI', 'P3': 'Machine learning', 'p4': 'Web development','p5' : 'SEO'}, 
# 'Java': {'j1': 'Android development', 'j2': 'OS development', 'j3': 'Testing', 'j4': 'selinum'}}













