def store_it(while_it_was_event):
    f = open("log.txt", "a")    
    f.write(while_it_was_event)
    f.close()
