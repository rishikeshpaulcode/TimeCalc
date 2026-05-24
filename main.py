# import libraries
from timecalc import exceptions as e
from timecalc.time import Time

# global constants
OPERATORS = ("+", "-", "/", "*", ">>", "==", "!=", "<", "<=", ">", ">=", "(", ")")
KEYWORDS = ("exit", "now", "ans", "rand")

# initializing state
exp_str = ""
exp_seq = []
timestamps = []
prev_ans = None

# display title
print('=' * 30)
print('TIME CALCULATOR'.center(30))
print('=' * 30, end='\n\n\n')

# main loop
while True:
    # accept expression
    input_raw = input("\n>> ")

    # tokenization
    exp_seq = list(filter(lambda x: x, input_raw.split(' ')))

    try:
        # parsing
        for item in exp_seq:
            if item in OPERATORS:
                exp_str += f"{item} "
            
            elif item in KEYWORDS:
                if item == "exit":
                    quit(0)
                elif item == "now":
                    timestamps.append(Time.now())
                elif item == "rand":
                    timestamps.append(Time.rand())
                else:
                    timestamps.append(prev_ans)
                
                exp_str += f"timestamps[{len(timestamps) - 1}] "
            
            elif item.isdigit():
                exp_str += f"{item} "
            
            else:
                # item must be timestamp
                new_timestamp = Time(item)
                timestamps.append(new_timestamp)
                exp_str += f"timestamps[{len(timestamps) - 1}] "

        # evaluation
        result = eval(exp_str)
        print(">>", result)
    
    except e.NullValueError as error:
        print(f"{error.error_message}")
        continue
    
    except e.FormatError as error:
        print(f"{error.error_message} [{error.error_item}]")
        continue
    
    except e.InvalidOperandError as error:
        print(f"{error.error_message} [{error.error_item}]")
        continue
    
    except e.ZeroDivisionError as error:
        print(f"{error.error_message}")
        continue

    # reset state
    exp_str = ""
    exp_seq.clear()
    timestamps.clear()
    prev_ans = result
