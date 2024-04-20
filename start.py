import os

if not os.path.exists('./chiori'):
    os.system("git clone https://code.openxlab.org.cn/fisher_lee/chiori.git")
os.system('streamlit run app.py --server.address=0.0.0.0 --server.port 7860')