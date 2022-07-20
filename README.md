# Cifra de Vigenere

Primeiro trabalho da matéria de segurança computacional.

- Aluno: Felipe Gomes Paradas
- Matrícula: 170009840

## Como rodar

Para rodar o programa é necessário ter o python3 instalado e a biblioteca unidecode, que pode ser instalada através do comando:

```sh
pip3 install unidecode
```

O programa tem os seguintes argumentos:
- "-k": Chave
- "-e": arquivo que será cifrado
- "-d": arquivo que será decifrado

Dessa forma, para cifrar um texto rode:

```sh
python3 main.py -k <chave> -e <arquivo>
```

E para decifrar:

```sh
python3 main.py -k <chave> -d <arquivo>
```
Não consegui implementar a segunda parte corretamente, mas fica aí o arquivo que eu usei para tentar!!

## Implementação

Para implementar a cifra, foram utilizadas as seguintes funções:

```python
def cycle_zip_with(func, key, msg):
  """
    func: (a: char, b:char) -> char
    key: [char] or string
    msg: [char] or string

    Creates a cyclic list with the first list (key)
    then zips with the second list (msg) unsing func
  """
  cycled = cycle(key)
  return list(starmap(func, zip(cycled, msg)))
```

```python
def cypher(key, msg):
  """
    Cypher the msg with the provided key and returns the cyphertext
  """
  def cip(k, m):
    """
      Sum the int value of m_n with the int value of k_n module the number
      of letters in the alphabet

      int value of m_n = ord(m_n) - ord('A'),
      int value of k_n = ord(k_n) - ord('A')
    """
    r = ""
    if m.isalpha():
      x = (ord(m.upper()) + ord(k) - 2*ord('A')) % (ord('Z') - ord('A'))
      r = chr(x + ord('A'))
    else:
      r = m
    return r

  return "".join(cycle_zip_with(cip, key, msg))
```

```python
def decypher(key, msg):
  """
    Decypher the cyphertext with the provided key and returns the msg
  """
  def dec(k, c):
    """
      Subtracts the int value of k_n from the int value of c_n module the number
      of letters in the alphabet

      int value of c_n = ord(c_n) - ord('A'),
      int value of k_n = ord(k_n) - ord('A')
    """
    r = ""
    if c.isalpha():
      x = (ord(c.upper()) - ord(k)) % (ord('Z') - ord('A'))
      r = chr(x + ord('A'))
    else:
      r = c
    return r

  return "".join(cycle_zip_with(dec, key, msg))
```