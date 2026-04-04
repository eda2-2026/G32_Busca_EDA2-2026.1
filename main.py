import csv

qa_list = None
with open("./qa.csv", "rt") as qa_csv:
    qa_list = list(csv.reader(qa_csv, dialect="excel"))
    print("csv carregado")

# Building index table 
qa_categories = set()
qa_categories.add(qa_list[1][0])
qa_index_table = {qa_list[1][0]: 1}

for qa_i in range(2, len(qa_list)):
    set_size = len(qa_categories)
    qa_categories.add(qa_list[qa_i][0])
    set_size -= len(qa_categories)
    if (set_size == -1):
        qa_index_table[qa_list[qa_i][0]] = qa_i

print(qa_index_table)

def qa_filter(category):
    # Search code here
    return qa_list

def qa_format(qa_selected):
    # Format Questions and Answers Here
    return "\n".join([", ".join(i) for i in qa_selected])

def on_post_page_macros(env):
    print(env.page.title)
    qa_filtered = qa_filter(category)
    env.markdown += qa_format(qa_filtered)


# Scrapped Idea
# def define_env(env):
#     @env.macro
#     def load_qa(category):
#         #qa_filtered = qa_filter(qa_list, category)
#         #print(qa_filtered)
#         #print([i for i in qa_list])
#         ...