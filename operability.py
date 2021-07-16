import numpy as np
import streamlit as st
import plotly.express as px

def operability(task_time, task_list, total):

    task_repartition = {}

    for task, time in zip(task_list, task_time):
        task_repartition[task] = time/total
        task_repartition['Divers'] = 10/total

    return task_repartition

def total_time(task_time, total):

    return ((sum(task_time)+10)/total) * 100

def camembert(task_repartition):

    labels = list(task_repartition.keys())
    values = list(task_repartition.values())

    return px.pie(values = values, names= labels)

st.title('Operability app')
st.write('Avec les paramètres à gauche, tu peux ajouter autant de tâches que tu veux, il suffit ensuite'
         ' de cliquer sur calculer à  la fin et tu as ton résultat')

with st.sidebar:
    st.title('Paramètres')
    nb_taches = st.number_input('Entrez le nombre de tâches', value=3)
    task_time = np.empty(shape=nb_taches)
    task_list = np.empty(shape=nb_taches)
    time_spent = st.number_input('Entrez le temps de travail total (en heures)', value=8)
    total_hour = time_spent * 60
    if not time_spent:
        st.warning('entrez un temps de travail ci-dessus')
    #if new_task:
    operateur = st.text_input('Nom de l\'opérateur')
    if not operateur:
        st.warning('Entrez un nom ci-dessus')

task_list = ['Bennes jaunes', 'Bennes vertes', 'Amorçage', 'Autocontrôle', 'Partiels']
for i in range(nb_taches):
    option = st.selectbox(f'Test {i+1}', task_list, key=i)
    h1,h2,h3,h4 = st.beta_columns(4)
    time = h1.number_input('Temps passé sur cette tâche', value=10, key=i)
    frequency = h2.number_input('Nombre de fois que cette tâche a été faite', value=1, key=1000*i)
    task_time[i] = time * frequency
    task_list[i] = option
    st.write(task_time[i])
if st.button('calculer'):
    task_dict = operability(task_time, task_list, total_hour)
    st.write(f'Temps efficace de {operateur}: {round(total_time(task_time, total_hour),2)} %')
    st.write(camembert(task_dict))
