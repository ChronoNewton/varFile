class varFile:
    isKey_CaseSensitive = None
    
    varFile_Location = None
    varFile_Text = None
    varFile_Lines = None
    
    
    def __init__(self,
                 file_location='', file_text='',
                 isKey_CaseSensitive=False):
        self.varFile_Location = file_location
        self.varFile_Text = file_text
        
        self.isKey_CaseSensitive = isKey_CaseSensitive
    
    
    def Split_Lines(self):
        self.varFile_Lines = self.varFile_Text.split('\n')
        #print(self.varFile_Lines)  #used to output the list of 'varFile_Lines'
    
    def Get_varFile_Text(self):#regenerates 'varFile_Text' from the list 'varFile_Lines'
        self.varFile_Text = '\n'.join(self.varFile_Lines)

            
        return self.varFile_Text
    
    
    def Read_VarFile(self, file_location=''):
        file = None
        if file_location != '':#if file_location parameter was provided
            file = open(file_location, "rt")
        else:#if file_location parameter was NOT provided
            file = open(self.varFile_Location, "rt")
        
        self.varFile_Text = file.read()
        file.close()
        
        self.Split_Lines()
    
    def Write_VarFile(self, file_location=''):
        file = None
        if file_location != '':#if file_location parameter was provided
            file = open(file_location, "wt")
        else:#if file_location parameter was NOT provided
            file = open(self.varFile_Location, "wt")
        
        self.Get_varFile_Text()#regenerate 'varFile_Text' from the list 'varFile_Lines'
        file.write(self.varFile_Text)
        file.close()
    
    
    #short for: variable parts(1 2 3)
    def Get_Var_Parts(self, var_line_text):
        if('=' not in var_line_text and 
           ':' not in var_line_text and
           '\t' not in var_line_text):#check variable line if may not be properly formated
            raise Exception("varFile: var_line_text has no initializer(e.g. '=')\n" + "var_line_text:  " + var_line_text)
        
        if(var_line_text[0] == '#' or
           (var_line_text[0] == '/' and var_line_text[1] == '/') or
           (var_line_text[0] == '-' and var_line_text[1] == '-')):#check variable line if may be a comment(starts with a comment mark)
            raise Exception("varFile: var_line_text starts with a comment mark(e.g. '#')\n" + "var_line_text:  " + var_line_text)
        
        #three sections_parts:
        # 1 = key
        # 2 initializer
        # 3 value
        section_part='1'
        part_key=''
        part_initializer=''
        part_value=''
        
        for i in range(len(var_line_text)):
            if section_part=='1':
                if(var_line_text[i] != '=' and
                   var_line_text[i] != ':' and
                   var_line_text[i] != '\t'):
                    part_key += var_line_text[i]
                else:
                    #section_part='2'
                    part_initializer=var_line_text[i] #here section part 2 is completed, then proceed to section part 3
                    section_part = '3'
                
            elif section_part == '3':
                part_value+= var_line_text[i]
        return [part_key.strip(), part_initializer, part_value.strip()]


    #HERE starts the ".var" file data manipulation functions
    def Get_Value_ByKey(self, key):
        if not self.isKey_CaseSensitive:
            key = key.lower()#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive
        
        for variable_line in self.varFile_Lines:
            variable_line = variable_line.lstrip()#trim line for unwanted starting space
            
            try:
                variable_line_parts = self.Get_Var_Parts(variable_line)#get variable line parts
            except Exception:
                continue
            
            if not self.isKey_CaseSensitive:
                variable_line_parts[0] = variable_line_parts[0].lower()#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive

            if variable_line_parts[0] == key: 
                return variable_line_parts[2]

    
    def Get_Value_ByLineNumber(self, line_number):
        try:
            return self.Get_Var_Parts(self.varFile_Lines[line_number-1])[2]
        except Exception:
            return None

    
    def Set_Value_ByKey(self, key, value):
        for i in range(len(self.varFile_Lines)):
            if not self.isKey_CaseSensitive:#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive
                if self.varFile_Lines[i].lower().startswith(key.lower()):
                    self.varFile_Lines[i] = value
                    break
            
            else:#else then the search will be case-sensitive
                if self.varFile_Lines[i].startswith(key):
                    self.varFile_Lines[i] = value
                    break
        
        self.Get_varFile_Text()#regenerate 'varFile_Text' from the list 'varFile_Lines'
    
    
    def Set_Value_ByLineNumber(self, line_number, value):
        self.varFile_Lines[line_number-1] = value
        
        self.Get_varFile_Text()#regenerate 'varFile_Text' from the list 'varFile_Lines'
    
    
    #get variable line parts
    def Get_Var_ByLineNumber(self, line_number):
        return self.getVarParts(self.varFile_Lines[line_number-1])    
    
    
    def Get_AbsLine_At(self, line_number):
        return self.varFile_Lines[line_number-1]
    
    
    #absolute line (e.g. "name: alex"  OR can be a comment "--this' a comment" )
    def Append_AbsLine_At(self, abs_line, line_number=0):
        if line_number==0:#if 'line_number' is 0 then append to the end(this is a special case number)
            self.varFile_Lines.append(abs_line)
        else:# if 'line_number' is > 0 then make it at the specified position line (e.g. 'line_number' is 1, then it will be the fist line..., and so for 2, second line)
            self.varFile_Lines.insert(line_number-1, abs_line)

        self.Get_varFile_Text()#regenerate 'varFile_Text' from the list 'varFile_Lines'
        
    def Replace_AbsLine_ByLineNumber(self, line_number, replace_with):
        self.varFile_Lines[line_number-1] = replace_with
        self.Get_varFile_Text()

    def Remove_AbsLine_ByKey(self, key):#can be only used to remove variables(e.g. "name=alex")
        for i in range(len(self.varFile_Lines)):
            if not self.isKey_CaseSensitive:#if option 'isKey_CaseSensitive' false, then the search will be case-INsensitive
                if self.varFile_Lines[i].lower().startswith(key.lower()):
                    del self.varFile_Lines[i]
                    break
            else:#else then the search will be case-sensitive
                if self.varFile_Lines[i].startswith(key):
                    del self.varFile_Lines[i]
                    break
        self.Get_varFile_Text(self)#regenerate 'varFile_Text' from the list 'varFile_Lines'

    def Remove_AbsLine_ByLineNumber(self, line_number):#can be used to remove either variables(e.g. "name=alex")  OR comments
        del self.varFile_Lines[line_number-1]
        self.Get_varFile_Text(self)#regenerate 'varFile_Text' from the list 'varFile_Lines'
        
#HERE ends the ".var" file data manipulation functions
    
    
    def Convert_ValueToInt(self, value):
        return int(''.join(value.split()))
    
    def Convert_ValueToBoolean(self, value):
        boolean_value = None
        if value.lower() in ('true', 't', 'yes', 'y', '1'):
            boolean_value=True#if 'boolean_value' was detected as TRUE
        elif value.lower() in ('false', 'f', 'no', 'n', '0'):
            boolean_value=False#if 'boolean_value' was detected as FALSE
        return boolean_value
    
    
    #not yet implemented!
    #def convertValueToBytes(self, value):
    #    pass
    
    
    def Clear(self):# note the function DOESNT clear the variable 'varFile_Location'
        self.varFile_Text = ''
        self.varFile_Lines = ''