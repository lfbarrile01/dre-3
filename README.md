Implementação do Airflow utilizando o servico gerenciado da Amazon (MWAA)

O Amazon MWAA é um serviço completamente gerenciado que facilita a execução de workflows do Apache Airflow na AWS. Ele permite que você crie, execute e monitore fluxos de trabalho de maneira mais simples, sem precisar gerenciar a infraestrutura subjacente.

Com o MWAA não é necessário se preocupar com N aspectos que na construção em partições tornaria a administração do produto muito mais complexa.

Podemos citar os seguintes pontos que o MWAA contempla e que ajudam na Implementação
* Gerenciamento simplificado: Com o MWAA, você não precisa se preocupar com a infraestrutura subjacente, pois a AWS cuida de tarefas como provisionamento, gerenciamento e escalabilidade.
* Escalabilidade automática: O serviço pode escalar automaticamente para atender à demanda de recursos de acordo com o tamanho e a complexidade dos seus workflows.
* Segurança integrada: O MWAA oferece integrações com serviços da AWS, como IAM (Identity and Access Management), VPC (Virtual Private Cloud), e CloudWatch, para garantir que suas tarefas sejam executadas de forma segura e eficiente.
* Alta disponibilidade: O MWAA é projetado para ser resiliente e com alta disponibilidade, garantindo que seus workflows continuem sendo executados sem interrupções.
* Facilidade de integração com outros serviços AWS: Você pode integrar facilmente o MWAA com outros serviços da AWS, como S3, DynamoDB, Lambda, Redshift, entre outros, para criar soluções de dados completas.

Como MWAA funciona?

Os workflows são definidos da forma padrão que já conhecemos, utilizando arquivos de códigos em Python que você criará a sua DAG
Quando uma DAG é submetida o serviço gerenciado da AWS vai executar de acordo com o Airflow Scheduler

Basicamente na arquitetura temos:

Amazon MWAA (Serviço Gerenciado)
O Amazon MWAA é o serviço que executa e gerencia os fluxos de trabalho do Apache Airflow de forma totalmente gerenciada pela AWS. Ele provê a infraestrutura necessária, como servidores e escalabilidade automática.
O MWAA é responsável por orquestrar a execução dos DAGs (fluxos de trabalho no Apache Airflow), sem que você precise configurar servidores ou lidar com problemas de infraestrutura.
Armazenamento e Arquivos

Amazon S3: O serviço de armazenamento da AWS (S3) é utilizado para armazenar seus arquivos de configuração, DAGs (arquivos de definição de workflow), logs e outros dados relacionados aos seus workflows. O MWAA tem integração direta com o S3, de forma que seus workflows podem acessar dados armazenados na nuvem de maneira fácil.
S3 também armazena logs da execução das tarefas do Airflow, permitindo monitoramento e rastreamento.
Execução de Workflows

O MWAA executa seus workflows de acordo com o que você configurou nos DAGs. A execução pode envolver a orquestração de tarefas e a integração com outros serviços da AWS, como AWS Lambda, Amazon DynamoDB, Redshift, RDS, entre outros, para que você possa automatizar diversos processos de dados.
Monitoramento e Logs

O Amazon CloudWatch é utilizado para monitoramento e log da execução do Airflow. Você pode ver o status dos seus workflows, alertas sobre falhas e resultados de execução através do painel do CloudWatch.
Segurança

O AWS Identity and Access Management (IAM) controla o acesso aos recursos. O IAM garante que apenas os usuários e serviços autorizados possam interagir com seus workflows e dados.

O MWAA também pode ser configurado para operar dentro de uma VPC (Virtual Private Cloud), o que aumenta a segurança ao isolar o tráfego de rede, no nosso caso temos uma VPC separada para a camada de Database do produto e uma VPC apartada para a camada Web em que há exposição do Airflow Webserver através de um Application Load Balancer.
