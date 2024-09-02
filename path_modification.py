from tqdm import tqdm

def path_modification(path_to_datasets):
    purposes = ['baseline', 'adaptation']
    split_list = ['train', 'valid', 'test']
    durations = ['1min', '5min', '15min', '30min', '45min']

    for purpose in purposes:
        if purpose == 'baseline':
            for split in split_list:
                tsv_pth = f'{purpose}/{split}.tsv'
                tsv_lines = open(tsv_pth).readlines()
                new_tsv_lines = [x.replace('/Path_to_Datasets', path_to_datasets) for x in tsv_lines]
                
                with open(tsv_pth, 'w') as f:
                    f.write(''.join(new_tsv_lines))
                    
        elif purpose == 'adaptation':
            for duration in durations:
                for i in range(20):
                    id = str(i+1).zfill(5)                
                    for split in split_list:
                        tsv_pth = f'{purpose}/{duration}/voxlrs-{id}/{split}.tsv'
                        tsv_lines = open(tsv_pth).readlines()
                        new_tsv_lines = [x.replace('/Path_to_Datasets', path_to_datasets) for x in tsv_lines]
                    
                    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='replace the path in manifest', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataset_pth', type=str, help='path to preprocessed datasets')
    args = parser.parse_args()
    path_modification(args.dataset_pth)