# Instruções
### Crie o arquivo .env com as variáveis de ambiente do email permitido pela amazon

### Precisa ter o Docker instalado

### Executa os containers
```
docker compose up --build
```

### Acessar a rota ou caso não tenha modificado
```
http://localhost:8000/lesson/
```

### Fazer uma requisição json POST com o seguinte corpo
Em que a url é a lição que você deseja baixar
E o email é o email gerado pela amazon para você enviar dados para seu kindle
```
{
	"email": "your_kindle@email.com",
	"url": "https://www.inversebible.org/rl"
}
```