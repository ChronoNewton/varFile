from varFile import varFile

test_varFile = varFile('../test.var')
test_varFile.readVarFile()

print(test_varFile.getValueByKey('name'))
print(test_varFile.getValueByLineNumber(1))