class Wrapper:
    def __init__(self, object):
        self.wrapped = object  # Save object

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)  # Trace fetch
        return getattr(self.wrapped, attrname)  # Delegate fetch


if __name__ == "__main__":
    x = Wrapper([1,2,3])
    x.append(4)
    print(x.wrapped)

    x = Wrapper({'a':1,'b':2})
    list(x.keys())