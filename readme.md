# Instruções
### Crie um email com senha de aplicativo
O gmail permite criar desde que adicione as duas etapas

### Na Amazon, habilite um email para envio do Kindle
[Para Mais Informações](https://www.amazon.com.br/gp/help/customer/display.html?nodeId=GX9XLEVV8G4DB28H)

### Crie o arquivo .env com as variáveis de ambiente do email permitido pela amazon

### Precisa ter o Docker instalado

### Executa os containers
```
docker compose up --build
```

### Acessar a rota ou caso não tenha modificado a porta
```
http://localhost:8000/lesson
```

### Fazer uma requisição json POST com o seguinte corpo
O campo url é o endereço da listagem trimestral da lição que deseja baixar
O campo email é aquele gerado automaticamente pela amazon para você enviar dados para seu kindle
```
{
	"email": "your_kindle@email.com",
	"url": "https://www.inversebible.org/rl"
}
```