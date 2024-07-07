
i = 0


def NEW(token):
    global i

    if token[i][0] == "[":
        i += 1
        if token[i][0] == "]":
            i += 1
            if NEW(token):
                return True
    if token[i][0] == "idn" or token[i][0] == "," or token[i][0] == "=":
        i += 1
        return True

    return False


def NEAR2(token):
    global i

    if token[i][0] == "(":
        i += 1
        if func(token):
            return True
    if token[i][0] == ";":
        i += 1
        return True

    return False


def NEAR(token):
    global i

    if token[i][0] == "idn":
        i += 1
        if NEAR2(token):
            return True
    if token[i][0] == "=":
        i += 1
        if array(token):
            if token[i][0] == ";":
                i += 1
                return True

    return False


def N3(token):
    global i

    if token[i][0] == "=" or token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        if AO(token):
            if OE(token):
                if token[i][0] == ";":
                    i += 1
                    return True
    if token[i][0] == "(":
        i += 1
        if func(token):
            return True
    if token[i][0] == ";":
        i += 1
        return True

    return False


def N2(token):
    global i

    if token[i][0] == "[":
        i += 1
        if token[i][0] == "]":
            i += 1
            if NEW(token):
                if NEAR(token):
                    return True
    if token[i][0] == "idn":
        i += 1
        if N3(token):
            return True

    return False


def P(token):
    global i

    if token[i][0] == "DT":
        i += 1
        if NEW(token):
            if token[i][0] == "idn":
                i += 1
                return True
    if token[i][0] == "idn":
        i += 1
        if NEW(token):
            if token[i][0] == "idn":
                i += 1
                return True

    return False


def PLC(token):
    global i

    if token[i][0] == ",":
        i += 1
        if P(token):
            if PLC(token):
                return True
    if token[i][0] == ")":
        return True

    return False


def PL(token):
    global i

    if token[i][0] == "DT" or token[i][0] == "idn":
        i += 1
        if P(token):
            if PLC(token):
                return True
    if token[i][0] == ")":
        i += 1
        return True

    return False


def DD(token):
    global i

    if token[i][0] == "{":
        i += 1
        if MST(token):
            if token[i][0] == "}":
                i += 1
                return True
    if token[i][0] == ";":
        i += 1
        return True

    return False


def func(token):
    global i

    if token[i][0] == "(":
        i += 1
        if PL(token):
            if token[i][0] == ")":
                i += 1
                if DD(token):
                    if token[i][0] == ";":
                        i += 1
                        return True

    return False


def old1(token):
    global i

    if token[i][0] == "DT":
        i += 1
        if N2(token):
            return True
    if token[i][0] == "idn":
        i += 1
        if NEW(token):
            if token[i][0] == "idn":
                i += 1
                if func(token):
                    return True
    if token[i][0] == "void":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if func(token):
                return True

    return False


def old2(token):
    global i

    if token[i][0] == "idn":
        i += 1
        if old3(token):
            return True
    if token[i][0] == "=" or token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        if exp_array(token):
            if token[i][0] == ";":
                i += 1
                return True
    if token[i][0] == "[":
        i += 1
        if token[i][0] == "]":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if func(token):
                    return True

    return False


def old3(token):
    global i

    if token[i][0] == "(":
        i += 1
        if func(token):
            return True
    if token[i][0] == "=":
        i += 1
        if token[i][0] == "new":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if token[i][0] == "(":
                    i += 1
                    if AL(token):
                        if token[i][0] == ")":
                            i += 1
                            if token[i][0] == ";":
                                i += 1
                                return True

    return False


def old4(token):
    global i

    if token[i][0] == "idn":
        i += 1
        if NEW(token):
            if token[i][0] == "idn":
                i += 1
                if func(token):
                    return True
    if token[i][0] == "void":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if func(token):
                return True
    if token[i][0] == "DT":
        i += 1
        if NEW(token):
            if token[i][0] == "idn":
                i += 1
                if func(token):
                    return True

    return False


def oldd3(token):
    global i

    if token[i][0] == "=" or token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        if exp_array(token):
            if token[i][0] == ";":
                i += 1
                return True
    if token[i][0] == "idn":
        i += 1
        if old3(token):
            return True
    if token[i][0] == "(":
        i += 1
        if func(token):
            return True
    if token[i][0] == "[":
        i += 1
        if token[i][0] == "]":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if func(token):
                    return True

    return False


def AM(token):
    global i

    if token[i][0] == "public" or token[i][0] == "private" or token[i][0] == "protected" or token[i][0] == "static" or token[i][0] == "virtual" or token[i][0] == "idn" or token[i][0] == "DT" or token[i][0] == "void" or token[i][0] == "struct" or token[i][0] == "classs" or token[i][0] == "sealed":
        i += 1
        return True

    return False


