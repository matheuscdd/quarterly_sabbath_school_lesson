# Instruções
### Precisa ter o Docker instalado

### Executa os containers
```
docker compose up --build
```

### Acessar a rota
```
http://localhost:8000/lesson/
```

### Fazer uma requisição json POST com o seguinte corpo
Em que a url é a lição que você deseja baixar
```
{
	"url": "https://www.inversebible.org/rl"
}
```