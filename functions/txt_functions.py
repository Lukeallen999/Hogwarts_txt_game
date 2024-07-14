# Text for locations
import textwrap

# Variables
puppy_name = False


def print_clean_txt(txt: str) -> str:
    '''
    
    
    '''
    txt = txt.replace("  ","")
    txt = txt[1:]
    txt = textwrap.fill(txt, 100)

    print(txt)


def hagrid_hut_txt():   
    print_clean_txt('''path''')
    print('')
    print_clean_txt('''Intro''')
    print('')
    global puppy_name
    if puppy_name == False:
        print_clean_txt('''Finding puppy''')
        print('')
        choice_input = input('Do you investigate? (Y/N):').upper()
        if choice_input == 'Y':
            print('You find a puppy')
            puppy_name = input('Puppy name:' )
            print(f'Good {puppy_name} you say as you pet him')

hagrid_hut_txt()

print(f'your puppy is called: {puppy_name}')