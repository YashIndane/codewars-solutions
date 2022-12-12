def hex_to_base64(hex: str) -> str:
    import codecs
    b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
    return b64[:-1]
