import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth

with open('.streamlit/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# ---- Creating a login widget ---- #
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()
# ---- Creating a login widget ---- #

# ---- Authenticating users ---- #
if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    with open('.streamlit/config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
# ---- Authenticating users ---- #

# ---- Creating a reset password widget ---- #
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
        with open('.streamlit/config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)
# ---- Creating a reset password widget ---- #

# ---- Creating a new user registration widget ---- #
try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
    if email_of_registered_user:
        st.success('User registered successfully')
    with open('.streamlit/config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)
# ---- Creating a new user registration widget ---- #

# ---- Creating a forgot password widget ---- #
try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        # The developer should securely transfer the new password to the user.
    elif username_of_forgotten_password == False:
        st.error('Username not found')
    with open('.streamlit/config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)
# ---- Creating a forgot password widget ---- #

# ---- Creating a forgot username widget ---- #
try:
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
    if username_of_forgotten_username:
        st.success('Username to be sent securely')
        # The developer should securely transfer the username to the user.
        with open('.streamlit/config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
    elif username_of_forgotten_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)
# ---- Creating a forgot username widget ---- #

# ---- Creating an update user details widget ---- #
if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
    with open('.streamlit/config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
# ---- Creating an update user details widget ---- #
