def killer(suspect_info, dead):
    for n, z in suspect_info.items():
        if all([a in z for a in dead]):
            return n