def CSdefs(token):
    global i

    if token[i][0] == "static":
        i += 1
        if old1(token):
            return True
    if token[i][0] == "virtual":
        i += 1
        if old4(token):
            return True
    if token[i][0] == "idn":
        i += 1
        if oldd3(token):
            return True
    if token[i][0] == "DT":
        i += 1
        if N2(token):
            return True
    if token[i][0] == "void":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if func(token):
                return True
    if token[i][0] == "classs" or token[i][0] == "sealed":
        i += 1
        if classs(token):
            return True
    if token[i][0] == "struct" or token[i][0] == "sealed":
        i += 1
        if struct(token):
            return True

    return False


def SMB(token):
    global i

    if token[i][0] == "public" or token[i][0] == "private" or token[i][0] == "protected" or token[i][0] == "static" or token[i][0] == "virtual" or token[i][0] == "idn" or token[i][0] == "DT" or token[i][0] == "void" or token[i][0] == "struct" or token[i][0] == "classs" or token[i][0] == "sealed":
        i += 1
        if AM(token):
            if CSdefs(token):
                return True

    return False


def SM(token):
    global i

    if token[i][0] == "public" or token[i][0] == "private" or token[i][0] == "protected" or token[i][0] == "static" or token[i][0] == "virtual" or token[i][0] == "idn" or token[i][0] == "DT" or token[i][0] == "void" or token[i][0] == "struct" or token[i][0] == "classs" or token[i][0] == "sealed":
        i += 1
        if SMB(token):
            if SM(token):
                return True
    if token[i][0] == "}":
        i += 1
        return True

    return False


def SB(token):
    global i

    if token[i][0] == "{":
        i += 1
        if SM(token):
            if token[i][0] == "}":
                i += 1
                return True

    return False


def SD(token):
    global i

    if token[i][0] == ":":
        i += 1
        if AM(token):
            if token[i][0] == "idn":
                i += 1
                if SB(token):
                    if token[i][0] == ";":
                        i += 1
                        return True
    if token[i][0] == ";":
        i += 1
        return True
    if token[i][0] == "{":
        i += 1
        if SB(token):
            if token[i][0] == ";":
                i += 1
                return True

    return False


def classs(token):
    global i

    if token[i][0] == "classs":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if SD(token):
                return True
    if token[i][0] == "sealed":
        i += 1
        if token[i][0] == "classs":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if SB(token):
                    if token[i][0] == ";":
                        i += 1
                        return True

    return False


def struct(token):
    global i

    if token[i][0] == "struct":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if SD(token):
                return True
    if token[i][0] == "sealed":
        i += 1
        if token[i][0] == "struct":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if SB(token):
                    if token[i][0] == ";":
                        i += 1
                        return True

    return False


def defs(token):
    global i

    if token[i][0] == "static":
        i += 1
        if old1(token):
            return True
    if token[i][0] == "idn":
        i += 1
        if old2(token):
            return True
    if token[i][0] == "classs" or token[i][0] == "sealed":
        i += 1
        if classs(token):
            return True
    if token[i][0] == "struct" or token[i][0] == "sealed":
        i += 1
        if struct(token):
            return True

    return False


def old5(token):
    global i

    if token[i][0] == "idn":
        i += 1
        if k2(token):
            return True
    if token[i][0] == "=" or token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        if AO(token):
            if OE(token):
                if token[i][0] == ";":
                    i += 1
                    return True
    if token[i][0] == "reference operator":
        i += 1
        if A1(token):
            if AO(token):
                if OE(token):
                    if token[i][0] == ";":
                        i += 1
                        return True
    if token[i][0] == "(":
        i += 1
        if AL(token):
            if token[i][0] == ")":
                i += 1
                if A3(token):
                    if AO(token):
                        if OE(token):
                            if token[i][0] == ";":
                                i += 1
                                return True
    if token[i][0] == "[":
        i += 1
        if old6(token):
            return True

    return False


def old6(token):
    global i

    if token[i][0] == "idn" or token[i][0] == "this" or token[i][0] == "bool_const" or token[i][0] == "int/float" or token[i][0] == "string const":
        i += 1
        if OE(token):
            if token[i][0] == "]":
                i += 1
                if A1(token):
                    if AO(token):
                        if OE(token):
                            if token[i][0] == ";":
                                i += 1
                                return True
    if token[i][0] == "]":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if func(token):
                return True

    return False


def Next_ele(token):
    global i

    if token[i][0] == "}":
        i += 1
        return True
    if token[i][0] == ",":
        i += 1
        if R(token):
            if Next_ele(token):
                return True

    return False


