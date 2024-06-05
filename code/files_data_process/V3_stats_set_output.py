import os
import json

class JSONREAD():
    def __init__(self) -> None:
        super().__init__()
    
    def get_ttschunk_successfull_example(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if "ttschunk_successfull_example" in data:
                successfull_example = data["ttschunk_successfull_example"]
            else:
                successfull_example = 0.0
        return successfull_example
    
    def run(self, json_dir):
        successfull_examples = []
        for name in os.listdir(json_dir):
            json_file = os.path.join(json_dir,name)
            successfull_example = self.get_ttschunk_successfull_example(json_file)
            successfull_examples.append(float(successfull_example))
        print(str(round(sum(successfull_examples)/3600, 5)))
    
JSON_INPUT_STEP = None

def init():

    global JSON_INPUT_STEP
    JSON_INPUT_STEP = JSONREAD()

    JSON_INPUT_STEP.prs_step_init()

def run(mini_batch):

    return JSON_INPUT_STEP.prs_step_run(mini_batch)

if __name__ == "__main__":
    json_read = JSONREAD()

    json_dir = r"C:\Users\v-zhazhai\Desktop\stats_set_output"
    json_read.run(json_dir)
    # json_read.get_ttschunk_successfull_example(r"C:\Users\v-zhazhai\Desktop\stats_set_output\stats_minibatch_10020_0.json")