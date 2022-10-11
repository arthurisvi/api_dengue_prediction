# Auxílio ao diagnóstico de Dengue
API em Flask para auxílio de predição de pacientes com Dengue.

Utiliza-se um modelo de machine learning em que foi aplicada a técnica de Decision Three, o qual está carregado no repositório no arquivo 'model_dt.save'.

### Exemplo de JSON de entrada
```json
{
	"cs_sexo": 1,
	"febre": 1,
	"mialgia": 1,
	"cefaleia": 2,
	"exantema": 2,
	"vomito": 1,
	"nausea": 1,
	"dor_costas": 2,
	"artralgia": 2,
	"dor_retro": 1,
	"leucopenia": 1,
	"petequia_n": 1
}
```

### Exemplo JSON de saída
```json
{
	"exit": 1,
	"positive_probability": 71.42,
	"negative_probability": 28.57
}
```

### Dicionário

Sintomas clínicos 
```
1- Sim
2- Não
```

Gênero 

```
0- Feminino
1- Masculino
```

Saída
```
"Exit"
0- Não é dengue
1- Dengue
```
```
positive_probability: Porcentagem da probabilidade do paciente estar com Dengue.
negative_probability: Porcentagem da probabilidade do paciente não estar com Dengue. 
```
