import solara

input_value = solara.reactive([])
input_label = solara.reactive([])
curr_rendered = solara.reactive(0)
max_rendered = solara.reactive(50)
prev_components = solara.reactive([])
disable_value = solara.reactive(False)
load_first = solara.reactive(True)
first_components_list = solara.reactive([])
prev_label_id = solara.reactive(None)
prev_input_id = solara.reactive(None)
# load_more = solara.reactive(False)

# def components():
#     load_more.value = not load_more.value

def add_components():
    end = 50 if len(input_value.value.value) - curr_rendered.value > 50 else len(input_value.value.value) - curr_rendered.value
    if end != 0:
        prev_components.value += [solara.InputInt(input_label.value.value[i+curr_rendered.value], value=input_value.value.value[i+curr_rendered.value], continuous_update=True) for i in range(0, end)]
        curr_rendered.set(curr_rendered.value+end)
        print(curr_rendered.value, end, len(prev_components.value), len(input_label.value.value), len(input_value.value.value), "???")
    # return prev_components.value

# @solara.lab.computed
# def load_components():
#     print(load_more.value, "???!!!")
#     if load_more.value:
#         return add_components()
#     else:
#         return add_components()

def first_components():
    curr_rendered.value = max_rendered.value if max_rendered.value < len(input_value.value.value) else len(input_value.value.value)
    # load_first.value = False
    return [solara.InputInt(input_label.value.value[i], value=input_value.value.value[i], continuous_update=True) for i in range(0, max_rendered.value if max_rendered.value < len(input_value.value.value) else len(input_value.value.value))]


@solara.component
def PredictForm(input_Value, input_Label, generate_output, x, disable=solara.reactive(False)):
    if id(input_Label) != prev_label_id.value or id(input_Value) != prev_input_id.value:
        prev_label_id.value = id(input_Label)
        prev_input_id.value = id(input_Value)
        input_value.value = []
        input_label.value = []
        curr_rendered.value = 0
        prev_components.value = []
        disable_value.value = False
        load_first.value = True
        first_components_list.value = []
    if load_first.value:
        input_value.value, input_label.value = input_Value, input_Label
        disable_value.value = disable.value
        first_components_list.value = first_components()
        load_first.value = False
    with solara.Row(justify='center'):
        solara.Button("Predict", on_click=generate_output, style='color:white;background-color:black;width:15rem;', disabled=disable_value.value)
    solara.Text(x)
    solara.Column(children=first_components_list.value)
    solara.Column(children=prev_components.value)
    if curr_rendered.value < len(input_value.value.value):
        solara.Button("More", on_click=add_components)