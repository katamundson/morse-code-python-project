"""
Kat Amundson
CIS 189
Final
Morse Code/English Translator
"""
from tkinter import *   #the * means everything... dont have to do tkinter.
import datetime as dt
from datetime import timedelta
from tkinter import messagebox
 
m = Tk() #creates the window
 
var1 = StringVar(m) 
var2 = StringVar(m) 
   
var1.set("lang-code") 
var2.set("lang-code") 
   
   
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',           #morse code dictionary
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '!':'-.-.--','/':'-..-.',
                    '-':'-....-', '(':'-.--.', ')':'-.--.-',
                    ';':'-.-.-',':':'---...', '-':'-....-',
                    '_':'..--.-','@':'.--.-.'} 
 
def clearAll(): #clears the text areas (entire)
    
    lang1_field.delete(1.0, END)
    lang2_field.delete(1.0, END)
 
def change():  #translates the two languages
    
    message = lang1_field.get("1.0", "end")[:-1]    #gets ALL the input
 
    if var1.get() == var2.get():  #gets var1 and var2 info and checks their values 
        
        messagebox.showerror("Can't Be same Language")  #shows an error
        return
 
    elif var1.get() == "English" and var2.get() == "Morse" :
 
        result = eng_to_morse(message)
 
    elif var1.get() == "Morse" and var2.get() == "English" :
 
        result = morse_to_eng(message)
 
    else :
         
        messagebox.showerror("please choose valid language code..") #shows an error
        returndec
    
    lang2_field.insert('end -1 chars', result)    #puts the info in text fields from result var


def eng_to_morse(message):   
    encode = ''         #encode stores the morse form of the english
    for letter in message: 
        if letter != ' ':
            
            encode += MORSE_CODE_DICT[letter] + ' '     #finds dict and the right code, must include space to work
        else: 
            
            encode += ' '   #1 space = diff letters, 2 spaces = different words
   
    return encode 
   
def morse_to_eng(message):  
    
    message += ' ' #space to get the last code
   
    decode = '' 
    citext = ''     #citext stores the morse code for the character
    for letter in message: 
        if (letter != ' '):     #checks for the space
            i = 0               #counter keeps track of the spaces
            citext += letter
            
        else:       #in case of space
            i += 1  #new letter
            if i == 2 : #new word
    
                decode += ' '     #adds space to separate words
            else: 
                    #reverses the encrption 
                decode += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = '' 
   
    return decode


#DRIVER

if __name__ == "__main__" : 
     
    m.geometry("550x810")  
    
    m.title("Morse/English Translator")
    
    headlabel = Label(m, text = 'Morse Code Translator')
    sublabel = Label(m, text = 'FOR ENGLISH:\nPlease use all CAP letters'
                     +'\nFOR MORSE:\n Please use 1 space between letters \nand 2 spaces between words')
   
    label1 = Label(m, text = "  Type One Language") 
    label2 = Label(m, text = "   Choose Input Language")  
    label3 = Label(m, text = "  Choose Output Language") 
    label4 = Label(m, text = "  Translation ")
    label5 = Label(m, text = "       Start Time ")
    label6 = Label(m, text = "Key")

#grid is for placing them where they need to be 
    headlabel.grid(row = 0, column = 2)
    sublabel.grid(row =1, column = 2)
    label1.grid(row = 2, column = 1)  
    label2.grid(row = 3, column = 1) 
    label3.grid(row = 4, column = 1) 
    label4.grid(row = 6, column = 1)
    label5.grid(row = 7, column = 1)
    label6.grid(row = 9, column = 1)

#creates the input text box
    lang1_field = Text(m, height = 5, width = 30) 
    lang1_field.grid(row = 2, column = 2)
    
    lang2_field = Text(m, height = 5, width = 30)
    lang2_field.grid(row = 6, column = 2) 

    languageCode_list = ["English", "Morse"] #list of what will be in the drop down menu
   

    FromLanguage_option = OptionMenu(m, var1, *languageCode_list) #the * makes it so eng and 
    ToLanguage_option = OptionMenu(m, var2, *languageCode_list)    #morse are separate
       
    FromLanguage_option.grid(row = 3, column = 2) 
    ToLanguage_option.grid(row = 4, column = 2) 
       
#creates the convert button and where it is. Assigns the convert() 
    button1 = Button(m, text = "Translate", command = change)  
    button1.grid(row = 5, column = 2) 
   
#creates the clear button and where it is. Assigns the clearAll()
    button2 = Button(m, text = "Clear",  command = clearAll)
    button2.grid(row = 8, column = 2)

#creates a datetime for when you open the gui
    datetime_field = Label(m, text=dt.datetime.now())
    datetime_field.grid(row = 7, column = 2)

#I did two different ones just to separate and make it seem more clean in their respective columns
    key_field1 = Label(m, text= "A: .-    \nB: -...  \nC: -.-.  \nD: -..   \nE: .     \nF: ..-.  \nG: --.   \nH: ....  \nI: ..    "
                       +"\nJ: .---  \nK: -.-   \nL: .-..  \nM: --    \nN: -.    \nO: ---   \nP: .--.  \nQ: --.-  \nR: .-.   "
                       +"\nS: ...   \nT: -     \nU: ..-   \nV: ...-  \nW: .--   \nX: -..-  \nY:-.--   \nZ: --..  ")
 
    key_field1.grid(row = 9, column = 2)

    key_field2 = Label(m, text= "\n1: .---- \n2: ..--- \n3: ...-- \n4: ....- \n5: ..... \n6: -.... \n7: --... \n8: ---.. \n9: ----. "
                       +"\n0: ----  \n/: -..-. \n-: -....-\n(: -.--. \n): -.--.-\n_: ..--.-\n@: .--.-.\n,: --..-- \n.: .-.-.- "
                       +"\n?: ..--.. \n!: -.-.--\n;: -.-.- \n:: ---... \n-: -....-")

    key_field2.grid(row = 9, column = 3)

#in some letters, like 'E', there is a large amount of spaces, this is so they can appear more in a straight line. So there are 7 spaces between the : and the \n


m.mainloop()
