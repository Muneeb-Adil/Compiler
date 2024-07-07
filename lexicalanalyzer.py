import re
import syntaxanalyzer

reserved_words = {"DT": ["intfl", "str", "bool"], "loop": ["goto"], "check": ["check"], "otherwise": ["otherwise"], "skip": ["skip"], "carryon": ["carryon"],
                  "start": ["start"], "bool_const": ["true", "false"], "return": ["return"], "AM": ["public", "private", "protected"], "this": ["this"],
                  "classs": ["classs"], "static": ["static"], "virtual": ["virtual"], "sealed": ["sealed"], "void": ["void"], "struct": ["struct"], "main": ["main"],
                  "new": ["new"], "try": ["try"], "catch": ["catch"], "finally": ["finally"]}


with open("democode.txt", "r") as f:
    code_lines = f.readlines()

temp = ""
temp2 = ""
temp3 = ""
a = False
b = False  # string checker
c = False  # multi line comment checker
d = False
e = False
f = False  # single line comment checker
g = False
h = False
c_float = False
check = False
check1 = False
check2 = False


class Token_maker:

    def __init__(self):
        self.token_set = []
        self.token = []

    def setter(self, cp, cv, line_no):
        self.token.append(cp)
        self.token.append(cv)
        self.token.append(line_no)
        self.token_set.append(self.token)
        self.token = []


obj_token_maker = Token_maker()


def iden_regex_checker(idn):
    pattern = re.compile(r"([a-zA-Z_]+[0-9]*)")
    match = re.match(pattern, idn)
    return match


def int_float_regex_checker(idn):
    pattern = re.compile(r"^([0-9]+)?(\.[0-9]+)?$")  # (^[0-9]*.[0-9]+$)
    match = re.match(pattern, idn)
    return match


