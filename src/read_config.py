def read_config():
    file = open('config.txt', 'r')
    string = file.readline().split()                        # читаем первую строку
    if string[0] != 'type' or string[1] != '=':
        raise Exception("file config.txt is corrupted")

    if string[2] in ('simple', 'hard'):
        type_ = string[2]
    else:
        raise Exception("file config.txt is corrupted")

    string = file.readline().split()                        # читаем вторую строку
    if string[0] != 'location_of_input_data' or string[1] != '=':
        print(string)
        raise Exception("file config.txt is corrupted")
    path_of_incoming_file = string[2]

    string = file.readline().split()                        # читаем третью строчку
    if string[0] != 'location_of_output_data' or string[1] != '=':
        raise Exception("file config.txt is corrupted")
    path_to_the_output_file = string[2]
        
    
    file.close()
    return [type_, path_of_incoming_file, path_to_the_output_file]
