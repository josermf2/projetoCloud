# Terraform-AWS CLI

## Desenvolvedor:
- José Rafael Martins Fernandes

## Sobre o projeto:
-  O Terraform-AWS CLI é uma command-line interface que permite ao usuário fazer as seguintes operações:
    - Criar instânciaS EC2 do tipo micro ou small e associa-láS a um grupo de segurança
    - Criar security groups
    - Criar usuários IAM na AWS
    - Criar VPCs com uma subnet e um internet gateway

## Dependencias:
* Python 3.8+ (https://www.python.org/downloads)
* Terraform (https://developer.hashicorp.com/terraform/downloads)


## Como usar:
- Clone o repositório para seu computador com o seguinte comando: 
<pre><code> git clone https://github.com/josermf2/projetoCloud.git</code></pre>
- Entre na pasta pythonCLI e instale as bibliotecas necessárias utilizando o seguinte comando:
<pre><code> pip install -r requirements.txt</code></pre>
- Carregue suas credenciais AWS no terminal utilizando o seguinte comando:
<pre><code> 
$ export AWS_ACCESS_KEY_ID="anaccesskey"
$ export AWS_SECRET_ACCESS_KEY="asecretkey"
</code></pre>
- Caso prefira, utilize o AWS CLI e crie um perfil com suas credenciais, dessa forma não será necessário carregar as credenciais todas as vezes que for utilizar um novo bash. Tutorial: https://www.youtube.com/watch?v=2Q39eWPLVpg&list=PLWQmZVQayUUIgSmOj3GPH2BJcn0hOzIaP&index=6
- Rode o arquivo pythonCLI.py e utilize o Terraform-AWS CLI
