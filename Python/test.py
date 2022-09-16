from varFile import varFile

test_varFile = varFile('../test.var')
test_varFile.readVarFile()


#variable value is retrieved by its key(name), which is e.g. 'NAME'
print('My name is ' + test_varFile.getValueByKey('NAME'))

#variable value is retrieved by the line number, which is e.g. 7
print('My Ip is ' + test_varFile.getValueByLineNumber(7))

#entire variable line is retrieved by the line number, which is e.g. 8
print('\nfull variable line:\n' + test_varFile.getAbsLineAt(8))