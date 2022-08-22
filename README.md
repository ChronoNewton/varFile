# varFile

Var File is a light-wight cross-platform library, that comes in *different coding languages(not yet), it's designed with the sole purpose to handle the creation and modification of a special file type, which it introduces as the "var file"(.var) .

# ".var" File Example

    #This is a comment using '#'
    --This is a comment using '--'
    //This is a comment using '//'

    NAME  alex

    IP = 127.0.0.1
    port: 1024



## ".var" File Purpose
A ".var" file, is a file type, which use is to store all sorts of variable data/information, in a way that's both easily user accessible & modifible, and computer ready to interpret & use fastly for variable data/information.(note: i just wrote that partially for the rhythm of the words)

**_Note_**: A var is to be always treated with its own set of rules in-order to work properly.


## Terminology
- 'varFile' is a system file of variables

- A 'variable' or 'var' is a whole line for itself alone in the system file.
- A 'key' is a part of a variable, that is a unique name to identify the variable itself.
- A 'value' is a part of a variable, that is any data/information that follows the variable's name and its initializer(A mark to identify the value being declared)


## ".var" File Rules

**_Note_**: Reading a key always returns a 'String', no matter if the value was absolute 'int', so consider using the built-in conversion to make it from text to (int/boolean...) OR any-method you see fits.

- In-order to make a var: You first just write the key name, though to note, it's highly recommended to write it in the Standard way( English ONLY & aA-zZ & 0-9 & Underscore ONLY ) as other programming languages require.
- After the var Key(name), comes the initializer which is so simple either  "=" or ":" or "(a tab)"(NOTE: a tab is a *BYTE* of tab, NOT some amount of *SPACES*).
- Finally comes the value, the value can be anything and written easily, though in one case if the value is in bytes format, it *should* use a special method to writting which is in square brackets, and for it can be represented either in Hex or Binary, e.g. like this "h[00][1f][AB]"(upper/lower all work!)   or   "b[01010110][11101011][01010]"(NOTE: in binary it can be represented as low as a bit!). BUT in-case you chose to write the bytes directly without the *special method*, then its fine, but note: the user may mess it up, and it could potentially be harder to modify by the user *in some cases*.
- In-order to declare a comment, write a '#' or '//' or '--' followed by the comment itself(text), like this "#This is a comment".


## How To Make ".var" File

There are two ways to create:
- 1- Manualy (User):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any text editor will do the job just fine.

- 2- Programmatically (Program/Code):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Using the varFile library(this library).


## Support Me
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ChronoNewton)
