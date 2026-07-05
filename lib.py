import random 

def generate_move():
 number_component = str(random.randint(1, 8))
 letter_component = random.randint(1, 8)
 piece = random.randint(1, 5)
 if piece == 5:
   piece_name = 'pawn'
   piece_num = str(random.randint(1, 4))
 if piece == 1:
  piece = 'king'
 if piece == 2:
  piece = 'elephant' 
 if piece == 3:
  piece = 'horse'
 if piece == 4:
  piece = 'boat'
 if letter_component == 1:
  letter_component = 'a'
 if letter_component == 2:
  letter_component = 'b'
 if letter_component == 3:
  letter_component = 'c'
 if letter_component == 4:
  letter_component = 'd'
 if letter_component == 5:
  letter_component = 'e'
 if letter_component == 6:
  letter_component = 'f'
 if letter_component == 7:
  letter_component = 'g'
 if letter_component == 8:
  letter_component = 'h'
 if piece == 5:
  print(piece_name + piece_num + ' ' + letter_component + ' ' + number_component)
 else:
   print(piece + ' ' + letter_component + ' ' + number_component)
