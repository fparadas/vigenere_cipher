from itertools import cycle, starmap
import unidecode
import sys

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

if __name__ == "__main__":
  key = sys.argv[sys.argv.index("-k") + 1]
  if "-d" in sys.argv:
    file = sys.argv[sys.argv.index("-d") + 1]
    encrypt = False
  else:
    file = sys.argv[sys.argv.index("-e") + 1]
    encrypt = True

  with open(file, 'r') as fp:
      msg = fp.read()
      if encrypt:
        cyphertext = cypher(key, unidecode.unidecode(msg))
        print(cyphertext)
      else:
        cyphertext = decypher(key, unidecode.unidecode(msg))
      print(cyphertext)

