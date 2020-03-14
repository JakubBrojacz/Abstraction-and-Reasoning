def flattener(pred):
    str_pred = str([row for row in pred])
    str_pred = str_pred.replace(', ', '')
    str_pred = str_pred.replace('[[', '|')
    str_pred = str_pred.replace('][', '|')
    str_pred = str_pred.replace(']]', '|')
    return str_pred

def add_results(results, file_path, i, result):
    results.append(file_path[file_path.rfind("/")+1:file_path.rfind(".json")] + "_" + str(i) + ",", flattener(result) + "\n")

def save_results(results, file_name):
    with open(file_name, 'w') as file:
        file.write("output_id,output\n")
        for result in results:
            file.write(result)
