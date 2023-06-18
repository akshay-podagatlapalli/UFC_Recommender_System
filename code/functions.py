import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output, Javascript, HTML
import random


def handle_likert_scale1_change(change):
    responses['question1'] = change.new

def handle_likert_scale2_change(change):
    responses['question2'] = change.new

def handle_likert_scale3_change(change):
    responses['question3'] = change.new

def handle_likert_scale4_change(change):
    responses['question4'] = change.new

def handle_likert_scale5_change(change):
    responses['question5'] = change.new


def run():
    button = widgets.Button(description='Run Cells Below')
    output = widgets.Output()

    def run_all_cells(button):
        with output:
            clear_output(wait=True)  # Clear previous output
            display(Javascript('IPython.notebook.execute_cells_below()'))

    button.on_click(run_all_cells)

    display(button, output)

def create_button_widget():
    button = widgets.Button(description='See Results')
    output = widgets.Output()

    def run_all_cells(button):
        with output:
            clear_output(wait=True)  # Clear previous output
            display(Javascript('IPython.notebook.execute_cells_below()'))

    button.on_click(run_all_cells)

    display(button, output)
