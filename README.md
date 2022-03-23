# Multi Page Web App using Streamlit

The code in this repository is an improvement on the code developed at the article
`Building Multi Page Web App Using Streamlit` 
(https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4)

The main improvement here implemented was to make the class `StreamlitMultiApp` as a Singleton.

More on Singletons at `Singletons: Instantiate objects only once`
(https://www.pythonforthelab.com/blog/singletons-instantiate-objects-only-once/)

## How to run one of the provided examples

At the root of the project:
```
$ export PYTHONPATH=$PWD
$ streamlit run examples/basic_02__one_app_per_file/main_app.py
```
This is necessary because when importing a file, 
Python only searches the directory (and subdirectories) that the entry-point script is running from.

My current streamlit version is 1.7.0