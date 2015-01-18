# 自己抓到这个异常后，再往上抛
def example():
    try:
        int('n')
    except ValueError:
        print('do not work')
        raise

example()