lst_one_pos = []
lst_val = []
lst_dir = ["north", "south", "west", "east","front", "right", "left","back"]
lst_turn = ["left","right","around"]
lst_turnto = ["north", "south", "west", "east"]
p = []
lst_type = {"jump": lst_val,"walk":[lst_val,lst_dir],"leap": [lst_val,lst_dir],"turn":lst_turn,"turnto":lst_turnto,"drop":lst_val,"get":lst_val, "grab":lst_val, "letGo":lst_val, "nop": None}



while True:
    txt = input("ingrese le comando para el robot: ")    
    def comprobar_txt(txt, cV):
        
        if "defVar" in txt:
                txt = txt.split(" ")
                lst_val.append(txt[1])
                
                return True
        else: 
            for i in cV.keys():
                if i in txt:
                    if len (cV[i]) > 1:
                        if "," in txt:
                            
                            for var in  cV[i][0]:
                                if var in txt:
                                    
                                    for dir in cV[i][1]:
                                        if dir in txt:
                                            return True 
                                    return False
                            return False
                        
                        else:
                            for var in  cV[i]:
                                if var in txt:
                                    return True
                            return False
                    else:
                        for p in cV[i]:
                            if p in txt:
                                return True
                        return False

        return False
    print(comprobar_txt(txt,lst_type))