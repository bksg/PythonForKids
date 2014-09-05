Python 3.4.1 (default, Jul 26 2014, 13:46:45) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 3 + 4
7
>>> fred= "why do gorillas have big nostrils?
SyntaxError: EOL while scanning string literal
>>> fred= "why do gorillas have big nostrils?"
>>> "big fingers!!"
'big fingers!!'
>>> print(fred)
why do gorillas have big nostrils?
>>> fred=what is pink and fluffy?pink fluffy!!"
SyntaxError: invalid syntax
>>> fred=what is pink and fluffy?pink fluffy!!"fred=what is pink and fluffy?pink fluffy!!"
SyntaxError: invalid syntax
>>> 
>>> 
>>> fred='what is pink and fluffy?' 'pink fluff!!'
>>> print(fred)
what is pink and fluffy?pink fluff!!
>>> fred="how do dinosaurs pay their bills?
SyntaxError: EOL while scanning string literal
>>> 
>>> >>> fred="how do dinosaurs pay their bills?" "with tyransaurus checks!!"
SyntaxError: invalid syntax
>>> fred="how do dinosaurs pay their bills?" "with tyransaurus checks!!"fred="how do dinosaurs pay their bills?" "with tyransaurus checks!!"print(fred)
SyntaxError: invalid syntax
>>> 
>>> print(fred)
what is pink and fluffy?pink fluff!!
>>> spaces=''*25
>>> print(spaces)

>>> 
>>> wizard list=['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff','eye of cyclops']
SyntaxError: invalid syntax
>>> 'wizard_list'=['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff','eye of cyclops']

SyntaxError: can't assign to literal
>>> 'wizard_list'=['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff','eye of cyclops']
SyntaxError: can't assign to literal
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> wizard_list=['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff','eye of cyclops']
>>> print(wizard_list[2])
eye of newt
>>> print(wizard_list)
['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff', 'eye of cyclops']
>>> wizard_list[2]='snail tongue'
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff', 'eye of cyclops']
>>> print(wizard_list[2:5])
['snail tongue', 'bat wing', 'slug butter']
>>> some_strings=['which','witch','is','which']
>>> 
>>> 
>>> some_strings
['which', 'witch', 'is', 'which']
>>> wizard_list=['spider legs','toe of frog','eye of newt','bat wing','slug butter','snake dandruff','eye of cyclops']
>>> wizard_list.append('bear burp')
>>> wizard_list.append('bear burp','mandrake','hemlock','swamp gas' )
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    wizard_list.append('bear burp','mandrake','hemlock','swamp gas' )
TypeError: append() takes exactly one argument (4 given)
>>> wizard_list('bear burp','mandrake','hemlock','swamp gas' )
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    wizard_list('bear burp','mandrake','hemlock','swamp gas' )
TypeError: 'list' object is not callable
>>> wizard_list.append('bear burp')
>>> print(wizard_list)
['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff', 'eye of cyclops', 'bear burp', 'bear burp']
>>> wizard_list.append('swamp gas')
>>> wizard_list.append('mandrake')
>>> wizard_list.append('hemlock')
>>> print(wizard_list)
['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff', 'eye of cyclops', 'bear burp', 'bear burp', 'swamp gas', 'mandrake', 'hemlock']
>>> 
