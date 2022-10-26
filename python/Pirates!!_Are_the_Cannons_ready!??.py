def cannons_ready(gunners):
     return 'Shiver me timbers!' if list(gunners.values()).count('nay') >= 1 else 'Fire!'
