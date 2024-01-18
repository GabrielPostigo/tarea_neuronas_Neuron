import streamlit as st
import numpy as np
import math

st.image('imagen_neurona.jpg', caption=None)

st.title('Simulador de Neurona')

st.divider() # divisores, puramente esteticos

# Mediante este slider, introducimos cuantas entradas y pesos habrá
num_entradas = st.slider('Elige el número de entradas y pesos que tendrá la neurona',1,10) 

st.divider()

st.subheader('Pesos')

valores_pesos=[] #aquí guardamos los valores que introduciremos como pesos
columnas_pesos= st.columns(num_entradas) # con esto establecemos cuantas columnas habrá

for i in range(num_entradas):
    valores_pesos.append(i) # añadimos el valor introducido

    #creamos el molde de columnas para los pesos
    with columnas_pesos[i]:
        st.markdown(f'w<sub>{i}</sub>', unsafe_allow_html=True)
        valores_pesos[i] = st.number_input(f'Entrada de w<sub>{i}</sub>',label_visibility='collapsed')
    
    
st.text(f'Peso: {valores_pesos}')

st.divider()

st.subheader('Entradas')

valores_entradas=[]
columnas_entradas = st.columns(num_entradas)

for i in range(num_entradas):
    valores_entradas.append(i)

    with columnas_entradas[i]:
        st.markdown(f'x<sub>{i}</sub>', unsafe_allow_html=True)
        valores_entradas[i] = st.number_input('Entrada de x<sub>{i}</sub>',label_visibility='collapsed')

st.text(f'Entradas: {valores_entradas}')

st.divider()

col1,col2 = st.columns(2)

with col1:
    st.subheader('Sesgo/Bias')
    sesgo = st.number_input('Introduce aqui su valor(Sesgo)')

with col2:
    st.subheader('Función a activar')
    elige_fun = st.selectbox('Elige la función a activar','Sigmoide','ReLU','Tangente hiperbólica')

st.divider()

funciones = {'Sigmoide':'sigmoid', 'ReLU':'relu', 'Tangente hiperbólica': 'tanh'}

# Creación de la clase Neuron
class Neuron:
    def __init__(self,pesos=[],b=0,funcion='sigmoid'): #metodo constructor
        self.pesos = pesos
        self.b = b
        self.funcion = funcion
    
    def run(self, entradas=[]):
        sum = np.dot(np.array(entradas),self.pesos)
        sum += self.b # aplicamos sesgo/bias

        if self.funcion == 'sigmoid':
            return self.__sigmoid(sum)
        elif self.funcion == 'relu':
            return Neuron.__relu(sum)
        elif self.funcion == 'tanh':
            return self.__tanh(sum)
        else:
            print('Función no valida, introduzca una valida(sigmoid, relu o tanh)')
    
    def cambia_peso(self, pesos):
        self.pesos = pesos

    def cambia_sesgo(self, b):
        self.b = b

    # definimos cada metodo estatico, que serán las funciones que elijan en la app
    @staticmethod
    def __sigmoid(x):
        return 1/(1 + math.e ** - x)
    
    @staticmethod
    def __relu(x):
        return 0
    
    @staticmethod
    def __tanh(x):
        return math.tanh(x)

if st.button('Submit'):
    val = Neuron(pesos=valores_pesos, b=sesgo, funcion=[elige_fun])
    st.text(f'Esta es la salida de la neurona es {val.run(entradas=valores_entradas)}')
