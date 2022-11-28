import wikipedia

def get_wikipedia_summary(search_term):
    wikipedia.set_lang("en")
    return wikipedia.summary(search_term)

def get_wikipedia_page(search_term):
    wikipedia.set_lang("en")
    return wikipedia.page(search_term)

def wikipedia_search(search_term):
    wikipedia.set_lang("en")
    return wikipedia.search(search_term)

def wikipedia_suggest(search_term):
    wikipedia.set_lang("en")
    return wikipedia.suggest(search_term)

def wikipedia_random():
    wikipedia.set_lang("en")
    return wikipedia.random()

# print(get_wikipedia_summary("Moto GP"))
# print(get_wikipedia_page("Moto GP"))
# print(wikipedia_search("Moto GP"))
# print(wikipedia_suggest("Moto GP"))
# print(wikipedia_random())