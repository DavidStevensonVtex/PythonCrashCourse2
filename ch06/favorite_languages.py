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

# {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
# Sarah's favorite language is C

# Jen's favorite language is Python
# Sarah's favorite language is C
# Edward's favorite language is Ruby
# Phil's favorite language is Python