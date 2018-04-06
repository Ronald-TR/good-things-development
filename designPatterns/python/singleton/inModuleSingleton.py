class SingletonBase:
    def __init__(self, *args, **kwargs):
        super(SingletonBase, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'Calling the singleton module!!'


if not hasattr(globals(), 'standard_singleton'):
    standard_singleton = SingletonBase()

# to use the singleton, just do:
# from inModuleSingleton import standard_singleton
# and use it when you want