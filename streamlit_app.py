import streamlit as st
import math

def prime_factorization(n):
    factors = []
    
    # 2で割り切れる間は2で割り続ける
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # 3以上の奇数で割っていく
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # 最後に残った数が1より大きければ、それも素因数
    if n > 1:
        factors.append(n)
    
    return factors

st.title('素因数分解プログラム')

number = st.number_input('正の整数を入力してください:', min_value=1, step=1)

if st.button('素因数分解'):
    if number > 1:
        factors = prime_factorization(int(number))
        
        st.write(f'{int(number)}の素因数分解結果:')
        
        # 素因数とその指数を表示
        factor_counts = {}
        for factor in factors:
            if factor in factor_counts:
                factor_counts[factor] += 1
            else:
                factor_counts[factor] = 1
        
        result = ' × '.join([f'{factor}^{count}' if count > 1 else str(factor) for factor, count in factor_counts.items()])
        st.latex(result)
        
        # 展開した形も表示
        expanded = ' × '.join(map(str, factors))
        st.write('展開形:')
        st.latex(expanded)
    else:
        st.write('1より大きい整数を入力してください。')