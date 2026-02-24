import os
import json
from typing import List, Tuple
import argparse


def save_to_json(data: List[dict], output_file_path: str) -> bool:
    if not data: return False # No data to save -> skip file creation
    with open(output_file_path, 'w') as f:
        json.dump({
            item['function_name']: {
                'restype': item['return_type'],
                'argtypes': item['argtypes']
        } for item in data}, f, indent=4)
    return True


def split_type_and_name(segment: str) -> Tuple[str, str]:
    nb_stars = segment.count('*')
    segment = segment.replace('*', '')
    segment = segment.split(' ')
    segment = [element for element in segment if element]
    if not segment:
        raise ValueError("split_type_and_name: Segment is empty, cannot split type and name.")
    segment[-2] += '*' * nb_stars
    return ' '.join(segment[:-1]).replace('const ', ''), segment[-1]


def get_argtypes(params: str) -> List[str]:
    if not params.strip() or params.strip() == 'void':
        return []
    return [split_type_and_name(segment)[0].replace('const ', '') for segment in params.split(',')]


def parse_line(line: str) -> dict:
    parts = line.split('(')
    if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
        raise ValueError(f"parse_line: Line does not contain a valid function declaration: {line}")

    argtypes_end_index = parts[1].index(')')
    argtypes = parts[1][:argtypes_end_index]

    return_type, function_name = split_type_and_name(parts[0])

    return {
        'return_type': return_type,
        'function_name': function_name,
        'argtypes': get_argtypes(argtypes)
    }


def parse_input_file(input_file_path: str, start_line: str) -> List[str]:
    with open(input_file_path, 'r') as f:
        lines = f.readlines()

    data_list = []

    start_line_len = len(start_line)
    
    for line in lines:
        if not line.startswith(start_line): continue
        line = line[start_line_len:].strip()
        if not line: continue

        data = parse_line(line)
        if data:
            data_list.append(data)
    
    return data_list


def parse_file(input_file_path: str, output_file_path: str, start_line: str) -> bool:
    try:
        if output_file_path[-5:] != '.json':
            output_file_path += '.json'
        data_list = parse_input_file(input_file_path, start_line)
        return save_to_json(data_list, output_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def parse_all_files(folder_path: str, output_folder_path: str, start_line: str):
    for filename in os.listdir(folder_path):
        if filename.endswith('.h'):
            input_file_path = os.path.join(folder_path, filename)
            os.makedirs(output_folder_path, exist_ok=True)
            output_file_name = os.path.splitext(filename)[0] + '.json'
            output_file_path = os.path.join(output_folder_path, output_file_name)
            parse_file(input_file_path, output_file_path, start_line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse header files to extract function signatures and generate JSON specs.'
    )
    parser.add_argument(
        '--input', '-i',
        nargs='+',
        required=True,
        help='Input header file(s) or directory to parse'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Output directory for JSON files'
    )
    parser.add_argument(
        '--start-line', '-s',
        default='DLLEXPORT',
        help='Prefix to identify exported functions (default: DLLEXPORT)'
    )
    
    args = parser.parse_args()
    
    try:
        os.makedirs(args.output, exist_ok=True)
        files_to_process = []

        for path in args.input:
            
            # Check if input is a directory
            
            if os.path.isdir(path):
                for filename in os.listdir(path):
                    if filename.endswith('.h'):
                        files_to_process.append(os.path.join(path, filename))
            
            elif os.path.isfile(path) and path.endswith('.h'):
                files_to_process.append(path)

            else:
                raise ValueError(f"'{path}' is not a valid header file or directory.")
        
        if not files_to_process:
            raise ValueError("No header files found to process.")
        
        processed_files_count = 0
        empty_files_count = 0

        for input_file in files_to_process:
            filename = os.path.basename(input_file)
            output_file_name = os.path.splitext(filename)[0] + '.json'
            output_file_path = os.path.join(args.output, output_file_name)
            
            print(f"Processing: {input_file}")
            if parse_file(input_file, output_file_path, args.start_line):
                processed_files_count += 1
            else:
                empty_files_count += 1
                print(f"WARNING: No valid function signatures found in '{input_file}'. Skipping file creation.")
        
        print(f"Processing completed. {processed_files_count} file{'s' if processed_files_count > 1 else ''} generated, {empty_files_count} file{'s' if empty_files_count > 1 else ''} skipped due to no valid signatures.")
        
        error_files_count = len(files_to_process) - processed_files_count - empty_files_count
        if error_files_count > 0:
            print(f"WARNING: {error_files_count} file{'s' if error_files_count > 1 else ''} were not processed due to errors. Check the logs for details.")
        
    except Exception as e:
        print(f"Error: {e}")
        exit(1)