def substring_test(s1, s2):
     s1 = s1.lower()
     s2 = s2.lower()
     a = len(s1) if len(s1) <= len(s2) else len(s2)
     s = s1 if len(s1) == a else s2
     s_b = s1 if s1 != s else s2
     for i in range(a - 1) : 
       if s[i : i + 2] in s_b : return True
     return False
