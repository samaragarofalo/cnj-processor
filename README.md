# CNJ Processor – Serviço Serverless para Processamento Assíncrono de Processos Judiciais

Este projeto implementa um serviço assíncrono baseado em arquitetura serverless na AWS com o objetivo de receber e processar números CNJ (Cadastro Nacional de Justiça). A solução foi construída para atender cenários de baixa e alta volumetria, garantindo escalabilidade, isolamento entre responsabilidades e observabilidade do fluxo de processamento.

## Objetivo

A proposta é receber via API um número CNJ, encaminhá-lo a uma fila para processamento assíncrono e, posteriormente, consultar uma fonte externa (mockada neste projeto) para obter os dados associados ao número informado. Por fim, os dados obtidos são armazenados em uma base interna.


## Arquitetura da Solução

A arquitetura foi implementada com os seguintes componentes:

- **AWS API Gateway (HTTP API)**  
  Recebe os CNJs via endpoint público.

- **AWS Lambda (api handler)**  
  Valida o número CNJ e publica na fila SQS.

- **AWS SQS**  
  Fila intermediária para desacoplamento e controle de volume.

- **AWS Lambda (worker)**  
  Consome as mensagens da fila, realiza a chamada externa e armazena os dados.

- **AWS DynamoDB**  
  Armazena o CNJ junto aos dados retornados da API externa.

- **Cognito User Pool**  
  Permite autenticação via JWT, implementado como extensão de segurança.

---

## Estrutura de Diretórios

```bash
.
├── app                  # Regras de negócio (casos de uso)
│   └── usecase.py
├── domain               # Entidades do domínio
│   └── cnj.py
├── infra                # Integrações externas e persistência
│   ├── db.py
│   └── client_api.py
├── protocol             # Lambda handlers (entrada da aplicação)
│   ├── lambda_handler.py
│   └── lambda_worker.py
├── tests                # Testes unitários
│   ├── test_usecase.py
│   └── test_lambda_handler.py
├── serverless.yml       # Definição da infraestrutura (IaC)
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação e explicação da estrutura definida
