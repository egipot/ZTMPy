#pdb
import pdb

def add(num1, num2):
    #print(num1, num2)
    #pdb.set_trace()         # this runs a trace in the Code Terminal (where you can check the value of a variable - see below "Terminal #1")
    t = 4*5                 # this is added for Terminal #2
    return num1 + num2

#erroneous code: 
# add(4, 'sdfs')

#corrected one:
print(add (4, 5))


# Terminal #1
# PS C:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM> python -u "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\184_debugging.py"
#> c:\users\gaycalaranan.000\documents\programming\udemy - python - ztm\184_debugging.py(7)add()
#-> return num1 + num2
#(Pdb) num1
#4
#(Pdb) num2
#'sdfs'
#(Pdb) help

#Documented commands (type help <topic>):
#========================================
#EOF    c          d        h         list      q        rv       undisplay
#a      cl         debug    help      ll        quit     s        unt      
#alias  clear      disable  ignore    longlist  r        source   until    
#args   commands   display  interact  n         restart  step     up       
#b      condition  down     j         next      return   tbreak   w        
#break  cont       enable   jump      p         retval   u        whatis   
#bt     continue   exit     l         pp        run      unalias  where    

#Miscellaneous help topics:
#==========================
#exec  pdb

#(Pdb) list
#  2     import pdb
#  3
#  4     def add(num1, num2):
#  5         #print(num1, num2)
#  6         pdb.set_trace()
#  7  ->     return num1 + num2
#  8
#  9     add(4, 'sdfs')
#[EOF]
#(Pdb) help list
#l(ist) [first [,last] | .]

#        List source code for the current file.  Without arguments,
#        list 11 lines around the current line or continue the previous
#        listing.  With . as argument, list 11 lines around the current
#        line.  With one argument, list 11 lines starting at that line.
#        With two arguments, list the given range; if the second
#        argument is less than the first, it is a count.

#        The current line in the current frame is indicated by "->".
#        If an exception is being debugged, the line where the
#        exception was originally raised or propagated is indicated by
#        ">>", if it differs from the current line.
#(Pdb) clear
#Clear all breaks? y
#(Pdb) step 
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#> c:\users\gaycalaranan.000\documents\programming\udemy - python - ztm\184_debugging.py(7)add()
#-> return num1 + num2
#(Pdb)


# Terminal #2
#PS C:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM> python -u "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\184_debugging.py"
#> c:\users\gaycalaranan.000\documents\programming\udemy - python - ztm\184_debugging.py(7)add()
#-> t = 4*5
#(Pdb) t
#*** NameError: name 't' is not defined
#(Pdb) step
#> c:\users\gaycalaranan.000\documents\programming\udemy - python - ztm\184_debugging.py(8)add()
#-> return num1 + num2
#(Pdb) t
#20
#(Pdb) a
#num1 = 4
#num2 = 'sdfs'
#(Pdb) w
#  c:\users\gaycalaranan.000\documents\programming\udemy - python - ztm\184_debugging.py(10)<module>()
#-> add(4, 'sdfs')
#> c:\users\gaycalaranan.000\documents\programming\udemy - python - ztm\184_debugging.py(8)add()
#-> return num1 + num2
#(Pdb) exit
#Traceback (most recent call last):
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\184_debugging.py", line 10, in <module>
#    add(4, 'sdfs')
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\184_debugging.py", line 8, in add
#    return num1 + num2
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM\184_debugging.py", line 8, in add
#    return num1 + num2
#  File "C:\Users\GayCalaranan.000\anaconda3\lib\bdb.py", line 88, in trace_dispatch
#    return self.dispatch_line(frame)
#  File "C:\Users\GayCalaranan.000\anaconda3\lib\bdb.py", line 113, in dispatch_line
#    if self.quitting: raise BdbQuit
#bdb.BdbQuit

