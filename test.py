import json

samples = []

with open("Eval.txt", 'r') as f:
    data = f.readlines()

    for i in range(0, int(len(data)/8)):
        sample = {}
        start_idx = i * 8
        sample['#'] = i
        sample['label'] = data[start_idx+1]
        sample['para'] = data[start_idx+2]
        sample['question'] = data[start_idx+3]
        sample['choices'] = data[start_idx+4:start_idx+8]
        samples.append(sample)



with open("Eval_reformatted.json", 'w') as optf:
    json.dump(samples, optf, indent=4)
