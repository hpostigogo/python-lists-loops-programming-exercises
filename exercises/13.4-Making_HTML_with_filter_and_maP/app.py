all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def generate_li(list):
	color=list['label']
	return  (f'<li>{color}</li>')

def filter_colors(list):
	return list['sexy']

new_list=list(filter(filter_colors,all_colors))
list_html=list(map(generate_li,new_list))
print(list_html)

