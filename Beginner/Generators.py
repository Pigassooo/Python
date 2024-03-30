def remote_control_next():
    yield 'cnn'
    yield 'cctv'

itr = remote_control_next()
print(next(itr))
print(next(itr))
