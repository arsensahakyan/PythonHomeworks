import os


# Ruben
def create_a_testing_work_environment(main_path):
    filepath = os.path.join(main_path, create_a_testing_work_environment.paths['dirname'][0])
    os.mkdir(filepath)
    for i in range(len(create_a_testing_work_environment.paths['dirname'])):
        if create_a_testing_work_environment.paths['files'][i]:
            for file in create_a_testing_work_environment.paths['files'][i]:
                filepath = os.path.join(main_path, file)
                with open(filepath, 'w'):
                    pass
        if create_a_testing_work_environment.paths['directories'][i]:
            for directname in create_a_testing_work_environment.paths['directories'][i]:
                filepath = os.path.join(main_path, directname)
                os.mkdir(filepath)
    print('Directory created !')


create_a_testing_work_environment.paths = {
    'dirname': ["test", "test/dir_1", "test/dir_1/dir_3", "test/dir_1/dir_3/dir_4", "test/dir_1/dir_3/dir_5",
                "test/dir_2", "test/dir_2/dir_6", "“test/dir_2/dir_7"],
    'files': [['test/file_1.txt', 'test/file_2.txt'], ['test/dir_1/file_3.txt', 'test/dir_1/file_4.txt'],
              ['test/dir_1/dir_3/file_5.txt', 'test/dir_1/dir_3/file.6.txt'], ['test/dir_1/dir_3/dir_4/file_7.txt'],
              None, ['test/dir_2/file_8.txt'], ['test/dir_2/dir_6/file_9.txt', 'test/dir_2/dir_6/file_10.txt'],
              ['test/dir_2/dir_7/file_11.txt']],
    'directories': [['test/dir_1', 'test/dir_2'], ['test/dir_1/dir_3'], ['test/dir_1/dir_3/dir_4',
                                                                         'test/dir_1/dir_3/dir_5'],
                    None, None, ['test/dir_2/dir_6', 'test/dir_2/dir_7'], None, None]
}

create_a_testing_work_environment('C:/Users/Admin/Desktop/')


def delete_all_the_files_and_directories_recursively(directory):
    if delete_all_the_files_and_directories_recursively.drname == '':
        delete_all_the_files_and_directories_recursively.drname = os.path.split(directory)[1]
    drlen = -len(delete_all_the_files_and_directories_recursively.drname)
    print(f'dir : {delete_all_the_files_and_directories_recursively.drname}')
    for path in os.listdir(directory):
        new_path = os.path.join(directory, path)
        if os.path.isfile(new_path):
            os.remove(new_path)
            if not os.listdir(directory) and directory[drlen:] != \
                    delete_all_the_files_and_directories_recursively.drname:
                os.rmdir(directory)
        elif os.path.isdir(new_path):
            if not os.listdir(new_path) and directory[drlen:] != \
                    delete_all_the_files_and_directories_recursively.drname:
                os.rmdir(new_path)
                if not os.listdir(directory) and path != delete_all_the_files_and_directories_recursively.drname:
                    os.rmdir(new_path)
            else:
                delete_all_the_files_and_directories_recursively(new_path)


delete_all_the_files_and_directories_recursively.drname = ''
delete_all_the_files_and_directories_recursively('C:/Users/Admin/Desktop/test')