def arr_ele(token):
    global i

    if token[i][0] == "idn" or token[i][0] == "this" or token[i][0] == "bool_const" or token[i][0] == "int/float" or token[i][0] == "string const" or token[i][0] == "{":
        i += 1
        if R(token):
            if Next_ele(token):
                return True
    if token[i][0] == "}":
        i += 1
        return True

    return False


def array(token):
    global i

    if token[i][0] == "{":
        i += 1
        if arr_ele(token):
            if token[i][0] == "}":
                i += 1
                return True

    return False


def exp_array(token):
    global i

    if token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        if OE(token):
            return True
    if token[i][0] == "=":
        i += 1
        if R(token):
            return True

    return False


def R(token):
    global i

    if token[i][0] == "idn" or token[i][0] == "this" or token[i][0] == "bool_const" or token[i][0] == "int/float" or token[i][0] == "string const":
        i += 1
        if OE(token):
            return True
    if token[i][0] == "{":
        i += 1
        if array(token):
            return True

    return False


def AO(token):
    global i

    if token[i][0] == "=":
        i += 1
        return True
    if token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        return True

    return False


def A1(token):
    global i

    if token[i][0] == "reference operator":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if A1(token):
                return True
    if token[i][0] == "[":
        i += 1
        if OE(token):
            if token[i][0] == "]":
                i += 1
                if A1(token):
                    return True
    if token[i][0] == "(":
        i += 1
        if AL(token):
            if token[i][0] == ")":
                i += 1
                if A3(token):
                    return True
    if token[i][0] == "=" or token[i][0] == "+=" or token[i][0] == "-=" or token[i][0] == "*=" or token[i][0] == "/=" or token[i][0] == "%=":
        i += 1
        return True

    return False


def A2(token):
    global i

    if token[i][0] == "reference operator":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if A1(token):
                return True
    if token[i][0] == "[":
        i += 1
        if OE(token):
            if token[i][0] == "]":
                i += 1
                if A1(token):
                    return True
    return False


def A3(token):
    global i

    if token[i][0] == ";":
        i += 1
        return True
    if token[i][0] == "reference operator" or token[i][0] == "[":
        i += 1
        if A2(token):
            return True

    return False


def ALC(token):
    global i

    if token[i][0] == ",":
        i += 1
        if A(token):
            if ALC(token):
                return True
    if token[i][0] == ")":
        i += 1
        return True

    return False


def AL(token):
    global i

    if token[i][0] == "idn" or token[i][0] == "this" or token[i][0] == "bool_const" or token[i][0] == "int/float" or token[i][0] == "string const":
        i += 1
        if A(token):
            if ALC(token):
                return True
    if token[i][0] == ")":
        i += 1
        return True

    return False


def A(token):
    global i

    if token[i][0] == "idn" or token[i][0] == "this" or token[i][0] == "bool_const" or token[i][0] == "int/float" or token[i][0] == "string const":
        i += 1
        if OE(token):
            return True

    return False


def k2(token):
    global i

    if token[i][0] == ";":
        i += 1
        return True
    if token[i][0] == "=":
        i += 1
        if token[i][0] == "new":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if token[i][0] == "(":
                    i += 1
                    if AL(token):
                        if token[i][0] == ")":
                            i += 1
                            if token[i][0] == ";":
                                i += 1
                                return True
    if token[i][0] == "(":
        i += 1
        if func(token):
            return True

    return False


def NEXT(token):
    global i

    if token[i][0] == ";":
        i += 1
        return True
    if token[i][0] == "idn" or token[i][0] == "this" or token[i][0] == "bool_const" or token[i][0] == "int/float" or token[i][0] == "string const":
        i += 1
        if OE(token):
            if token[i][0] == ";":
                i += 1
                return True

    return False


def ret(token):
    global i

    if token[i][0] == "return":
        i += 1
        if NEXT(token):
            return True

    return False


def skip(token):
    global i

    if token[i][0] == "skip":
        i += 1
        if token[i][0] == ";":
            i += 1
            return True

    return False


def carryon(token):
    global i

    if token[i][0] == "carryon":
        i += 1
        if token[i][0] == ";":
            i += 1
            return True

    return False


def NEXT3(token):
    global i

    if token[i][0] == "otherwise":
        i += 1
        if token[i][0] == "{":
            i += 1
            if MST(token):
                if token[i][0] == "}":
                    i += 1
                    return True

    return False


def check_otherwise(token):
    global i

    if token[i][0] == "check":
        i += 1
        if token[i][0] == "(":
            i += 1
            if OE(token):
                if token[i][0] == ")":
                    i += 1
                    if token[i][0] == "{":
                        i += 1
                        if MST(token):
                            if token[i][0] == "}":
                                i += 1
                                if NEXT3(token):
                                    return True

    return False