for i in range(len(code_lines)):
    # print(code_lines[i],end="")
    #print(f"len of line {len(code_lines[i])}")

    for j in range(len(code_lines[i])):
        # print(code_lines[i][j])
        #print(i, j)

        if code_lines[i][j] == "\\" or code_lines[i][j] == " " or code_lines[i][j] == "(" or code_lines[i][j] == ")" or code_lines[i][j] == "[" or code_lines[i][j] == "]" or code_lines[i][j] == "{" or code_lines[i][j] == "}" or code_lines[i][j] == ";" or code_lines[i][j] == "," or code_lines[i][j] == "&" or code_lines[i][j] == "|" or code_lines[i][j] == "\n" or code_lines[i][j] == ":":

            if code_lines[i][j] == "\n" and f == True and g == False:
                f = False
                temp = ""

            if code_lines[i][j] == "\\" and b == True:
                if j+1 < len(code_lines[i]):
                    if code_lines[i][j+1] == "~":
                        temp += "~"
                        g = True
                        # print(temp,"1")

            if code_lines[i][j] == "\\" and b == True:
                if j+1 < len(code_lines[i]):
                    if code_lines[i][j+1] == "$":
                        temp += "$"
                        d = True

            if code_lines[i][j] == "\\" and b == False:
                if j+1 < len(code_lines[i]):
                    # when we have to use this in general manner
                    if code_lines[i][j+1] == "$":
                        temp += "$"
                        d = True

            if code_lines[i][j] == "\\" and c == True:
                if j+1 < len(code_lines[i]):
                    if code_lines[i][j+1] == "\"":
                        temp += "\""
                        e = True

            if code_lines[i][j] == "\\" and c == False:
                if j+1 < len(code_lines[i]):
                    # when we have to use this in general manner
                    if code_lines[i][j+1] == "\"":
                        temp += "\""
                        e = True

            # PUNCTUATORS & OPERATOR WORK DOWN HERE
            if b == False and c == False and f == False:

                if temp2 != "":
                    if temp2 == "+" or temp2 == "-":
                        obj_token_maker.setter("PM", temp2, i+1)
                        temp2 = ""
                    elif temp2 == "*" or temp2 == "/" or temp2 == "%":
                        obj_token_maker.setter("MDM", temp2, i+1)
                        temp2 = ""
                    elif temp2 == "=":
                        obj_token_maker.setter(temp2, "", i+1)
                        temp2 = ""
                    elif temp2 == "<" or temp2 == ">":
                        obj_token_maker.setter("relational op.", temp2, i+1)
                        temp2 = ""
                    elif temp2 == ">=" or temp2 == "<=" or temp2 == "==" or temp2 == "!=":
                        obj_token_maker.setter("relational op.", temp2, i+1)
                        temp2 = ""
                    elif temp2 == "+=" or temp2 == "-=" or temp2 == "*=" or temp2 == "/=" or temp2 == "%=":
                        obj_token_maker.setter("assignment op.", temp2, i+1)
                        temp2 = ""
                    else:
                        temp2 = ""

                # RESERVED WORDS WORK DOWN HERE
                # print(temp)
                if temp != "":
                    for k in reserved_words:
                        # print(k)
                        for l in range(len(reserved_words[k])):
                            # print(reserved_words[k][l])
                            # print(temp)
                            if reserved_words[k][l] == temp:
                                # print("matchedddddddd")
                                obj_token_maker.setter(k, temp, i+1)
                                temp = ""
                                a = True
                                break

                        if a == True:
                            a = False
                            break

                    # IDENTIFIER INT/FLOAT WORK START DOWN HERE
                    if a == False:
                        if temp == "":
                            continue
                        else:
                            # print(temp)
                            for g in range(len(temp)):
                                # print(temp)

                                if temp[g] == ".":

                                    for h in range(len(temp3)):
                                        if ord(temp3[h]) >= 65 and ord(temp3[h]) <= 90 or ord(temp3[h]) >= 97 and ord(temp3[h]) <= 122 or ord(temp3[h]) == 46:
                                            match = iden_regex_checker(temp3)
                                            if match == None:
                                                match1 = int_float_regex_checker(
                                                    temp3)
                                                if match1 == None:
                                                    # print(temp3)
                                                    obj_token_maker.setter(
                                                        "invalid lexemes", temp3, i+1)
                                                else:
                                                    obj_token_maker.setter(
                                                        "int/float", temp3, i+1)
                                            else:
                                                obj_token_maker.setter(
                                                    "idn", temp3, i+1)

                                            temp3 = ""

                                            if g+1 < len(temp):
                                                if ord(temp[g+1]) >= 65 and ord(temp[g+1]) <= 90 or ord(temp[g+1]) >= 97 and ord(temp[g+1]) <= 122:
                                                    obj_token_maker.setter(
                                                        "reference operator", ".", i+1)

                                            break

                                    if g+1 < len(temp):
                                        # print("1")
                                        if ord(temp[g+1]) >= 48 and ord(temp[g+1]) <= 57:
                                            temp3 += temp[g]
                                            temp3 += temp[g+1]
                                            check = True

                                    if temp[g] == ".":
                                        if g+1 < len(temp):
                                            if ord(temp[g-1]) >= 48 and ord(temp[g-1]) <= 57:
                                                if ord(temp[g+1]) >= 65 and ord(temp[g+1]) <= 90 or ord(temp[g+1]) >= 97 and ord(temp[g+1]) <= 122:
                                                    further_length = len(
                                                        temp) - g

                                                    if further_length == 2:
                                                        temp3 += temp[g]

                                                    else:
                                                        for n in range(g+1, further_length+1):
                                                            # print("g",g)
                                                            # print(temp[n])
                                                            if ord(temp[n]) >= 65 and ord(temp[n]) <= 90 or ord(temp[n]) >= 97 and ord(temp[n]) <= 122:
                                                                check1 = True
                                                            else:
                                                                check2 = True

                                                        if check1 == True and check2 == False:
                                                            temp3 += temp[g]

                                                        check1 = False
                                                        check2 = False

                                else:
                                    if check == True:
                                        check = False
                                    else:
                                        if temp[g] == ".":
                                            pass
                                        else:
                                            if temp3 == ".":
                                                temp3 = ""

                                            temp3 += temp[g]

                            temp = ""

                            if temp3 != "":
                                match = iden_regex_checker(temp3)
                                if match == None:
                                    match1 = int_float_regex_checker(temp3)
                                    if match1 == None:

                                        obj_token_maker.setter(
                                            "invalid lexemes", temp3, i+1)
                                    else:
                                        obj_token_maker.setter(
                                            "int/float", temp3, i+1)
                                else:
                                    obj_token_maker.setter("idn", temp3, i+1)

                                temp3 = ""

                if code_lines[i][j] == " ":
                    continue
                elif code_lines[i][j] == "\n":
                    continue
                else:
                    if code_lines[i][j] == "\\" and b == False:
                        obj_token_maker.setter("\\", "invalid lexemes", i+1)

                    elif code_lines[i][j] == "\\" and c == False:
                        obj_token_maker.setter("\\", "invalid lexemes", i+1)

                    elif code_lines[i][j] == "\\":
                        pass
                    else:
                        # print(code_lines[i][j])
                        obj_token_maker.setter(code_lines[i][j], "", i+1)

            else:
                if code_lines[i][j] == "\n":
                    continue
                else:
                    if d == True or e == True or g == True:
                        pass
                    else:
                        temp = temp + code_lines[i][j]

        elif code_lines[i][j] == ">" or code_lines[i][j] == "<" or code_lines[i][j] == "+" or code_lines[i][j] == "-" or code_lines[i][j] == "!" or code_lines[i][j] == "*" or code_lines[i][j] == "/" or code_lines[i][j] == "%" or code_lines[i][j] == "=":

            # PUNCTUATORS & OPERATOR WORK DOWN HERE
            if b == False and c == False and f == False:

                for g in range(len(temp)):
                    # print(temp)
                    if temp[g] == ".":
                        for h in range(len(temp3)):
                            if ord(temp3[h]) >= 65 and ord(temp3[h]) <= 90 or ord(temp3[h]) >= 97 and ord(temp3[h]) <= 122 or ord(temp3[h]) == 46:
                                match = iden_regex_checker(temp3)
                                if match == None:
                                    match1 = int_float_regex_checker(
                                        temp3)
                                    if match1 == None:
                                        # print(temp3)
                                        obj_token_maker.setter(
                                            "invalid lexemes", temp3, i+1)
                                    else:
                                        obj_token_maker.setter(
                                            "int/float", temp3, i+1)
                                else:
                                    obj_token_maker.setter(
                                        "idn", temp3, i+1)

                                temp3 = ""

                                if g+1 < len(temp):
                                    if ord(temp[g+1]) >= 65 and ord(temp[g+1]) <= 90 or ord(temp[g+1]) >= 97 and ord(temp[g+1]) <= 122:
                                        obj_token_maker.setter(
                                            "reference operator", ".", i+1)

                                break

                        if g+1 < len(temp):
                            # print("1")
                            if ord(temp[g+1]) >= 48 and ord(temp[g+1]) <= 57:
                                temp3 += temp[g]
                                temp3 += temp[g+1]
                                check = True

                        if temp[g] == ".":
                            if g+1 < len(temp):
                                if ord(temp[g-1]) >= 48 and ord(temp[g-1]) <= 57:
                                    if ord(temp[g+1]) >= 65 and ord(temp[g+1]) <= 90 or ord(temp[g+1]) >= 97 and ord(temp[g+1]) <= 122:
                                        further_length = len(temp) - g

                                        if further_length == 2:
                                            temp3 += temp[g]

                                        else:
                                            for n in range(g+1, further_length+1):
                                                # print("g",g)
                                                # print(temp[n])
                                                if ord(temp[n]) >= 65 and ord(temp[n]) <= 90 or ord(temp[n]) >= 97 and ord(temp[n]) <= 122:
                                                    check1 = True
                                                else:
                                                    check2 = True

                                            if check1 == True and check2 == False:
                                                temp3 += temp[g]

                                            check1 = False
                                            check2 = False
                    else:
                        if check == True:
                            check = False
                        else:
                            if temp[g] == ".":
                                pass
                            else:
                                if temp3 == ".":
                                    temp3 = ""

                                temp3 += temp[g]
                temp = ""

                if temp3 != "":
                    match = iden_regex_checker(temp3)
                    if match == None:
                        match1 = int_float_regex_checker(temp3)
                        if match1 == None:

                            obj_token_maker.setter(
                                "invalid lexemes", temp3, i+1)
                        else:
                            obj_token_maker.setter(
                                "int/float", temp3, i+1)
                    else:
                        obj_token_maker.setter("idn", temp3, i+1)

                    temp3 = ""

                if code_lines[i][j+1] != "=":
                    if code_lines[i][j] == "+" or code_lines[i][j] == "-":
                        obj_token_maker.setter("PM", code_lines[i][j], i+1)

                    elif code_lines[i][j] == "*" or code_lines[i][j] == "/" or code_lines[i][j] == "%":
                        obj_token_maker.setter("MDM", code_lines[i][j], i+1)

                    elif code_lines[i][j] == "=":
                        if code_lines[i][j-1] == "=" or code_lines[i][j-1] == "*" or code_lines[i][j-1] == "/" or code_lines[i][j-1] == "%" or code_lines[i][j-1] == ">" or code_lines[i][j-1] == "<" or code_lines[i][j-1] == "!" or code_lines[i][j-1] == "+" or code_lines[i][j-1] == "-":
                            pass
                        else:
                            obj_token_maker.setter(code_lines[i][j], "", i+1)

                    elif code_lines[i][j] == "<" or code_lines[i][j] == ">":

                        obj_token_maker.setter(
                            "relational op.", code_lines[i][j], i+1)

                    elif code_lines[i][j] == "!":
                        obj_token_maker.setter(
                            "invalid lexemes", code_lines[i][j], i+1)
                else:
                    if code_lines[i][j] == ">" or code_lines[i][j] == "<" or code_lines[i][j] == "=" or code_lines[i][j] == "!":
                        obj_token_maker.setter(
                            "relational op.", code_lines[i][j]+"=", i+1)

                    elif code_lines[i][j] == "+" or code_lines[i][j] == "-" or code_lines[i][j] == "*" or code_lines[i][j] == "/" or code_lines[i][j] == "%":
                        obj_token_maker.setter(
                            "assignment op.", code_lines[i][j]+"=", i+1)

            else:
                temp += code_lines[i][j]

        elif code_lines[i][j] == "\"" and b == True and e == False and c == False and h == False:
            b = False            # string off
            obj_token_maker.setter("string const", temp, i+1)
            temp = ""

        elif code_lines[i][j] == "$" and c == True and d == False:
            c = False  # multi line comment off
            temp = ""

        elif code_lines[i][j] == "~" and f == True:
            h = True

        elif code_lines[i][j] == "~" and c == False and b == False and f == False:
            f = True  # single line comment on

        elif code_lines[i][j] == "\"" and e == False and c == False and f == False:
            b = True           # string on

        elif code_lines[i][j] == "$" and d == False and f == False:
            c = True           # multi line comment on

        elif j == len(code_lines[i])-1:
            temp += code_lines[i][j]

        else:                   # main else
            if d == True or e == True or g == True:
                pass
            else:
                if code_lines[i][j] == "~":
                    h = True
                else:
                    temp = temp + code_lines[i][j]
                    # print(temp,"2")

        if code_lines[i][j] == "\\":
            if j+1 < len(code_lines[i]):
                if code_lines[i][j+1] == "$":
                    pass
        else:
            d = False

        if code_lines[i][j] == "\\":
            if j+1 < len(code_lines[i]):
                if code_lines[i][j+1] == "\"":
                    pass
        else:
            e = False

        if code_lines[i][j] == "\\":
            if j+1 < len(code_lines[i]):
                if code_lines[i][j+1] == "\n":
                    pass
        else:
            g = False


if temp != "":
    obj_token_maker.setter("invalid lexemes", temp, len(code_lines))


obj_token_maker.setter("end marker", "#", len(code_lines))


""" for l in range(len(obj_token_maker.token_set)):
    print(obj_token_maker.token_set[l])
 """

with open("tokenset.txt", "w") as f:
    for l in range(len(obj_token_maker.token_set)):
        f.write("[")
        f.write(obj_token_maker.token_set[l][0])
        f.write(" , ")
        f.write(obj_token_maker.token_set[l][1])
        f.write(" , ")
        f.write(str(obj_token_maker.token_set[l][2]))
        f.write("]")
        f.write("\n")


syntaxanalyzer.main(obj_token_maker.token_set)
