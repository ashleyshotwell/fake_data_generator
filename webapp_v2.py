# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# Data Pkgs
import pandas as pd
from faker import Faker

# Utils
import base64
import time
import os

timestr = time.strftime("%Y%m%d-%H%M%S")

# Fxn to Download
def make_downloadable_df(data):
    """
    Save the DataFrame as a CSV file in the current project directory and display a success message.
    
    Args:
        data (pd.DataFrame): The DataFrame to be saved.
    """
    csvfile = data.to_csv(index=False)
    new_filename = f"fake_dataset_{timestr}.csv"
    file_path = os.path.join(os.getcwd(), new_filename)
    with open(file_path, "w") as f:
        f.write(csvfile)
    st.success(f"File saved to {file_path}")

# Fxn to Download Into A Format
def make_downloadable_df_format(data, format_type="csv"):
    """
    Save the DataFrame in the specified format (CSV or JSON) in the current project directory,
    display the JSON data on the webpage if the format is JSON, and provide a download link.
    
    Args:
        data (pd.DataFrame): The DataFrame to be saved.
        format_type (str): The format to save the data in ("csv" or "json").
    """
    if format_type == "csv":
        datafile = data.to_csv(index=False)
    elif format_type == "json":
        datafile = data.to_json()
        st.json(datafile)  # Display JSON data on the webpage

    new_filename = f"fake_dataset_{timestr}.{format_type}"
    file_path = os.path.join(os.getcwd(), new_filename)
    with open(file_path, "w") as f:
        f.write(datafile)
    st.success(f"File saved to {file_path}")

    # Provide a download link
    b64 = base64.b64encode(datafile.encode()).decode()  # B64 encoding
    href = f'<a href="data:file/{format_type};base64,{b64}" download="{new_filename}">Click Here to Download</a>'
    st.markdown(href, unsafe_allow_html=True)

# Generate A Simple Profile
def generate_profile(number, random_seed=200):
    """
    Generate a DataFrame with simple profiles.
    
    Args:
        number (int): The number of profiles to generate.
        random_seed (int): The random seed for reproducibility.
    
    Returns:
        pd.DataFrame: The generated profiles.
    """
    fake = Faker()
    Faker.seed(random_seed)
    data = [fake.simple_profile() for i in range(number)]
    df = pd.DataFrame(data)
    return df

# Generate A Customized Profile Per Locality
def generate_locale_profile(number, locale, random_seed=200):
    """
    Generate a DataFrame with customized profiles based on the specified locale.
    
    Args:
        number (int): The number of profiles to generate.
        locale (str): The locale for the profiles.
        random_seed (int): The random seed for reproducibility.
    
    Returns:
        pd.DataFrame: The generated profiles.
    """
    locale_fake = Faker(locale)
    Faker.seed(random_seed)
    data = [locale_fake.simple_profile() for i in range(int(number))]
    df = pd.DataFrame(data)
    return df

custom_title = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Ashley's FAKE DATA GENERATOR</h2>
    </div>
"""

def main():
    # st.title("Fake Data Generator")
    stc.html(custom_title)

    menu = ["Home", "Customize", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        number_to_gen = st.sidebar.number_input("Number", 10, 5000)
        localized_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT",
                               "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE",
                               "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE",
                               "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN",
                               "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la",
                               "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL",
                               "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH",
                               "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
        locale = st.sidebar.multiselect("Select Locale", localized_providers, default="en_US")
        dataformat = st.sidebar.selectbox("Save Data As", ["csv", "json"])

        df = generate_locale_profile(number_to_gen, locale)
        st.dataframe(df)
        with st.expander("📩: Download"):
            make_downloadable_df_format(df, dataformat)

    elif choice == "Customize":
        st.subheader("Customize Your Fields")

        # Locale Providers For Faker Class
        localized_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT",
                               "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE",
                               "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE",
                               "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN",
                               "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la",
                               "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL",
                               "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH",
                               "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
        
        locale = st.sidebar.multiselect("Select Locale", localized_providers, default="en_US")

        profile_options_list = ['username', 'name', 'sex', 'address', 'mail', 'birthdate', 'job', 'company', 'ssn',
                                'residence', 'current_location', 'blood_group', 'website']
        
        default_fields = ['username', 'ssn']
        profile_fields = st.sidebar.multiselect("Fields", profile_options_list, default=default_fields)

        number_to_gen = st.sidebar.number_input("Number", 10, 10000)
        dataformat = st.sidebar.selectbox("Save Data As", ["csv", "json"])

        # Initialize Faker Class
        custom_fake = Faker(locale)
        data = [custom_fake.profile(fields=profile_fields) for i in range(int(number_to_gen))]
        df = pd.DataFrame(data)

        # View As Dataframe
        st.dataframe(df)

        # View as JSON
        with st.expander("🔍: View JSON "):
            st.json(data)

        with st.expander("📩: Download"):
            make_downloadable_df_format(df, dataformat)

    else:
        st.subheader("About")
        st.success("Built with Streamlit")
        st.info("Virtual Office Point")
        st.text("By Steve Karanja")

if __name__ == '__main__':
    main()