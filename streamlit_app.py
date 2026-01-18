import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Dashboard Mejor CDT", layout="wide")

# Estilos globales
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    h1, h2, h3 { color: #111BFF !important; font-family: 'Roboto', sans-serif; }
    
    .top-card {
        background-color: white; 
        padding: 15px; 
        border-radius: 12px;
        border: 1px solid #EDEEFF; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        height: 140px; 
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .leads-table { width: 100%; border-collapse: collapse; font-family: sans-serif; color: #000000; }
    .leads-table td { padding: 4px 0; border-bottom: 1px solid #F0F0F0; font-size: 13px; }
    .val { text-align: right; font-weight: bold; }
    .change { font-size: 10px; font-weight: bold; margin-left: 5px; }
    .down { color: #FF4B4B; }
    .up { color: #00CA67; }
    </style>
    """, unsafe_allow_html=True)

# 2. FUNCIÓN GRÁFICO CIRCULAR
def progress_circle(nombre, porcentaje, monto_actual, meta, color="#111BFF"):
    display_porcentaje = min(porcentaje, 100)
    circunferencia = 282.7
    offset = circunferencia - (circunferencia * display_porcentaje / 100)
    html_code = f"""
    <div style="font-family: sans-serif; text-align: center; background: white; border-radius: 15px; border: 1px solid #EDEEFF; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 410px; display: flex; flex-direction: column; justify-content: space-between; padding: 20px; box-sizing: border-box;">
        <div>
            <div style="color: {color}; font-weight: 900; font-size: 18px;">${monto_actual:,.0f}</div>
            <div style="color: #888; font-size: 10px; text-transform: uppercase;">Logrado Hoy</div>
        </div>
        <div style="color: {color}; font-weight: 800; font-size: 13px; margin: 10px 0;">PROGRESO {nombre}</div>
        <div style="position: relative; width: 160px; height: 160px; margin: 0 auto;">
            <svg viewBox="0 0 100 100" style="transform: rotate(-90deg); width: 100%; height: 100%;">
                <circle cx="50" cy="50" r="45" fill="none" stroke="#EDEEFF" stroke-width="8" />
                <circle cx="50" cy="50" r="45" fill="none" stroke="{color}" stroke-width="8" 
                        stroke-dasharray="282.7" stroke-dashoffset="{offset}" style="transition: 1.5s;"/>
                <circle cx="50" cy="50" r="45" fill="none" stroke="white" stroke-width="9" stroke-dasharray="1 3.71" />
            </svg>
            <div style="position: absolute; top:0; left:0; width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                <span style="font-size: 26px; font-weight: 900; color: {color};">{porcentaje}%</span>
                <span style="font-size: 10px; color: #888;">LOGRADO</span>
            </div>
        </div>
        <div style="background: #F8F9FF; padding: 10px; border-radius: 8px; font-size: 11px; font-weight: bold; color: #555; border: 1px solid #DDD;">
            Meta: ${meta:,.0f}
        </div>
    </div>
    """
    return st.components.v1.html(html_code, height=450)

# 3. DATOS
datos_equipos = {
    "SALES": {"actual": 2293996261, "meta": 1222000000, "color": "#111BFF"},
    "OPSCOM": {"actual": 30559520, "meta": 78000000, "color": "#6133FF"},
    "TUBO": {"actual": 20000000, "meta": 200000000, "color": "#FF6B00"},
    "APP": {"actual": 31400000, "meta": 67000000, "color": "#00A38B"}
}

# 4. HEADER
st.markdown("<h1 style='text-align: center;'>🚀 DASHBOARD - MEJOR CDT</h1>", unsafe_allow_html=True)

# FILA SUPERIOR
c1, c2, c3 = st.columns([1.2, 2.5, 1])
with c1:
    st.markdown("""
        <div class="top-card">
            <table class="leads-table">
                <tr><td>Returning</td><td class="val">73 <span class="change up">▲ 2.5%</span></td></tr>
                <tr><td>New</td><td class="val">56 <span class="change down">▼ -52.5%</span></td></tr>
                <tr style="border:none;"><td style="font-weight:bold;">Total</td><td class="val" style="color:#111BFF; font-size:16px;">173 <span class="change down">▼ -26.7%</span></td></tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

with c2:
    monto_global = 79054602968
    st.html(f"""
        <div class="top-card" style="text-align:center;">
            <div style="color:#111BFF; font-weight:800; font-size:11px; letter-spacing:1px; margin-bottom:8px;">ROAD TO 100K</div>
            <div style="font-size:26px; font-weight:900; color:#111BFF; margin-bottom:8px;">${monto_global:,.0f}</div>
            <div style="background:#EDEEFF; border-radius:50px; height:12px; overflow:hidden; width:90%; margin: 0 auto;">
                <div style="background:linear-gradient(90deg, #111BFF, #00CA67); width:79%; height:100%;"></div>
            </div>
            <div style="color:#00CA67; font-size:10px; font-weight:bold; margin-top:8px;">79.05% de la meta global</div>
        </div>
    """)

with c3:
    st.markdown("""
        <div class="top-card" style="text-align:center;">
            <div style="color:#888; font-size:11px; font-weight:bold; margin-bottom:5px;">Cantidad CDTs</div>
            <div style="font-size:32px; font-weight:900; color:#333;">173</div>
            <div style="color:#FF4B4B; font-size:12px; font-weight:bold;">▼ -26.7%</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# 5. FILA DE EQUIPOS (CORREGIDO: 5 columnas iguales)
cols_equipo = st.columns(5) 

for i, (nombre, info) in enumerate(datos_equipos.items()):
    porcentaje = round((info["actual"] / info["meta"]) * 100, 2)
    with cols_equipo[i]:
        progress_circle(nombre, porcentaje, info["actual"], info["meta"], info["color"])

# TERMÓMETRO (Columna 5, mismo ancho y alto)
with cols_equipo[4]:
    monto_hoy = sum(e["actual"] for e in datos_equipos.values())
    porcentaje_diario = 84
    st.html(f"""
        <div style="font-family: sans-serif; background: white; padding: 20px; border-radius: 15px; border: 1px solid #EDEEFF; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 410px; display: flex; flex-direction: column; justify-content: space-between; align-items: center; box-sizing: border-box; text-align: center;">
            <div>
                <div style="color: #111BFF; font-weight: 900; font-size: 18px;">${monto_hoy:,.0f}</div>
                <div style="color: #888; font-size: 10px; text-transform: uppercase;">Acumulado Hoy</div>
            </div>
            
            <div style="color: #111BFF; font-weight: 800; font-size: 13px; margin: 5px 0;">META DIARIA</div>

            <div style="height: 160px; width: 30px; background: #EDEEFF; border-radius: 20px; position: relative; overflow: hidden; display: flex; flex-direction: column-reverse; border: 1px solid #D0D5FF;">
                <div style="height: {porcentaje_diario}%; background: linear-gradient(0deg, #111BFF, #00CA67); width: 100%;"></div>
            </div>
            
            <div style="width: 65px; height: 65px; background: #111BFF; border-radius: 50%; border: 4px solid white; color: white; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 16px; box-shadow: 0 6px 12px rgba(17,27,255,0.3); margin-top: -35px; z-index: 10;">
                {porcentaje_diario}%
            </div>
            
            <div style="background: #F8F9FF; padding: 10px; border-radius: 8px; font-size: 11px; font-weight: bold; color: #555; border: 1px solid #DDD; width: 100%; box-sizing: border-box;">
                Meta: $2,830M
            </div>
        </div>
    """)

st.divider()

# 6. GRÁFICOS INFERIORES
df_mock = pd.DataFrame({"Banco": ["KOA", "Coltef.", "Credif.", "Finan.", "Bancam."], "Val": [67, 21, 5, 4, 1]})
df_bar = pd.DataFrame({"Ene": ["13", "14", "15", "16", "17"], "Monto": [2100, 1700, 900, 1650, 20]})

inf_c1, inf_c2, inf_c3 = st.columns([1, 1.5, 1])

def update_fig_style(fig, title, is_pie=False):
    fig.update_layout(
        title={'text': title, 'font': {'color': '#111BFF', 'size': 18}, 'x': 0.5},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=20, l=10, r=10),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    if is_pie:
        fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

with inf_c1:
    fig1 = px.pie(df_mock, values='Val', names='Banco', hole=0.5, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(update_fig_style(fig1, "Cantidad de CDTs", True), use_container_width=True)

with inf_c2:
    fig3 = px.bar(df_bar, x='Ene', y='Monto', color_discrete_sequence=['#111BFF'], text_auto='.2s')
    fig3.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(update_fig_style(fig3, "Rango de plazos por monto"), use_container_width=True)

with inf_c3:
    fig2 = px.pie(df_mock, values='Val', names='Banco', hole=0.5, color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(update_fig_style(fig2, "Monto por Banco", True), use_container_width=True)