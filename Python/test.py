from varFile import varFile



data_varfile = varFile('../test.var')
data_varfile.Read_VarFile()

#variable value is retrieved by its key(name), which is e.g. 'NAME'
print('My name is ' + data_varfile.Get_Value_ByKey('NAME'))

#variable value is retrieved by the line number, which is e.g. 7
print('My Ip is ' + data_varfile.Get_Value_ByLineNumber(7))

#entire variable line is retrieved by the line number, which is e.g. 8
print('\nfull variable line:\n' + data_varfile.Get_AbsLine_At(8))