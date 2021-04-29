def alpha_sort(string):
    word_list = string.split()
    no_dup = list(set(word_list))
    no_dup.sort()
    outstr = f"{no_dup[0]}"
    for i in range(1, len(no_dup)):
        outstr += f" {no_dup[i]}"
    return outstr 
