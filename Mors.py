print('1-Enkodiranje')
print('2-Dekodiranje')
op = int(input('Odaberi željenu funkciju:'))


if op == 1:
         value=input('Upisi tekst koj zelis enkodirat u morsov kod:')
         string = value.upper()
         morse_code = {'A': '.-','B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-','L' : '-.-',
                      'M' : '--','N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--','X' : '-..-',
                      'Y' : '-.--','Z' : '--..','0' : '-----', '1' : '.----', '2' :'..---', '3' : '...--', '4' : '....-', '5' : '.....', '6':'-.....','7':'--....','8':'---..',
                      '9' : '----.', '.' : '.-.-.-', ',' : '--..--','?' : '..--..', ' ' : '/'}
         print('Morsov kod:',end='')

         for element in range(0, len(string)):
          print(morse_code.get(string[element]), end='')



      

elif op == 2:
     value=input('Upisi morsov koj zelis enkodirat u morsov kod:')
     alpha_code = {'.-' : 'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
                   '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
                   '..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','-----':'0','.----':'1','..---':'2','...--':'3',
                   '....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','.-.-.-':'.','--..--':',','..--..':'?','/':' '}
     code=value.split()
     print('Tekst:',end='')
     for element in range(0, len(code)):
        print(alpha_code.get(code[element]), end='')

else:
    print('Nije upisan tekst ni morsov kod')
m=print('\n')
k=input("Klikni bilo koj gumb da zatvoris prozor: ")


    
    
              
              
