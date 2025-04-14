def file_handler(input_file):
    try:
        with open(input_file, 'r') as r:
            content = r.read()
            #modify content
            modified_content = content.upper()

        output_file =  f"modified_{input_file}"
        with open(output_file, 'w') as w:
            w.write(modified_content)
        print(f" Modified file saved as: {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found")
    except PermissionError:
        print(f"Permission denied to read {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File handling operation completed")


def file_prompter():
    '''
    function handles the prompting of the values
    '''
    input_file = input("Enter file name to be modified: ")
    file_handler(input_file)
