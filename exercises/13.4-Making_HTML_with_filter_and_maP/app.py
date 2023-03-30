all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(color):
	return color["sexy"]

def generate_li(color_sexy):
	return f'<li>{color_sexy["label"]}</li>'


new_list = list(filter(filter_colors, all_colors))

new_list2 = list(map(generate_li, new_list))

print(new_list2)


# OTRA SOLUCION
# def filter_colors(color):
# 	return color["sexy"]

# def generate_li(color_sexy):
# 	return "<li>" + color_sexy["label"] + "</li>"


# new_list = list(filter(filter_colors, all_colors))

# new_list2 = list(map(generate_li, new_list))

# print(new_list2)