# 🌟 Sistema de Agendamento de Eventos com Microsserviços e Mensageria (RabbitMQ)

Este projeto consiste em dois microsserviços desenvolvidos em Python: um para gerenciamento de eventos e inscrições (event_service), e outro para envio de e-mails reais de confirmação (email_service). A comunicação entre eles é feita via RabbitMQ.

---

## 🧩 Estrutura do Projeto
```text
AgendamentoEventos/
│
├── email_service/
│   ├── consumer.py
│   ├── email_sender.py
│   └── .env.example
│
├── event_service/
│   ├── app.py
│   ├── db.py
│   ├── events.db
│   ├── message_sender.py
│   ├── models.py
│   ├── repository.py
│
├── .gitignore
├── Atividade 4.pdf
├── README.md
├── requirements.txt
```

---

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** — API REST para gerenciamento de eventos
- **SQLite** — banco de dados leve para armazenar eventos e inscrições
- **RabbitMQ + pika** — mensageria entre os microsserviços
- **smtplib + email.message** — envio de e-mail real via SMTP
- **python-dotenv** — leitura de variáveis de ambiente para configuração de e-mail

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/IsabelleRancan/AgendamentoEventos.git
cd AgendamentoEventos
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente para envio de e-mail
- Renomeie o arquivo .env.example para .env dentro da pasta email_service/
- Preencha com suas credenciais de e-mail (usar senha de app para Gmail)

```text
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

## ▶️ Execução dos Microsserviços

### 1. Inicie o serviço de eventos
Em um terminal:
``` bash
cd event_service
python app.py
```
API rodando em: http://localhost:5000

### 2. Inicie o serviço de envio de e-mails
Em outro terminal:
``` bash
cd email_service
python consumer.py
```

---

## 🧪 Testando a Aplicação com Postman

### 1. Criar um evento
Método: POST
URL: http://localhost:5000/events
Body (JSON):

``` json 
{
  "title": "Workshop Python",
  "description": "Aprenda Flask e RabbitMQ!",
  "date": "2025-07-05",
  "max_participants": 10
}
```

### 2. Listar todos os eventos
Método: GET
URL: http://localhost:5000/events

### 3. Listar eventos futuros
Método: GET
URL: http://localhost:5000/events/upcoming

### 4. Inscrever participante em um evento
Método: POST
URL: http://localhost:5000/events/<event_id>/subscribe
(Substitua <event_id> pelo ID do evento que deseja inscrever)
Body (JSON):

``` json 
{
  "email": "participante@email.com"
}
```
| Após a inscrição, o participante receberá um e-mail real de confirmação.

---

## 📝 Endpoints resumidos

| Método | Endpoint                       | Descrição                       |
| ------ | ------------------------------ | ------------------------------- |
| GET    | `/events`                      | Retorna todos os eventos        |
| GET    | `/events/upcoming`             | Retorna eventos futuros         |
| POST   | `/events`                      | Cria um novo evento             |
| POST   | `/events/<event_id>/subscribe` | Inscreve participante em evento |

---

## 🛡️ Segurança
- Informações sensíveis como senhas não estão no código
- .env está no .gitignore
- .env.example mostra como configurar variáveis sem risco
- Senha de app Gmail usada para envio seguro de e-mails

---

## 🔍 Informações adicionais

- Projeto desenvolvido por Isabelle Firmino Rancan — Estudante de Análise e Desenvolvimento de Sistemas – IFMS
- Comunicação entre microsserviços feita via RabbitMQ, garantindo desacoplamento e escalabilidade
- Envio de e-mails com confirmação personalizada contendo detalhes do evento
- [Vídeo com exemplo de uso](https://drive.google.com/file/d/1496gNBDO5gTi0tto56tnesIvOCCazW3L/view?usp=sharing)