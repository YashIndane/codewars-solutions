def my_languages(results):
    # your fantastic code here
    return [x[0] for x in filter(lambda z: z[1] >= 60, sorted(results.items(), key=lambda x:x[1], reverse=True))]
