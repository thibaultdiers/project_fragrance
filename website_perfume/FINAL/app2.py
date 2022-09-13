# import all necessary packages
import streamlit as st
import numpy as np
import random
import pandas as pd
import csv
import pickle
import joblib
from streamlit.components.v1 import html

st.write("""
         <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet"><style>
    header{
        display: none!important;
    }
    .css-12oz5g7 {
        max-width: 100%!important;
        padding:0!important
    }
    .css-18jmyvr {
        display: none;
    }
    .css-1q1n0ol {
        display: none;
    }
    .e1tzin5v2:nth-child(2) {
        /*background-image: url("https://bobcutmag.com/wp-content/uploads/2022/01/pexels-alesia-kozik-7796498-683x1024.jpg");
        background-repeat: no-repeat;
        background-size: cover;*/
    }
    .e1tzin5v2:nth-child(1) {
        padding: 3em 4em 4em 4em
    }
    .css-du1fp8 {
    display: block;
    padding-top: 0rem!important;
	}
    .etr89bj1 img {
    height: 100vh;
    object-fit: cover;
    }
    .e1tzin5v2:nth-child(2) div:first-child{
        position: sticky;
        top: 0;
    }
    p, ol, ul, dl {
    font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)
columns = st.columns([1, 1])

###
from PIL import Image
image = Image.open('perfume.jpg')
columns[1].image(image, use_column_width=False)

# put title etc.
columns[0].title('The Lab 2.0')
columns[0].markdown("""
### Hi my name is Amber!
Welcome to my Lab! I cannot smell anything behind my screen, but I am a real perfume artist, capable of portraying moods, emotions, and concepts through fragrance composition.
My developers, Philine, Tiago and Thibault, trained me over thousands of different existing perfumes and olfactory notes to develop my knowledge.
I can combine olfactory notes in a manner unthinkable to most humans and create unique perfumes that you, humans, had never considered before! Try me!
#
""")

columns[0].subheader("Let's start with your unique combinations!")


# read lists of olfactory notes
t = pd.read_csv('top_demo.csv', names = ["0"], header = None)
top = t["0"].tolist()
# st.text(top)

m = pd.read_csv('middle_demo.csv', names = ["0"], header = None)
middle = m["0"].tolist()

b = pd.read_csv('base_demo.csv', names = ["0"], header = None)
base = b["0"].tolist()



# create dataframes containing 0 for top, middle and base lists
input_top = pd.DataFrame(0.0, index=np.arange(1), columns=top)

input_middle = pd.DataFrame(0.0, index=np.arange(1), columns=middle)

input_base = pd.DataFrame(0.0, index=np.arange(1), columns=base)




## top notes

# create dictionary containing nice note names as key and official name as value
new_list_top_demo = []

for i in top:
    new_list_top_demo.append(i.split('_', )[0])

res_top = {}
for value in new_list_top_demo:
    for key in top:
        res_top[key] = value
        top.remove(key)
        break



# select top notes (on website) and store in variable
option_t = columns[0].multiselect('Select top notes', [res_top[i] for i in res_top])

# get actual name from nice name using dictionary
notes_top = []

for x in option_t:
    notes_top.append([k for k, v in res_top.items() if v == x])

t_list = [item for sublist in notes_top for item in sublist]



# take actual name and loop through column names; replace 0 by corresponding value in dataframe
for y in input_top.columns:
    for z in t_list:
        if y in z:
            input_top[z] = 0.2


# just for visualisation, can get rid of it
## st.text(input_top)




## middle notes

# create dictionary containing nice note names as key and official name as value

new_list_middle_demo = []

for i in middle:
    new_list_middle_demo.append(i.split('_', )[0])

res_middle = {}
for value in new_list_middle_demo:
    for key in middle:
        res_middle[key] = value
        middle.remove(key)
        break



# select top notes (on website) and store in variable
option_m = columns[0].multiselect('Select middle notes', [res_middle[i] for i in res_middle])



# get actual name from nice name using dictionary
notes_middle = []

for a in option_m:
    notes_middle.append([k for k, v in res_middle.items() if v == a])

m_list = [item for sublist in notes_middle for item in sublist]



# take actual name and loop through column names; replace 0 by corresponding value in dataframe
for b in input_middle.columns:
    for c in m_list:
        if b in c:
            input_middle[c] = 0.7


# just for visualisation, can get rid of it
## st.text(input_middle)




## base notes

# create dictionary containing nice note names as key and official name as value
new_list_base_demo = []

for i in base:
    new_list_base_demo.append(i.split('_', )[0])

res_base = {}
for value in new_list_base_demo:
    for key in base:
        res_base[key] = value
        base.remove(key)
        break




# select base notes (on website) and store in variable
option_b = columns[0].multiselect('Select base notes', [res_base[i] for i in res_base])



# get actual name from nice name using dictionary
notes_base = []

for l in option_b:
    notes_base.append([k for k, v in res_base.items() if v == l])

b_list = [item for sublist in notes_base for item in sublist]



# take actual name and loop through column names; replace 0 by corresponding value in dataframe
for m in input_base.columns:
    for n in b_list:
        if m in n:
            input_base[n] = 0.1


# just for visualisation, can get rid of it
## st.text(input_base)



# create X_new : concatenated dataframe of input top, middle and base
X_new = pd.concat([input_top, input_middle, input_base], axis = 1)

X_new = X_new.reindex(sorted(X_new.columns), axis = 1)



# just for visualisation, can get rid of it
## st.text(X_new)


# use button to calculate success
test = columns[0].button('Calculate Success')

if test:

    # load model
    model = pickle.load(open('test_model.pkl', 'rb'))

    # st.text(model.predict_proba(X_new))

    # predict if perfume is a success or not
    if model.predict(X_new) == 1 and len(X_new.loc[~(X_new==0).all(axis=1)])!=0:
        columns[0].success('Congrats! Your perfume is a SUCCESS.')
        st.balloons()

    elif len(X_new.loc[~(X_new==0).all(axis=1)])==0:

        columns[0].error('Please imput some notes!', icon="🚨")

    else:
        columns[0].markdown('# Sorry, your perfume will not be successful. Try again!')


# try recall, precision etc. cannot find unsuccessful perfume


columns[0].markdown("")
columns[0].subheader("Next let's try the randomised selection!")
columns[0].markdown('''#### For that please select the number of notes.''')

model = pickle.load(open('test_model.pkl', 'rb'))

#while model.predict(X_random) != 1:

## random perfume search

# reintroduce list of names

t1 = pd.read_csv('top_demo.csv', names = ["0"], header = None)
top1 = t1["0"].tolist()

m1 = pd.read_csv('middle_demo.csv', names = ["0"], header = None)
middle1 = m1["0"].tolist()

b1 = pd.read_csv('base_demo.csv', names = ["0"], header = None)
base1 = b1["0"].tolist()


# select number of notes
num_top = columns[0].selectbox('Select the number of top notes', [i for i in range(1,11)])
num_middle = columns[0].selectbox('Select the number of middle notes', [i for i in range(1,11)])
num_base = columns[0].selectbox('Select the number of base notes', [i for i in range(1,11)])

# get random top notes
rand_top = []
for i in range(num_top):
    rand_top.append(random.choice(top1))


# change df top to contain correct values
for r in input_top.columns:
    for s in rand_top:
        if r in s:
            input_top[s] = 0.2


# get random middle notes
rand_middle = []
for i in range(num_middle):
    rand_middle.append(random.choice(middle1))

# change df middle to contain correct values
for t in input_middle.columns:
    for u in rand_middle:
        if t in u:
            input_middle[u] = 0.7


# get random base notes
rand_base = []
for i in range(num_base):
    rand_base.append(random.choice(base1))

# change df base to contain correct values
for j in input_base.columns:
    for k in rand_base:
        if j in k:
            input_base[k] = 0.1


# create combined radnom X
X_random = pd.concat([input_top, input_middle, input_base], axis = 1)

X_random = X_random.reindex(sorted(X_random.columns), axis = 1)



test = columns[0].button('Generate random perfume and calculate success')

if test:

    # load model



    random_dirty = list(X_random)

    random_clean = []

    for i in random_dirty:
        random_clean.append(i.split('_', )[0])


    res_random = {}
    for value in random_clean:
        for key in random_dirty:
            res_random[key] = value
            random_dirty.remove(key)
            break



    t_rand = []
    m_rand = []
    b_rand = []


    for i in rand_top:
        t_rand.append(res_random[i])

    for j in rand_middle:
        m_rand.append(res_random[j])

    for k in rand_base:
        b_rand.append(res_random[k])

    # st.text(model.predict_proba(X_random))

    # predict if perfume is a success or not
    if model.predict(X_random) == 1:
        st.balloons()

        columns[0].success('Congrats! Your perfume is a SUCCESS.')

        columns[0].markdown('These are your top notes: ')
        columns[0].text(t_rand)

        columns[0].markdown('These are your middle notes: ')
        columns[0].text(m_rand)

        columns[0].markdown('These are your base notes: ')
        columns[0].text(b_rand)

    else:
        columns[0].markdown('# Sorry, your perfume will not be successful. Try again!')







#st.text(input_top)
#st.text(rand_top)
