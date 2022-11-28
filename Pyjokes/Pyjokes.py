import pyjokes

def get_joke(language, category):
    joke = pyjokes.get_joke(language, category)
    return joke

print(get_joke("en", "neutral"))
print(get_joke("en", "all"))
print(get_joke("en", "chuck"))