def count_substring(string, sub_string):
    l=0
    count=0
    while(l != len(string)):
        c = string.find(sub_string,l,len(string))
        if(c!=-1):
            count += 1
            l = c+1
        else:
            l = len(string)
    return count

 if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)   