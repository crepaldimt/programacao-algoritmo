<div align="center">

```
██████╗ ██████╗  ██████╗  ██████╗     ██████╗ ███████╗██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝     ██╔══██╗██╔════╝██║   ██║
██████╔╝██████╔╝██║   ██║██║  ███╗    ██║  ██║█████╗  ██║   ██║
██╔═══╝ ██╔══██╗██║   ██║██║   ██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝
██║     ██║  ██║╚██████╔╝╚██████╔╝    ██████╔╝███████╗ ╚████╔╝ 
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝  ╚═══╝  
```

# 〈 Algoritmos & Estruturas de Dados 〉

*Transformando lógica em código, um algoritmo de cada vez.*

---

[![Linguagens](https://img.shields.io/badge/Linguagens-Python%20%7C%20C%2B%2B%20%7C%20Java-blue?style=flat-square&logo=code&logoColor=white)](.)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-brightgreen?style=flat-square)](.)
[![Licença](https://img.shields.io/badge/Licença-MIT-orange?style=flat-square)](./LICENSE)
[![PRs](https://img.shields.io/badge/PRs-Bem--vindos-blueviolet?style=flat-square)](.)

</div>

---

## 📌 Sobre o Repositório

> Este repositório é um **acervo pessoal de estudos** em programação e algoritmos. Aqui você encontrará implementações comentadas, análises de complexidade e comparações entre abordagens, organizadas por tema e nível de dificuldade.

O objetivo é documentar a jornada de aprendizado de forma clara e reutilizável — tanto para revisão pessoal quanto para quem estiver buscando referências bem explicadas.

---

## 🗂️ Estrutura do Repositório

```
📦 prog-dev/
 ┣ 📂 algoritmos/
 ┃ ┣ 📂 ordenacao/          # Bubble, Merge, Quick, Heap Sort...
 ┃ ┣ 📂 busca/              # Busca binária, BFS, DFS...
 ┃ ┣ 📂 grafos/             # Dijkstra, Kruskal, Bellman-Ford...
 ┃ ┣ 📂 programacao-dinamica/  # Mochila, LCS, Fibonacci...
 ┃ ┗ 📂 divisao-conquista/  # Merge Sort, Karatsuba...
 ┣ 📂 estruturas-de-dados/
 ┃ ┣ 📂 listas/             # Lista ligada, duplamente ligada
 ┃ ┣ 📂 arvores/            # BST, AVL, Heap, Trie
 ┃ ┣ 📂 pilhas-filas/       # Stack, Queue, Deque
 ┃ ┗ 📂 tabelas-hash/       # Hash Map, tratamento de colisões
 ┣ 📂 desafios/
 ┃ ┣ 📂 leetcode/
 ┃ ┗ 📂 beecrowd/
 ┗ 📜 README.md
```

---

## 🧠 Tópicos Cobertos

<table>
  <tr>
    <th>🔢 Algoritmos de Ordenação</th>
    <th>🔍 Algoritmos de Busca</th>
    <th>🌐 Grafos</th>
  </tr>
  <tr>
    <td>
      ✅ Bubble Sort<br>
      ✅ Selection Sort<br>
      ✅ Insertion Sort<br>
      ✅ Merge Sort<br>
      ✅ Quick Sort<br>
      🔄 Heap Sort<br>
      ⬜ Radix Sort
    </td>
    <td>
      ✅ Busca Linear<br>
      ✅ Busca Binária<br>
      ✅ BFS (Largura)<br>
      ✅ DFS (Profundidade)<br>
      🔄 A* (A-star)<br>
      ⬜ Jump Search
    </td>
    <td>
      ✅ Representação (Matriz/Lista)<br>
      ✅ Dijkstra<br>
      ✅ Kruskal<br>
      🔄 Prim<br>
      🔄 Bellman-Ford<br>
      ⬜ Floyd-Warshall
    </td>
  </tr>
  <tr>
    <th>🌲 Estruturas em Árvore</th>
    <th>💡 Prog. Dinâmica</th>
    <th>📚 Estruturas Base</th>
  </tr>
  <tr>
    <td>
      ✅ Árvore Binária (BST)<br>
      ✅ Árvore AVL<br>
      🔄 Heap Binário<br>
      🔄 Trie<br>
      ⬜ Árvore Vermelho-Preto
    </td>
    <td>
      ✅ Fibonacci (memoização)<br>
      ✅ Problema da Mochila<br>
      ✅ LCS<br>
      🔄 Coin Change<br>
      ⬜ Longest Palindrome
    </td>
    <td>
      ✅ Array / Matriz<br>
      ✅ Lista Ligada<br>
      ✅ Pilha & Fila<br>
      ✅ Tabela Hash<br>
      🔄 Deque<br>
      ⬜ Union-Find
    </td>
  </tr>
</table>

> `✅ Implementado` &nbsp;|&nbsp; `🔄 Em progresso` &nbsp;|&nbsp; `⬜ Planejado`

---

## 📊 Complexidades de Referência

| Algoritmo       | Melhor Caso | Caso Médio | Pior Caso | Espaço   |
|-----------------|:-----------:|:----------:|:---------:|:--------:|
| Bubble Sort     | O(n)        | O(n²)      | O(n²)     | O(1)     |
| Merge Sort      | O(n log n)  | O(n log n) | O(n log n)| O(n)     |
| Quick Sort      | O(n log n)  | O(n log n) | O(n²)     | O(log n) |
| Busca Binária   | O(1)        | O(log n)   | O(log n)  | O(1)     |
| Dijkstra        | —           | O(E log V) | O(E log V)| O(V)     |
| Hash Table      | O(1)        | O(1)       | O(n)      | O(n)     |

---

## 💻 Como Usar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/prog-dev.git

# Navegue até a pasta desejada
cd prog-dev/algoritmos/ordenacao

# Execute o exemplo (Python)
python3 merge_sort.py

# Execute o exemplo (C++)
g++ -o quicksort quick_sort.cpp && ./quicksort
```

---

## 🔬 Exemplo de Implementação

Todo algoritmo neste repositório segue o padrão:

```python
"""
Algoritmo: Merge Sort
Complexidade: O(n log n) — todos os casos
Espaço:      O(n)
Estável:     Sim
"""

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1

    return result + left[i:] + right[j:]


# Teste
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]
```

---

## 🏆 Desafios Resolvidos

| Plataforma  | Resolvidos | Nível Médio | Link                              |
|-------------|:----------:|:-----------:|-----------------------------------|
| LeetCode    | ![](https://img.shields.io/badge/-XX-yellow?style=flat-square) | Médio | [Ver perfil](https://leetcode.com) |
| Beecrowd    | ![](https://img.shields.io/badge/-XX-blue?style=flat-square)   | Médio | [Ver perfil](https://beecrowd.io) |
| HackerRank  | ![](https://img.shields.io/badge/-XX-green?style=flat-square)  | Médio | [Ver perfil](https://hackerrank.com)|

---

## 🛠️ Tecnologias

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

</div>

---

## 📖 Referências e Recursos

- 📘 **Introduction to Algorithms** — CLRS (Cormen et al.)
- 📗 **Algoritmos: Teoria e Prática** — Cormen (Ed. Brasileira)
- 🌐 [Visualgo](https://visualgo.net) — Visualização de algoritmos
- 🌐 [CP-Algorithms](https://cp-algorithms.com) — Algoritmos competitivos
- 🎓 [CS50x](https://cs50.harvard.edu) — Harvard OpenCourseWare

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se encontrar um erro, quiser adicionar uma implementação ou melhorar a documentação:

1. Faça um **fork** do repositório
2. Crie uma branch: `git checkout -b minha-contribuicao`
3. Commit suas mudanças: `git commit -m 'feat: adiciona algoritmo X'`
4. Push: `git push origin minha-contribuicao`
5. Abra um **Pull Request**

---

## 📬 Contato

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-usuario)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/seu-usuario)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:seu@email.com)

</div>

---

<div align="center">

*"Um algoritmo deve ser visto para ser acreditado."* — Donald Knuth

⭐ **Se este repositório foi útil, deixe uma estrela!** ⭐

</div>
