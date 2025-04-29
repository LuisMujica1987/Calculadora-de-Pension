import streamlit as st

st.set_page_config(page_title="Calculadora Ley 73 + Modalidad 40", layout="centered")

st.title("Calculadora de Pensión Ley 73 con Modalidad 40")
st.markdown("Asesor: **Luis Mujica**  \nWhatsApp: [8117618084](https://wa.me/528117618084)  \nCorreo: jose.rangel@suramexico.com")

edad = st.number_input("Edad actual", min_value=60, max_value=80, value=65)
semanas = st.number_input("Semanas cotizadas", min_value=500, max_value=3000, value=1300)
sbc_original = st.number_input("SBC antes de M40", min_value=100.0, max_value=2500.0, value=500.0)
sbc_m40 = st.number_input("SBC en Modalidad 40", min_value=100.0, max_value=2714.25, value=2500.0)
anios_m40 = st.number_input("Años en Modalidad 40", min_value=0, max_value=10, value=5)

def calcular_pension(edad, sbc_original, semanas, sbc_m40, años_m40):
    UMA = 108.57
    if edad == 60:
        porcentaje = 75
    elif edad == 61:
        porcentaje = 80
    elif edad == 62:
        porcentaje = 85
    elif edad == 63:
        porcentaje = 90
    elif edad == 64:
        porcentaje = 95
    else:
        porcentaje = 100

    total_anios = (semanas // 52) + años_m40

    bono = 0
    if 10 <= total_anios <= 14:
        bono = 5
    elif total_anios == 15:
        bono = 6.5
    elif total_anios == 16:
        bono = 8
    elif total_anios == 17:
        bono = 9.5
    elif total_anios == 18:
        bono = 11
    elif total_anios == 19:
        bono = 12.5
    elif total_anios >= 20:
        bono = 14 + ((total_anios - 20) * 2)

    sbc_promedio = ((sbc_original * (semanas // 52)) + (sbc_m40 * años_m40)) / total_anios
    pension = ((sbc_promedio * porcentaje) / 100) + (UMA * bono)
    inversion_m40 = sbc_m40 * 0.1025 * 12 * años_m40

    return round(pension, 2), round(inversion_m40, 2)

if st.button("Calcular pensión"):
    pension, inversion = calcular_pension(edad, sbc_original, semanas, sbc_m40, anios_m40)
    st.success(f"Pensión estimada: ${pension} MXN/mes")
    st.info(f"Total a invertir en M40: ${inversion} MXN")
    st.markdown("[Ir a WhatsApp](https://wa.me/528117618084)")
