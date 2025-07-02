def next_greatest_letter(letters, tar_num):
    num_list=[ord(li) for li in letters]
    targ=ord(tar_num)
    num_list.append(targ)
    num_sor=sorted(num_list)
    ind=num_sor.index(targ)
    return chr(num_list[ind])
    

letters=['c', 'f', 'j'] 
target="k"

result=next_greatest_letter(letters, target)
print(result)