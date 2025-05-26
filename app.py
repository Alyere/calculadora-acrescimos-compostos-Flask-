from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def formatar_br(valor):
    """
    Formata um valor numérico para o padrão monetário brasileiro (R$ X.XXX,XX).
    """
    return f"R$ {valor:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")

def calcular_acrescimos_compostos_web(valor_base):
    """
    Calcula os acréscimos de 27% e 30% sobre um valor base,
    retornando os resultados formatados para exibição web.
    """
    valor_apos_27 = valor_base * 1.27
    acrescimo_27 = valor_apos_27 - valor_base

    valor_apos_30 = valor_apos_27 * 1.30
    acrescimo_30 = valor_apos_30 - valor_apos_27

    total_acrescimos = acrescimo_27 + acrescimo_30

    return {
        "valor_base": formatar_br(valor_base),
        "acrescimo_27": formatar_br(acrescimo_27),
        "valor_apos_27": formatar_br(valor_apos_27),
        "acrescimo_30": formatar_br(acrescimo_30),
        "valor_apos_30": formatar_br(valor_apos_30),
        "total_acrescimos": formatar_br(total_acrescimos),
        "valor_final": formatar_br(valor_apos_30),
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = None
    if request.method == 'POST':
        try:
            valor_base_input = float(request.form['valor_base'])
            resultados = calcular_acrescimos_compostos_web(valor_base_input)
        except ValueError:
            resultados = {"error": "Por favor, digite um valor numérico válido."}
    return render_template('index.html', resultados=resultados)