def until(token):
    global i

    if token[i][0] == "until":
        i += 1
        if token[i][0] == "(":
            i += 1
            if OE(token):
                if token[i][0] == ")":
                    i += 1
                    if token[i][0] == "{":
                        i += 1
                        if MST(token):
                            if token[i][0] == "}":
                                i += 1
                                return True

    return False


def catch(token):
    global i

    if token[i][0] == "catch":
        i += 1
        if NEXT2(token):
            if token[i][0] == ";":
                i += 1
                return True
    if token[i][0] == "finally":
        i += 1
        return True

    return False


def try_catch(token):
    global i

    if token[i][0] == "try":
        i += 1
        if token[i][0] == "{":
            i += 1
            if MST(token):
                if token[i][0] == "}":
                    i += 1
                    if catch(token):
                        if token[i][0] == "finally":
                            i += 1
                            if token[i][0] == "{":
                                i += 1
                                if MST(token):
                                    if token[i][0] == "}":
                                        i += 1
                                        return True

    return False


def NEXT2(token):
    global i

    if token[i][0] == "(":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if token[i][0] == "idn":
                i += 1
                if token[i][0] == ")":
                    i += 1
                    if token[i][0] == "{":
                        i += 1
                        if MST(token):
                            if token[i][0] == "}":
                                i += 1
                                return True
    if token[i][0] == "{":
        i += 1
        if MST(token):
            if token[i][0] == "}":
                i += 1
                return True

    return False


def SST(token):
    global i

    if token[i][0] == "check":
        i += 1
        if check_otherwise(token):
            return True
    if token[i][0] == "until":
        i += 1
        if until(token):
            return True
    if token[i][0] == "try":
        i += 1
        if try_catch(token):
            return True
    if token[i][0] == "this":
        i += 1
        if token[i][0] == "reference operator":
            i += 1
            if A1(token):
                if AO(token):
                    if OE(token):
                        if token[i][0] == ";":
                            i += 1
                            return True
    if token[i][0] == "static":
        i += 1
        if old1(token):
            return True
    if token[i][0] == "idn":
        i += 1
        if old5(token):
            return True
    if token[i][0] == "DT":
        i += 1
        if N2(token):
            return True
    if token[i][0] == "void":
        i += 1
        if token[i][0] == "idn":
            i += 1
            if func(token):
                return True
    if token[i][0] == "skip":
        i += 1
        if skip(token):
            return True
    if token[i][0] == "carryon":
        i += 1
        if carryon(token):
            return True
    if token[i][0] == "return":
        i += 1
        if ret(token):
            return True

    return False


def MST(token):
    global i

    if token[i][0] == "check" or token[i][0] == "until" or token[i][0] == "try" or token[i][0] == "this" or token[i][0] == "static" or token[i][0] == "idn" or token[i][0] == "DT" or token[i][0] == "void" or token[i][0] == "skip" or token[i][0] == "carryon" or token[i][0] == "return":
        i += 1
        if SST(token):
            if MST(token):
                return True
    if token[i][0] == "}":
        i += 1
        return True

    return False


def M1(token):
    global i

    if token[i][0] == "idn":
        i += 1
        if func(token):
            return True
    if token[i][0] == "main":
        i += 1
        if token[i][0] == "(":
            i += 1
            if token[i][0] == ")":
                i += 1
                if token[i][0] == "{":
                    i += 1
                    if MST(token):
                        if token[i][0] == "}":
                            i += 1
                            return True

    return False


def M2(token):
    global i

    if token[i][0] == "[" or token[i][0] == "idn":
        i += 1
        if N2(token):
            return True
    if token[i][0] == "main":
        i += 1
        if token[i][0] == "(":
            i += 1
            if token[i][0] == ")":
                i += 1
                if token[i][0] == "{":
                    i += 1
                    if MST(token):
                        if token[i][0] == "}":
                            i += 1
                            return True

    return False


def S(token):
    global i

    if token[i][1] == "#":    # end marker
        return True

    if token[i][0] == "void":
        i += 1
        if M1(token):
            if S(token):
                return True
    if token[i][0] == "DT":
        i += 1
        if M2(token):
            if S(token):
                return True
    if token[i][0] == "static" or token[i][0] == "idn" or token[i][0] == "struct" or token[i][0] == "class" or token[i][0] == "sealed":
        i += 1
        if defs(token):
            if S(token):
                return True

    return False


def main(token):
    if S(token):
        print(f"Compeletly parsed")
    else:
        print(f"Syntax error at line no: {token[i][2]}")
