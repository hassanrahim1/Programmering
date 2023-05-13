import PySimpleGUI as sg
import pandas as pd

def table():

    sg.set_options(auto_size_buttons=True)
    filename = sg.popup_get_file(
        'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        return

    data = []
    header_list = []
    button = sg.popup_yes_no('Does this file have column names already?')

    if filename is not None:
        try:
            # Header=None betyder att du direkt sätter columnnamnen i dataframen
            df = pd.read_csv(filename, sep=',', engine='python', header=None)

            # Läs allt i flera rader
            data = df.values.tolist()

            # Välj ja eller nej om din csv fil har namn på columnerna eller inte
            if button == 'Yes':
                #Använder namnen 8
                header_list = df.iloc[0].tolist()
                data = df[1:].values.tolist()

            elif button == 'No':
                #Gör custom columner t.ex. column0, column1, etc
                header_list = ['column' + str(x) for x in range(len(data[0]))]

        except:
            sg.popup_error('Fel vid läsning av fil')
            return

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]
    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()
    window.close()