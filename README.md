# AI Chat Application with AWS Bedrock

Modern bir chat uygulaması - AWS Bedrock AI servisleri ile entegre edilmiş React frontend ve Flask backend.

## 🚀 Features

- 🤖 **AWS Bedrock Integration** - Claude AI modeli ile sohbet
- 💬 **Modern Chat UI** - React ile geliştirilmiş arayüz
- ⚡ **Quick Questions** - Hızlı soru butonları
- 📱 **Responsive Design** - Mobil ve masaüstü uyumlu
- 🐳 **Docker Support** - Tek container deployment
- 🔒 **AWS Credentials** - Güvenli kimlik doğrulama

## 🛠️ Tech Stack

- **Frontend:** React, CSS3, HTML5
- **Backend:** Python Flask, AWS Bedrock
- **Container:** Docker, Nginx, Supervisor
- **AI Model:** Anthropic Claude Instant v1

## 📦 Installation

### Docker ile (Önerilen)

```bash
# Repository'yi klonla
git clone https://github.com/Letanom/ai-chatbot-awsbedrock.git
cd ai-chatbot-awsbedrock

# Docker ile çalıştır
docker-compose up --build
```

### Manuel Kurulum

```bash
# Backend
cd backend
pip install -r requirements.txt
python backend_api.py

# Frontend (yeni terminal)
cd frontend
npm install
npm start
```

## 🐳 Docker Hub

### Pull & Run
```bash
docker run -d -p 80:80 kevinozsimsek/aichat-bedrock:latest
```

### AWS Credentials ile
```bash
docker run -d -p 80:80 \
  -v ~/.aws:/root/.aws:ro \
  kevinozsimsek/aichat-bedrock:latest
```

## 🌐 Usage

1. **Tarayıcıda aç:** http://localhost:3000 (dev) / http://localhost (prod)
2. **Hızlı sorular:** Üstteki butonlardan seç
3. **Mesaj yaz:** Alt kısımdaki input'a yaz
4. **AI cevabı al:** AWS Bedrock'tan anında yanıt

## 📁 Project Structure

```
ai-chatbot-awsbedrock/
├── backend/           # Flask API + AWS Bedrock
│   ├── aws_bedrock.py
│   ├── backend_api.py
│   └── requirements.txt
├── frontend/          # React Chat UI
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   └── package.json
├── docker-compose.yml # Development
├── Dockerfile         # Single container
└── README.md
```

## ⚙️ Configuration

### AWS Credentials
```bash
# AWS CLI ile
aws configure

# Veya environment variables
export AWS_ACCESS_KEY_ID=your-key
export AWS_SECRET_ACCESS_KEY=your-secret
export AWS_DEFAULT_REGION=us-east-1
```

### Environment Variables
```bash
FLASK_ENV=production
AWS_DEFAULT_REGION=us-east-1
```

## 🔧 Development

### Backend API
- **Port:** 5000
- **Endpoint:** `/api/chat`
- **Method:** POST
- **Body:** `{"prompt": "your message"}`

### Frontend
- **Port:** 3000 (dev) / 80 (prod)
- **Framework:** React
- **Styling:** CSS3

## 📊 Monitoring

```bash
# Container logları
docker logs <container-id>

# Backend logları
docker exec <container-id> tail -f /var/log/supervisor/flask.out.log

# Nginx logları
docker exec <container-id> tail -f /var/log/supervisor/nginx.out.log
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/Letanom/ai-chatbot-awsbedrock/issues)
- **Docker Hub:** [kevinozsimsek/aichat-bedrock](https://hub.docker.com/r/kevinozsimsek/aichat-bedrock)

---

⭐ **Star this repository if you find it helpful!** 
