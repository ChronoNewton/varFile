from dataclasses import replace


class varFile:
    isKey_CaseSensitive = None
    
    varFileLocation = None
    varFileText = None
    varFileLines = None
    
    
    def __init__(self, file_location='', file_text='',   isKey_CaseSensitive=False):
        self.varFileLocation = file_location
        self.varFileText = file_text
        
        self.isKey_CaseSensitive = isKey_CaseSensitive
    
    
    def SplitLines(self):
        self.varFileLines = self.varFileText.split('\n')
        #print(self.varFileLines)  # used to output the list of 'varFileLines'
    
    
    
    def readVarFile(self, file_location=''):
        file = None
        if(file_location != ''):# if file_location parameter was provided
            file = open(file_location, "rt")
        else:# if file_location parameter was NOT provided
            file = open(self.varFileLocation, "rt")
        
        self.varFileText = file.read()
        file.close()
        
        self.SplitLines()
    
    def writeVarFile(self, file_location=''):
        file = None
        if(file_location != ''):# if file_location parameter was provided
            file = open(file_location, "wt")
        else:# if file_location parameter was NOT provided
            file = open(self.varFileLocation, "wt")
        
        file.read(self.varFileText)
        file.close()
    
    
    
    def getVarFileText(self):# also  regenerates 'varFileText' from the list 'varFileLines'
        self.varFileText = ''
        for var_line in self.varFileLines:
            self.varFileText += var_line + '\n'
            
        return self.varFileText
    
    
    def getVarParts(self, var_line_text):
        if('=' not in var_line_text and ':' not in var_line_text and '\t' not in var_line_text): #check variable line if may not be properly formated
            raise Exception("varFile: var_line_text has no initializer(e.g. '=')\n" + "var_line_text:  " + var_line_text)
        
        #three sections_parts:
        # 1 = key
        # 2 initializer
        # 3 value
        section_part='1'
        part_key=''
        part_initializer=''
        part_value=''
        
        for i in range(len(var_line_text)):
            if(section_part=='1'):
                if(var_line_text[i] != '=' and var_line_text[i] != ':' and var_line_text[i] != '\t'):
                    part_key += var_line_text[i]
                else:
                    #section_part='2'
                    part_initializer=var_line_text[i] # here section part 2 is completed, then proceed to section part 3
                    section_part='3'
                
            elif(section_part=='3'):
                part_value+=var_line_text[i]
        
        return [part_key.strip(), part_initializer, part_value.strip()]
    
    


#
#
#            HERE starts the ".var" file data mainpulation functions
#
#
    
    
    def getValueByKey(self, key):
        if(self.isKey_CaseSensitive==False):key=key.lower()#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive
        
        value = None
        for variable_line in self.varFileLines:
            variable_line = variable_line.lstrip()#trim line for unwanted starting space
            if(self.isKey_CaseSensitive==False):variable_line=variable_line.lower()#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive

            if(variable_line.startswith(key)): 
                #print(variable_line)
                value = self.getVarParts(variable_line)[2]
                break
                
        return value
    
    
    def getValueByLineNumber(self, line_number):
        return self.getVarParts(self.varFileLines[line_number-1])[2]
    
    
    
    
    
    
    def setValueByKey(self, key, value):
        for i in range(len(self.varFileLines)):
            if(self.isKey_CaseSensitive==False):#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive
                if(self.varFileLines[i].lower().startswith(key.lower())):
                    self.varFileLines[i] = value
                    break
            
            else:#else then the search will be case-sensitive
                if(self.varFileLines[i].startswith(key)):
                    self.varFileLines[i] = value
                    break
        
        self.getVarFileText(self)#regenerate 'varFileText' from the list 'varFileLines'
        
    
    
    def setValueByLineNumber(self, line_number, value):
        self.varFileLines[line_number-1] = value
        
        self.getVarFileText(self)#regenerate 'varFileText' from the list 'varFileLines'
    
    
    
    
    
    
    
    
    def getVarByLineNumber(self, line_number):
        return self.getVarParts(self.varFileLines[line_number-1])
    
    
    
    
    
    
    
    def getAbsLineAt(self, line_number):
        return self.varFileLines[line_number-1]
    
    
    
    
    #        absolute line (e.g. "name: alex"  OR can be a comment "--this' a comment" )
    def appendAbsLineAt(self, abs_line, line_number=0):
        if(line_number==0):#if 'line_number' is 0 then append to the end(this is a special case number)
            self.varFileLines.append(abs_line)
        else:# if 'line_number' is > 0 then make it at the specified position line (e.g. 'line_number' is 1, then it will be the fist line..., and so for 2, second line)
            self.varFileLines.insert(line_number-1, abs_line)

        self.getVarFileText(self)#regenerate 'varFileText' from the list 'varFileLines'
        
        
        
        
    def replaceAbsLineByLineNumber(self, line_number, replace_with):
        self.varFileLines[line_number-1] = replace_with
        self.getVarFileText(self)
        
    


    def removeAbsLineByKey(self, key):# can be only used to remove variables(e.g. "name=alex")
        for i in range(len(self.varFileLines)):
            if(self.isKey_CaseSensitive==False):#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive
                if(self.varFileLines[i].lower().startswith(key.lower())):
                    del self.varFileLines[i]
                    break
            
            else:#else then the search will be case-sensitive
                if(self.varFileLines[i].startswith(key)):
                    del self.varFileLines[i]
                    break
        
        self.getVarFileText(self)#regenerate 'varFileText' from the list 'varFileLines'
        
        

    def removeAbsLineByLineNumber(self, line_number):# can be used to remove either variables(e.g. "name=alex")  OR comments
        del self.varFileLines[line_number-1]
        self.getVarFileText(self)#regenerate 'varFileText' from the list 'varFileLines'
        
        

    
    
    
    # no need for this any more since function 'appendAbsLineAt()' exists and is all comprehensive and shiny lol
    #       var line (e.g. ['name'],[':'],['alex'])
    #def appendVarLine(self, var_line, line_number=''):
    #    pass
    
    
    
#
#
#            HERE ends the ".var" file data mainpulation functions
#
#
    
    
    
    
    
    
    
    
    
    def convertValueToInt(self, value):
        return int(''.join(value.split()))
    
    
    def convertValueToBoolean(self, value):
        boolean_value = None
        if(value.lower() in ('true', 't', 'yes', 'y', '1')): boolean_value=True#if 'boolean_value' was detected as TRUE
        elif(value.lower() in ('false', 'f', 'no', 'n', '0')): boolean_value=False#if 'boolean_value' was detected as FALSE

        return boolean_value
    
    
    #not yet implemented!
    def convertValueToBytes(self, value):
        pass
    
    
    def clear():# note the function DOESNT clear the variable 'varFileLocation'
        varFile.varFileText = ''
        varFile.varFileLines = ''