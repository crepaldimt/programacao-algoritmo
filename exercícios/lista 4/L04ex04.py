import string

texto = """The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."""
li = texto.split()

letras = tuple('python')

lista = []

for p in li:
    p_limpo = p.strip(string.punctuation).lower()
    if p_limpo.startswith(letras) or p_limpo.endswith(letras):
        lista.append(p_limpo)

print(lista)
