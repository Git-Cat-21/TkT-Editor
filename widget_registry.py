widget_registry={}
def register_widget(name,widget):
    widget_registry[name]=widget
def get_widget(name):
    return widget_registry.get(name)