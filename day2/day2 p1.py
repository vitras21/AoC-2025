##                                 ###
## Solution by vitras21 (Vitaly.R) ###
##                                 ###

Letstore = 0
data = "8284583-8497825,7171599589-7171806875,726-1031,109709-251143,1039-2064,650391-673817,674522-857785,53851-79525,8874170-8908147,4197684-4326484,22095-51217,92761-107689,23127451-23279882,4145708930-4145757240,375283-509798,585093-612147,7921-11457,899998-1044449,3-19,35-64,244-657,5514-7852,9292905274-9292965269,287261640-287314275,70-129,86249864-86269107,5441357-5687039,2493-5147,93835572-94041507,277109-336732,74668271-74836119,616692-643777,521461-548256,3131219357-3131417388"
all_numbers = []
invalid_ids = set()
max_id_limit = 0 
base_sequence = 1
total_invalid_sum = 0

for letter in data:
    if letter.isdigit(): 
        Letstore = (Letstore * 10) + int(letter)
    elif letter == '-' or letter == ',':
        all_numbers.append(Letstore)
        Letstore = 0
    
if Letstore != 0:
    all_numbers.append(Letstore)

if all_numbers:
    max_id_limit = max(all_numbers)
else:
    max_id_limit = 0

while True:
    N_str = str(base_sequence)
    
    # Check if the shortest possible repetition (R=2) exceeds the limit. 
    # If so, we can stop the entire generation process.
    test_id_str = N_str + N_str
    if int(test_id_str) > max_id_limit:
        break
        
    repetition_count = 2
    while True:
        # Construct the ID by repeating the base sequence R times
        invalid_id_str = N_str * repetition_count
        invalid_id = int(invalid_id_str)
        
        if invalid_id > max_id_limit:
            break
            
        invalid_ids.add(invalid_id)
        
        repetition_count += 1
        
    base_sequence += 1
    
for i in range(0, len(all_numbers), 2):
    if i + 1 >= len(all_numbers):
        break 
        
    start_id = all_numbers[i]
    end_id = all_numbers[i + 1]
    
    for invalid_id in invalid_ids:
        if start_id <= invalid_id <= end_id:
            total_invalid_sum += invalid_id

print(total_invalid_sum)
