def romanToInt(self, s: str) -> int:
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        arabic_num=int()    
        i=0
        while(len(s)-1>i):
         if roman_dict[s[i]]<roman_dict[s[i+1]]:
          arabic_num+=roman_dict[s[i+1]]-roman_dict[s[i]]
          i+=2      
         else:
          arabic_num+=roman_dict[s[i]]      
          i+=1
        if i==(len(s)-1):
         arabic_num+=roman_dict[s[i]]
        return(arabic_num)
romanToInt(1,"MCMXCIV")
#romanToInt(1,"III")