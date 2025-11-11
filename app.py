from flask import Flask, render_template, request
import json
import resend

resend.api_key = "re_DkzT2CY3_7Na9JerXKXEMt4MJvJdrR9kt"

with open('Contatos.json', 'r', encoding='utf-8') as arquivo:
    contatos=json.load(arquivo)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']

        contato = {}
        contato['nome'] = nome
        contato['email'] = email
        contato['mensagem'] = mensagem

        contatos.append(contato)

        with open('contatos.json', 'w', encoding='utf-8') as arquivo:
            json.dump(contatos, arquivo, indent=4, ensure_ascii=False)

        email_html = f"""
        <h1>Novo contato de {nome}!</h1><br>
        <p>Email: {email}</p><br>
        <p>{mensagem}</p>
        """
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "luanaalencarcarvalhoalves@gmail.com",
        "subject": "Contato para adoção de pets",
        "html": email_html
        })


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)