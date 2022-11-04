def check_parity(parity, bin_str): 
    # your code here
    return 0 if any([bin_str.count('1')%2==0 and parity=='even', bin_str.count('1')%2==1 and parity=='odd' ]) else 1
