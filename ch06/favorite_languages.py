favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n")
for name in favorite_languages.keys():
    print(name.title())

# {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
# Sarah's favorite language is C

# Jen's favorite language is Python
# Sarah's favorite language is C
# Edward's favorite language is Ruby
# Phil's favorite language is Python

# Jen
# Sarah
# Edward
# Phil
print("\n")
friends = [ 'phil', 'sarah' ]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

# Hi Jen.
# Hi Sarah.
#         Sarah, I see you love C
# Hi Edward.
# Hi Phil.
#         Phil, I see you love Python