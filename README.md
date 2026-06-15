# 🏃 Corridas de Rua — Sistema de Inscrição

Sistema de gerenciamento de inscrições para eventos de corrida e caminhada de rua, desenvolvido em Python com arquitetura limpa (Clean Architecture).

---

## 📋 Descrição

Permite cadastrar corredores em eventos de diferentes percursos, consultar inscrições, gerenciar participantes e visualizar estatísticas por percurso e faixa etária. Os dados são persistidos em arquivo de texto (`corredores.txt`), sem dependência de banco de dados externo.

---

## 🗂️ Estrutura do Projeto

```
corridas_rua/
├── main.py                          # Ponto de entrada da aplicação
├── data/
│   └── corredores.txt               # Persistência dos dados
├── domain/
│   ├── entities/
│   │   └── corredor.py              # Entidade Corredor
│   └── services/
│       ├── faixa_etaria_service.py  # Regras de agrupamento por idade
│       └── percurso_service.py      # Regras de validação de percurso
├── application/
│   ├── use_cases/
│   │   ├── inscrever_corredor.py
│   │   ├── remover_corredor.py
│   │   ├── listar_corredores.py
│   │   ├── listar_por_percurso.py
│   │   ├── listar_percursos.py
│   │   └── listar_faixas_etarias.py
│   └── interfaces/
│       └── corredor_repository.py   # Contrato do repositório
├── infrastructure/
│   ├── repositories/
│   │   └── txt_corredor_repository.py  # Implementação em .txt
│   └── persistence/
│       └── arquivo_manager.py       # Leitura e escrita no arquivo
├── presentation/
│   ├── menu.py                      # Exibição do menu principal
│   ├── inputs.py                    # Coleta de dados do usuário
│   └── outputs.py                   # Formatação e exibição de resultados
└── README.md
```

---

## ✅ Funcionalidades

| Opção | Descrição                                                                       |
| ----- | ------------------------------------------------------------------------------- |
| 1     | **Inscrever corredor** — Cadastra nome, data de nascimento, telefone e percurso |
| 2     | **Remover corredor** — Remove um corredor pelo nome ou identificador            |
| 3     | **Listar corredores** — Exibe todos os inscritos em ordem alfabética            |
| 4     | **Listar por percurso** — Filtra inscritos de um percurso específico            |
| 5     | **Listar percursos** — Mostra cada percurso com o total de inscritos            |
| 6     | **Listar faixas etárias** — Agrupa corredores por faixa etária com totais       |
| 0     | **Sair**                                                                        |

---

## 🛣️ Percursos Disponíveis

- 3 km
- 5 km
- 10 km
- 15 km
- 21 km _(Meia Maratona)_
- 42 km _(Maratona)_

---

## 👥 Faixas Etárias

| Faixa         | Intervalo    |
| ------------- | ------------ |
| Jovem         | 18 a 29 anos |
| Adulto        | 30 a 39 anos |
| Adulto Sênior | 40 a 49 anos |
| Sênior        | 50 a 59 anos |
| Veterano      | 60+ anos     |

---

## 🚀 Como Executar

**Pré-requisitos:** Python 3.8 ou superior.

```bash
# Clone o repositório
git clone https://gitlab.com/robertofilholopesg202/projeto_algoritimos.git
cd projeto_algoritimos/corridas_rua

# Execute o sistema
python main.py
```

Nenhuma dependência externa é necessária — a aplicação usa apenas a biblioteca padrão do Python.

---

## 🏛️ Arquitetura

O projeto segue os princípios da **Clean Architecture**:

- **Domain** — Entidades e regras de negócio puras, sem dependências externas.
- **Application** — Casos de uso que orquestram as regras de domínio.
- **Infrastructure** — Implementação concreta da persistência em arquivo `.txt`.
- **Presentation** — Interface com o usuário via terminal (menu, inputs, outputs).

Essa separação garante que as regras de negócio sejam independentes da forma de armazenamento ou de exibição, facilitando manutenção e testes.

---

## 👤 Autor

**Roberto Filho Lopes**  
Projeto desenvolvido para a disciplina de Algoritmos.  
GitLab: [@robertofilholopesg202](https://gitlab.com/robertofilholopesg202)

---

## 📄 Licença

Este projeto é de uso acadêmico.
