# Animal Trace

O sistema de Gerenciamento de Localização de Animais na Fazenda tem como objetivo principal auxiliar os fazendeiros no monitoramento e controle da movimentação de seus animais dentro da propriedade rural. O sistema permitirá aos usuários cadastrar suas propriedades, definir os limites físicos do lote e cadastrar os animais, associando a eles dispositivos de rastreamento. O sistema oferecerá a funcionalidade de visualização em tempo real da localização dos animais e emitirá alertas em caso de fuga dos limites estabelecidos.


## Como inicializar o projeto?
- Clonar repositório
``` bash
git clone [link do repositório]
```
- Criar ambiente virtual
``` bash
python -m venv venv 
```
- Ativar ambiente virtual (Windows)
``` bash
venv\Scripts\activate.bat
```
- Instalar dependências
```bash
pip install django
pip install python-decouple
```
- Executar o servidor django
```bash
python manage.py runserver
```
- Acessar: http://127.0.0.1:8000/mapa
