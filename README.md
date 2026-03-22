# CIN0168

## Instruções de Execução

Para reproduzir os testes, siga os passos abaixo:

### Pré-requisitos
* Possuir o Python 3.12.1 instalado.

### 1. Instalação
Instale o framework de teste necessário via terminal:
```bash
pip install pytest
```

### 2. Comando Principal
Para executar todos os testes da suíte, utilize o seguinte comando na raiz do diretório:
```bash
pytest test_scholarship.py
```

### 3. Estrutura da Suíte de Testes

A suíte implementada cobre os seguintes requisitos mínimos estabelecidos:
- Casos de APPROVED: Valida candidatos que atendem a todos os critérios;
- Casos de MANUAL_REVIEW: Valida transições de idade e notas que exigem revisão;
- Casos de REJECTED: Testes para múltiplos motivos (GPA baixo, falta de cursos, histórico disciplinar);
- Entradas Inválidas: Verificação de limites de domínio para GPA (0-10) e Frequência (0-100);
- Valores Limite: Testes nas fronteiras exatas de decisão (como GPA 6.0 e 7.0);
- Testes Estruturais: Exercitam diferentes caminhos, decisões if/else e fluxos de execução do código.