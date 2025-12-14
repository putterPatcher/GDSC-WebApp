import solara

input_value = solara.reactive([])
input_label = solara.reactive([])
curr_rendered = solara.reactive(0)
max_rendered = solara.reactive(300)
load_more = solara.reactive(False)
prev_components = solara.reactive([])
disable_value = solara.reactive(False)
load_first = solara.reactive(False)

def components():
    end = 300 if len(input_value.value) - curr_rendered.value > 300 else len(input_value.value) - curr_rendered.value
    prev_components.value = prev_components.value + [solara.InputFloat(input_label.value[i+curr_rendered.value], value=input_value.value[i+curr_rendered.value], continuous_update=True) for i in range(0, end)]
    curr_rendered.value+=end
    print(curr_rendered.value, end, len(prev_components.value), "???")

@solara.lab.computed
def first_components():
    if input_label.value:
        curr_rendered.value = max_rendered.value if max_rendered.value < len(input_value.value) else len(input_value.value)
        prev_components.value = []
        load_first.value = False
        return [solara.InputFloat(input_label.value[i], value=input_value.value[i], continuous_update=True) for i in range(0, max_rendered.value if max_rendered.value < len(input_value.value) else len(input_value.value))]


@solara.component
def PredictForm(input_Value, input_Label, generate_output, x, disable=solara.reactive(False)):
    input_value.value = input_Value.value
    input_label.value = input_Label.value
    disable_value.value = disable.value
    with solara.Row(justify='center'):
        solara.Button("Predict", on_click=generate_output, style='color:white;background-color:black;width:15rem;', disabled=disable_value.value)
    solara.Text(x)
    load_first.value = True
    solara.Column(children=first_components.value+prev_components.value)
    if curr_rendered.value < len(input_value.value):
        solara.Button("More", on_click=components)
