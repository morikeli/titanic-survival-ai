import streamlit as st


st.set_page_config(page_title='Titanic', page_icon='🚢', layout='wide')


def main():
    
    st.title(':red[Titanic survival]')
    st.caption("Do you believe you would have survived the Titanic incident? Find out today.")
    

    col = st.columns(2)

    with col[0]:
        passenger_name = st.text_input(label='Passenger name', placeholder='Enter your name')
        gender = st.selectbox(
            label='Gender', 
            options=(None, 'Male', 'Female')
        )
        sibling_spouse = st.number_input(
            label='Sibling(s)/Spouse(s)',
            help='Any siblings or spouse aboarding the Titanic?',
            min_value=0,
            max_value=10,
        )
        
    
    with col[1]:
        parent_child = st.number_input(
            label='Parent(s)/Child(ren)',
            help='Any parent(s) or child(ren) aboarding the Titanic? \
            If the child is travelling only with a nanny or a guardian, skip this step.',
            min_value=0,
            max_value=5,
        )
        ticket_class = st.selectbox(
            label='Passenger/Ticket class',
            options=(
                ('First class (upper class)'),
                ('Second class (middle class)'),
                ('Third class (lower class)'),
            )
        )
        embarking_port = st.selectbox(
            label='Port',
            options=('Cherbourg', 'Queenstown', 'Southampton'),
            help='Select the port you are embarking the Titanic'
        )
    

    submit_btn = st.button(label='Submit', type='primary', use_container_width=True)

    if submit_btn:
        st.toast('Form submitted successfully! Wait for response.', icon='✅')
        with st.spinner('Analyzing input data'):
            pass





if __name__ == '__main__':
    main()