import streamlit as st

def on_reload():
    st.sidebar.image('AEGIS_logo.png', width=240)
    st.sidebar.title('AIMS Test UI-01')
    st.sidebar.header('ログイン')
    st.sidebar.text_input('アカウント')
    st.sidebar.text_input('パスワード')
    st.sidebar.button('ログイン')
    st.sidebar.header('設定')
    st.sidebar.text('なにかしらの設定項目')
 
    st.title('A Innovative Matching System')
    st.header('Chat room')
    st.text('何でも聞いてね！')

    st.text_area('質問')
    req = st.button('送信')

    if req:
        st.text('メッセージ送信')


    return


def main():
    on_reload()
    return

if __name__ == '__main__':
    main()