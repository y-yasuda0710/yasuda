import streamlit as st
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

st.title("素数判定プログラム")

number = st.number_input("正の整数を入力してください:", min_value=1, step=1)

if st.button("判定"):
    if number.is_integer():
        number = int(number)
        if is_prime(number):
            st.success(f"{number} は素数です！")
        else:
            st.error(f"{number} は素数ではありません。")
    else:
        st.warning("整数を入力してください。")

st.write("---")
st.write("このプログラムは2から入力された数までの素数も表示します。")

if st.button("素数リストを表示"):
    primes = [num for num in range(2, int(number) + 1) if is_prime(num)]
    st.write(f"2から{int(number)}までの素数:")
    st.write(primes)

