def solve(nums, div):
    return list(map(lambda x: x+x%div, nums)) if nums else []
