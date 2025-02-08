import streamlit as st

if "counter_1" not in st.session_state:
    st.session_state.counter_1 = 0

def funct_MegaIncrease_1(increment = 1):
    st.session_state.counter_1 += increment
    st.session_state.counter_1 = st.session_state.counter_1
    
    if st.session_state.counter_1 == 50 or st.session_state.counter_1 == 100:
        st.balloons()  # Display balloons when the counter reaches 50 or 100
    st.session_state.counter_1 = st.session_state.counter_1

if "counter_2" not in st.session_state:
    st.session_state.counter_2 = 0

def funct_MegaIncrease_2(increment = 1):
    st.session_state.counter_2 += increment
    st.session_state.counter_2 = st.session_state.counter_2
    
    if st.session_state.counter_2 == 50 or st.session_state.counter_2 == 100:
        st.balloons()  # Display balloons when the counter reaches 50 or 100
    st.session_state.counter_2 = st.session_state.counter_2

if "counter_3" not in st.session_state:
    st.session_state.counter_3 = 0

def funct_MegaIncrease_3(increment = 1):
    st.session_state.counter_3 += increment
    st.session_state.counter_3 = st.session_state.counter_3
    
    if st.session_state.counter_3 == 50 or st.session_state.counter_3 == 100:
        st.balloons()  # Display balloons when the counter reaches 50 or 100
    st.session_state.counter_3 = st.session_state.counter_3

if "counter_4" not in st.session_state:
    st.session_state.counter_4 = 0

def funct_MegaIncrease_4(increment = 1):
    st.session_state.counter_4 += increment
    st.session_state.counter_4 = st.session_state.counter_4

    if st.session_state.counter_4 == 50 or st.session_state.counter_4 == 100:
        st.balloons()  # Display balloons when the counter reaches 50 or 100
    st.session_state.counter_4 = st.session_state.counter_4


tally_tab, result_tab = st.tabs(["Tally","Result"])

with tally_tab:
    tally_col1, tally_col2 = st.columns(2)   
    with tally_col1:
        
        #THIKE
        with st.container(border=1):
            st.session_state.title = st.write("THIKE")
            col1, col2 = st.columns([3,1])
            col3, col4 = st.columns(2) 

            with col2:
                if st.button("+1",use_container_width=True, key = "+1_THIKE"):
                    funct_MegaIncrease_1(1)
                if st.button("-1",use_container_width=True, key = "-1_THIKE"):
                    funct_MegaIncrease_1(-1)

            with col3:
                if st.button("+3",use_container_width=True, key = "+3_THIKE"):
                    funct_MegaIncrease_1(3)

            with col4:
                if st.button("+5",use_container_width=True, key = "+5_THIKE"):
                    funct_MegaIncrease_1(5)
            
            if st.button("-5",use_container_width=True, key = "-5_THIKE"):
                        funct_MegaIncrease_1(-5)

            with col1:
                with st.container(border=1):
                    st.header(f"{st.session_state.counter_1}")



        #OK
        with st.container(border=1):
            st.session_state.title = st.write("OK")
            col1, col2 = st.columns([3,1])
            col3, col4 = st.columns(2) 

            with col2:
                if st.button("+1",use_container_width=True, key = "+1_OK"):
                    funct_MegaIncrease_3(1)
                if st.button("-1",use_container_width=True, key = "-1_OK"):
                    funct_MegaIncrease_3(-1)

            with col3:
                if st.button("+3",use_container_width=True, key = "+3_OK"):
                    funct_MegaIncrease_3(3)

            with col4:
                if st.button("+5",use_container_width=True, key = "+5_OK"):
                    funct_MegaIncrease_3(5)

            
            if st.button("-5",use_container_width=True, key = "-5_OK"):
                funct_MegaIncrease_3(-5)
            
            with col1:
                with st.container(border=1):
                    st.header(f"{st.session_state.counter_3}")

    
    with tally_col2:
        #HAINA
        with st.container(border=1):
            st.session_state.title = st.write("HAINA")
            col1, col2 = st.columns([3,1])
            col3, col4 = st.columns(2) 

            with col2:
                if st.button("+1",use_container_width=True, key = "+1_HAINA"):
                    funct_MegaIncrease_2(1)
                if st.button("-1",use_container_width=True, key = "-1_HAINA"):
                    funct_MegaIncrease_2(-1)

            with col3:
                if st.button("+3",use_container_width=True, key = "+3_HAINA"):
                    funct_MegaIncrease_2(3)

            with col4:
                if st.button("+5",use_container_width=True, key = "+5_HAINA"):
                    funct_MegaIncrease_2(5)
            
            if st.button("-5",use_container_width=True, key = "-5_HAINA"):
                funct_MegaIncrease_2(-5)

            with col1:
                with st.container(border=1):
                    st.header(f"{st.session_state.counter_2}")



        #O-B-OSLY
        with st.container(border=1):
            st.session_state.title = st.write("O-B-OSLY")
            col1, col2 = st.columns([3,1])
            col3, col4 = st.columns(2) 

            with col2:
                if st.button("+1",use_container_width=True, key = "+1_O-B-OSLY"):
                    funct_MegaIncrease_4(1)
                if st.button("-1",use_container_width=True, key = "-1_O-B-OSLY"):
                    funct_MegaIncrease_4(-1)

            with col3:
                if st.button("+3",use_container_width=True, key = "+3_O-B-OSLY"):
                    funct_MegaIncrease_4(3)

            with col4:
                if st.button("+5",use_container_width=True, key = "+5_O-B-OSLY"):
                    funct_MegaIncrease_4(5)
            
            if st.button("-5",use_container_width=True, key = "-5_O-B-OSLY"):
                        funct_MegaIncrease_4(-5)

            with col1:
                with st.container(border=1):
                    st.header(f"{st.session_state.counter_4}")

with result_tab:
    # Create a dictionary of titles and their counter values
    counters = {
        "THIKE": st.session_state.counter_1,
        "HAINA": st.session_state.counter_2,
        "OK": st.session_state.counter_3,
        "O-B-OSLY": st.session_state.counter_4
    }

    # Sort the dictionary by values (counter values) in descending order
    sorted_counters = dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))

    # Display sorted counters in the result tab
    st.title("Counter Values in Descending Order:")
    for title, counter_value in sorted_counters.items():
        st.header(f"{title}: {counter_value}")








