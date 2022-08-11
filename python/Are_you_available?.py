def check_availability(schedule, current_time):
       c = current_time.replace(':' , '')
       c = int(c)
       for x in schedule : 
          a , b = x
          a = a.replace(':' , '')
          b = b.replace(':' , '')
          a = int(a)
          b = int(b)
          if all([a < c , c < b]) : 
            n = str(b)
            if len(n) == 3 : n = '0' + n
            n = n[:2] + ':' + n[2:]
            return n
       else : return True
