# r
# w
# w+
# r+
# a: append
# ...b: binary 

# with open('data.txt', 'w') as file:
#     content = file.read()
#     print(content)
    
#     file.write("Read by me")
    
    
    # Only change Peter to Brian, keep everything the same
    # r - it only reads
    # w - it will erase the file before writing
    
    
# with open('./data.txt', 'r') as file_r:
#     file_content = file_r.read() # bigggggggggggg string
#     new_content = file_content.replace('Peter', 'Brian')
#     print(new_content)
    
#     with open('./data.txt', 'w') as file_w:
#         file_w.write(new_content + '\n')
#         file_w.write('THIS FILE HAS BEEN HACKED')
#         file_w.close()
    
#     file_r.close()
    
import json

with open('./score.json', 'r') as file_r:
    data_obj = json.load(file_r) #### DICTIONARY
    current_score = data_obj['score']
    print(f"Your current score is {current_score}")
    
    # new_score = input("Enter your new score: ")
    new_score = current_score * 2
    
    data_obj['score'] = new_score
    
    # print("NEW OBJ", data_obj)
    
    with open('./score.json', 'w') as file_w:
        json.dump(data_obj, file_w, indent=4)
        file_w.close()
    
    file_r.close()
    
    
    