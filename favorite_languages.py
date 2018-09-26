favorite_languages = {
		'jen' : ['python', 'ruby'],
		'sarah' : ['c'],
		'edward' : ['ruby', 'go'],
		'phil' : ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are: ")
	if len(languages) >= 2:
		for language in languages:
			print("\t" + language.title())
	else:
		print("\t" + languages[0].title())
	
	