from chapter_14.listing_14_08.program import CustomFuture

future = CustomFuture()

i = 0

while True:
    try:
        print('Checking future...')
        gen = future.__await__()
        print("after await")
        send_res = gen.send(None)
        print(type(send_res))
        print('Future is not done...')
        if i == 1:
            print('Setting future value...')
            future.set_result('Finished!')
        i = i + 1
    except StopIteration as si:
        print(f'Value is: {si.value}')
        break